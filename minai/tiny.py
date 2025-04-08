"""From Cluster of stars study group"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../40_tiny_stories_bpe.ipynb.

# %% auto 0
__all__ = ['path', 'txt_L', 'txt_gpt4', 'txt_raw', 'tokenizer', 'total_len', 'split', 'ctx_len', 'trn_txts', 'val_txts', 'trn_ds',
           'val_ds', 'bs', 'trn_dl', 'val_dl', 'dls', 'xb', 'yb', 'cfg', 'model', 'load_json', 'TinyDataset',
           'SDPACausalAttentionBlock', 'FeedForward', 'TransformerBlock', 'GPTModel', 'get_total_params',
           'get_total_memory', 'generate_text_simple', 'text_to_token_ids', 'token_ids_to_text', 'generate',
           'GenerateTextCB', 'MixedPrecision', 'loss_fn', 'LLMMetricsCB', 'TinyProgressCB', 'main']

# %% ../40_tiny_stories_bpe.ipynb 5
from datasets import load_dataset
import tiktoken
import torch
import math
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor, BoolTensor
from minai import *

from functools import partial
from torch.optim import lr_scheduler

# %% ../40_tiny_stories_bpe.ipynb 7
import json
from fastcore.all import *

def load_json(path):
    "Load JSON file from path"
    return json.loads(path.read_text())

# %% ../40_tiny_stories_bpe.ipynb 8
path = Path.home()/'git/minai/TinyStories_All_data'
path.ls()

# %% ../40_tiny_stories_bpe.ipynb 9
txt_L = L(load_json(path/'data23.json'))
txt_L[0]

# %% ../40_tiny_stories_bpe.ipynb 12
txt_gpt4 = L([o for o in txt_L if o['source'] == 'GPT-4'])
len(txt_gpt4)

# %% ../40_tiny_stories_bpe.ipynb 13
txt_raw = ' '.join([o['story'] for o in txt_gpt4])

# %% ../40_tiny_stories_bpe.ipynb 18
from minbpe import RegexTokenizer

# %% ../40_tiny_stories_bpe.ipynb 19
tokenizer = RegexTokenizer()
# tokenizer.train(txt_raw, vocab_size=3000)

tokenizer.load((path/"tok3k_regex.model").name) # loads the model back from disk
tokenizer.encode("hello world") # string -> tokens

# %% ../40_tiny_stories_bpe.ipynb 24
# Code from llm from scratch
class TinyDataset(Dataset):
    def __init__(self, txt, tokenizer, ctx_len):
        self.inp = []
        self.targ = []
#         token_ids = tokenizer.encode(txt, allowed_special={"<|endoftext|>"})
        token_ids = tokenizer.encode(txt)
        for i in range(0, len(token_ids) - ctx_len, ctx_len):
            inp_chunk = token_ids[i:i + ctx_len]
            targ_chunk = token_ids[i + 1: i + ctx_len + 1]
            self.inp.append(torch.tensor(inp_chunk))
            self.targ.append(torch.tensor(targ_chunk))

    def __len__(self): return len(self.inp)

    def __getitem__(self, idx): return self.inp[idx], self.targ[idx]

# %% ../40_tiny_stories_bpe.ipynb 26
# Using around 55k
total_len = int(len(txt_raw) // 20)
total_len

# %% ../40_tiny_stories_bpe.ipynb 27
split = int(total_len * .9)
split

# %% ../40_tiny_stories_bpe.ipynb 28
ctx_len = 1024
trn_txts = txt_raw[:split]
val_txts = txt_raw[split:total_len]

trn_ds = TinyDataset(trn_txts, tokenizer, ctx_len)
val_ds = TinyDataset(val_txts, tokenizer, ctx_len)
trn_ds[0]

# %% ../40_tiny_stories_bpe.ipynb 32
bs = 8

trn_dl, val_dl = get_dls(trn_ds, val_ds, bs, drop_last=True)
dls = DataLoaders(trn_dl, val_dl)
xb,yb = next(iter(trn_dl))
xb.shape,yb.shape

# %% ../40_tiny_stories_bpe.ipynb 36
class SDPACausalAttentionBlock(nn.Module):
    """
    Attention block implementing multi-head causal (masked) attention using
    PyTorch's scaled_dot_product_attention (SDPA).
    """

    def __init__(
        self,
        hidden_dim: int,
        num_heads: int,
        dropout: float = 0.0,
    ):
        """
        Initialize the causal attention block with SDPA implementation.
        """
        super().__init__()
        if hidden_dim % num_heads != 0: raise Exception("hidden_dim not divisible by num_heads")
        self.head_dim = hidden_dim // num_heads
        self.num_heads = num_heads
        self.Wq, self.Wk, self.Wv = nn.Linear(hidden_dim, hidden_dim), nn.Linear(hidden_dim, hidden_dim), nn.Linear(hidden_dim, hidden_dim)
#         self.Wo = nn.Linear(hidden_dim, hidden_dim)
#         self.dropout = nn.Dropout(dropout)

    def forward(self, x: Tensor) -> Tensor:
        batch_size, seq_len, hidden_dim = x.shape
        q,k,v = self.Wq(x), self.Wk(x), self.Wv(x) # [batch_size, seq_len, d_out]

        sdpa_ctx = torch.nn.functional.scaled_dot_product_attention(
            q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1,2), 
            k.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1,2), 
            v.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1,2), 
            dropout_p=0.0, is_causal=True, scale=None)
        sdpa_ctx = sdpa_ctx.transpose(1,2).view(batch_size, seq_len, -1)
#         return self.dropout(self.Wo(sdpa_ctx))
        return sdpa_ctx

# %% ../40_tiny_stories_bpe.ipynb 38
class FeedForward(nn.Module):
    def __init__(self, in_dim, hidden_dim, act=nn.ReLU()):
        super().__init__()
        self.l1 = nn.Linear(in_dim, hidden_dim)
        self.act = act
        self.l2 = nn.Linear(hidden_dim, in_dim)
    
    def forward(self, x):
        return self.l2(self.act(self.l1(x)))

# %% ../40_tiny_stories_bpe.ipynb 40
class TransformerBlock(nn.Module):
    def __init__(self, emb_dim, ctx_len, n_head, drop_out=0, ff_mult=4, qkv_bias=False):
        super().__init__()
        self.ln1 = nn.LayerNorm(emb_dim)
        self.ln2 = nn.LayerNorm(emb_dim)
        self.mha = SDPACausalAttentionBlock(hidden_dim=emb_dim, num_heads=n_head, dropout=drop_out)
        self.do = nn.Dropout(drop_out)
        self.ff = FeedForward(emb_dim, emb_dim*ff_mult)
    
    def forward(self, x):
        skip1 = x
        x = self.ln1(x)
        x = self.mha(x)
        x = self.do(x)
        x = x + skip1
        
        skip2 = x
        x = self.ln2(x)
        x = self.ff(x)
        x = self.do(x)
        x = x + skip2
        return x

# %% ../40_tiny_stories_bpe.ipynb 42
class GPTModel(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.token_emb = nn.Embedding(cfg['vocab_sz'], cfg['emb_dim'])
        self.pos_emb = nn.Embedding(cfg['vocab_sz'], cfg['emb_dim'])
        self.do = nn.Dropout(cfg['drop_out'])
        self.tb = nn.Sequential(
            *[TransformerBlock(cfg['emb_dim'], cfg['ctx_len'], cfg['n_head'], cfg['drop_out_tb'],
                              cfg['ff_mult'], cfg['qkv_bias']) for _ in range(cfg['n_tb'])])
        self.final_ln = nn.LayerNorm(cfg['emb_dim'])
        self.final_l  = nn.Linear(cfg['emb_dim'], cfg['vocab_sz'])
    
    def forward(self, x):
        bs, seq_len = x.shape
        tok = self.token_emb(x)
        pos = self.pos_emb(torch.arange(seq_len, device=x.device))
        x = self.do(tok + pos)
        x = self.tb(x)
        x = self.final_ln(x)
        x = self.final_l(x)
        return x

# %% ../40_tiny_stories_bpe.ipynb 43
def get_total_params(model): return sum(p.numel() for p in model.parameters())

# %% ../40_tiny_stories_bpe.ipynb 44
def get_total_memory(model):
    total_params = get_total_params(model)
    total_size_bytes = total_params * 4   # Assuming fp32
    # Convert to megabytes
    total_size_mb = total_size_bytes / (1024 * 1024)
    print(f"Total params: {total_params:,}")
    print(f"Total size: {total_size_mb:.2f} MB")

# %% ../40_tiny_stories_bpe.ipynb 46
def generate_text_simple(model, idx, max_new_tokens, context_size):
    # idx is (batch, n_tokens) array of indices in the current context
    for _ in range(max_new_tokens):
        idx_cond = idx[:, -context_size:]  # Crop current context if it exceeds the supported context size
        with torch.no_grad(): logits = model(idx_cond)         # (bs, n_tokens, vocab_sz)
        logits = logits[:, -1, :]                              # (bs, vocab_sz)
        probas = torch.softmax(logits, dim=-1)                 # (bs, vocab_sz)
        idx_next = torch.argmax(probas, dim=-1, keepdim=True)  # (bs, 1)
        idx = torch.cat((idx, idx_next), dim=1)                # (bs, n_tokens+1)
    return idx

# %% ../40_tiny_stories_bpe.ipynb 47
def text_to_token_ids(text, tokenizer):
    encoded = tokenizer.encode(text, allowed_special={'<|endoftext|>'})
    encoded_tensor = torch.tensor(encoded).unsqueeze(0) # add batch dimension
    return encoded_tensor

# %% ../40_tiny_stories_bpe.ipynb 48
def token_ids_to_text(token_ids, tokenizer):
    flat = token_ids.squeeze(0) # remove batch dimension
    return tokenizer.decode(flat.tolist())

# %% ../40_tiny_stories_bpe.ipynb 49
def generate(model, idx, max_new_tokens, context_size, temperature=0.0, top_k=None, eos_id=None):
    for _ in range(max_new_tokens):
        idx_cond = idx[:, -context_size:].to(def_device)
        with torch.no_grad():
            logits = model(idx_cond)
        logits = logits[:, -1, :]
        if top_k is not None:
            # Keep only top_k values
            top_logits, _ = torch.topk(logits, top_k)
            min_val = top_logits[:, -1]
            logits = torch.where(logits < min_val, torch.tensor(float("-inf")).to(logits.device), logits)
        if temperature > 0.0:
            logits = logits / temperature
            probs = torch.softmax(logits, dim=-1)  # (batch_size, context_len)
            idx_next = torch.multinomial(probs, num_samples=1)  # (batch_size, 1)
        else:
            idx_next = torch.argmax(logits, dim=-1, keepdim=True)  # (batch_size, 1)

        if idx_next == eos_id:  # Stop generating early if end-of-sequence token is encountered and eos_id is specified
            break
        idx = torch.cat((idx, idx_next), dim=1)  # (batch_size, num_tokens+1)
    return idx

# %% ../40_tiny_stories_bpe.ipynb 50
class GenerateTextCB(Callback):
    pass

# %% ../40_tiny_stories_bpe.ipynb 52
from torcheval.metrics import  MulticlassAccuracy

# %% ../40_tiny_stories_bpe.ipynb 53
class MixedPrecision(TrainCB):
    order = DeviceCB.order+10
    def __init__(self, n_inp=1, dtype=torch.bfloat16):
        super().__init__(n_inp=n_inp)
        self.dtype=dtype
    
    def before_fit(self, learn): self.scaler = torch.amp.GradScaler('cuda')

    def before_batch(self, learn):
        self.autocast = torch.autocast("cuda", dtype=self.dtype)
        self.autocast.__enter__()

    def after_loss(self, learn): self.autocast.__exit__(None, None, None)
        
    def backward(self, learn): self.scaler.scale(learn.loss).backward()

    def step(self, learn):
        self.scaler.step(learn.opt)
        self.scaler.update()

# %% ../40_tiny_stories_bpe.ipynb 54
def loss_fn(pred, targ): return F.cross_entropy(pred.flatten(0, 1), targ.flatten())

# %% ../40_tiny_stories_bpe.ipynb 55
cfg = {
    'n_tb': 4,    # num transformer blocks
    'vocab_sz': 3000,
    'emb_dim': 256 // 64,
    'ctx_len': ctx_len,
    'n_head': 4,
    'drop_out': 0,
    'drop_out_tb': 0,  # dropout within transformer blocks
    'ff_mult': 4,
    'qkv_bias': False,
}

# %% ../40_tiny_stories_bpe.ipynb 56
model = torch.compile(GPTModel(cfg).to(def_device), mode="reduce-overhead")
get_total_memory(model)

# %% ../40_tiny_stories_bpe.ipynb 57
class LLMMetricsCB(MetricsCB):
    def __init__(self, *ms, **metrics):
        super().__init__(*ms, **metrics)
    
    def after_batch(self, learn):
        x,y,*_ = learn.batch
        for m in self.metrics.values(): m.update(to_cpu(learn.preds.flatten(0, 1)), y.flatten())
        self.loss.update(learn.loss, weight=len(x))

# %% ../40_tiny_stories_bpe.ipynb 58
class TinyProgressCB(ProgressCB):
#     order = MetricsCB.order+1
    def __init__(self, plot=False, table=True): store_attr()
    
    def _log(self, d): print(d)

# %% ../40_tiny_stories_bpe.ipynb 59
# opt = torch.optim.AdamW
# cbs = [LLMMetricsCB(accuracy=MulticlassAccuracy()), ProgressCB(plot=False), DeviceCB(),  MixedPrecision()]
# cbs = [LLMMetricsCB(accuracy=MulticlassAccuracy(device=def_device)), TinyProgressCB(), DeviceCB(), TrainCB()]
# learn = Learner(model, dls, loss_func=loss_fn, cbs=cbs, opt_func=opt)
# learn.lr_find()

# %% ../40_tiny_stories_bpe.ipynb 60
# set_seed(42)
# lr, epochs = 3e-4, 1
# tmax = epochs * len(dls.train)
# sched = partial(lr_scheduler.OneCycleLR, max_lr=lr, total_steps=tmax)
# xtra = [BatchSchedCB(sched)]
# model = torch.compile(GPTModel(cfg).to(def_device), mode="reduce-overhead")
# cbs = [LLMMetricsCB(accuracy=MulticlassAccuracy()), ProgressCB(plot=True), DeviceCB(),  MixedPrecision()]
# # cbs = [LLMMetricsCB(accuracy=MulticlassAccuracy()), ProgressCB(plot=True), DeviceCB(), TrainCB()]
# learn = Learner(model, dls, loss_func=loss_fn, cbs=cbs+xtra, opt_func=opt)
# learn.fit(epochs, lr=lr)

# %% ../40_tiny_stories_bpe.ipynb 61
# start_context = "Once upon a time, there lived a bunny in a field. Her name was Lucy. Lucy loved to have feasts and parties with her bunny friends. One day, when Lucy was about to leave for a feast at a friend's house, she realized she's starting to feel sick. She was so weak she could"
# model.eval()
# token_ids = generate(
#     model=model.eval(),
#     idx=text_to_token_ids("Once upon a time, there lived a bunny in a field. Her name was Lucy. Lucy loved to have feasts and parties with her bunny friends. One day, when Lucy was about to leave for a feast at a friend's house, she realized she's starting to feel sick. She was so weak she could", tokenizer).to(def_device),
#     max_new_tokens=150,
#     context_size=cfg["ctx_len"],
#     top_k=25,
#     temperature=1
# )

# print("Output text:\n", token_ids_to_text(token_ids, tokenizer))

# %% ../40_tiny_stories_bpe.ipynb 62
from fastcore.script import *

@call_parse
def main(
    n_tb:Param("Number of transformer blocks", int)=4,
    vocab_sz:Param("Vocabulary size", int)=3000,
    emb_dim:Param("Embedding dimension", int)=64,
    ctx_len:Param("Context length", int)=256,
    n_head:Param("Number of attention heads", int)=4,
    epochs:Param("Number of epochs", int)=1,
    lr:Param("Learning rate", float)=3e-4,
    bs:Param("Batch size", int)=4
):
    "Run training with specified parameters"
    print(n_tb, vocab_sz, emb_dim, ctx_len, n_head, epochs, lr, bs)
    cfg = dict(n_tb=n_tb, vocab_sz=vocab_sz, emb_dim=emb_dim, ctx_len=ctx_len, 
              n_head=n_head, drop_out=0, drop_out_tb=0, ff_mult=4, qkv_bias=False)
    
    model = torch.compile(GPTModel(cfg).to(def_device), mode="reduce-overhead")
    
    cbs = [LLMMetricsCB(accuracy=MulticlassAccuracy()), TinyProgressCB(), DeviceCB(), MixedPrecision()]
    learn = Learner(model, dls, loss_func=loss_fn, cbs=cbs, opt_func=torch.optim.AdamW)
    
    tmax = epochs * len(dls.train)
    sched = partial(lr_scheduler.OneCycleLR, max_lr=lr, total_steps=tmax)
    xtra = [BatchSchedCB(sched)]
    
    learn = Learner(model, dls, loss_func=loss_fn, cbs=cbs+xtra, opt_func=torch.optim.AdamW)
    learn.fit(epochs, lr=lr)
    
    return learn
