# Autogenerated by nbdev

d = { 'settings': { 'branch': 'master',
                'doc_baseurl': '/',
                'doc_host': 'https://minai.fast.ai',
                'git_url': 'https://github.com/fastai/minai/',
                'lib_path': 'minai'},
  'syms': { 'minai.core': { 'minai.core.AccelerateCB': ('core.html#acceleratecb', 'minai/core.py'),
                            'minai.core.AccelerateCB.__init__': ('core.html#acceleratecb.__init__', 'minai/core.py'),
                            'minai.core.AccelerateCB.after_fit': ('core.html#acceleratecb.after_fit', 'minai/core.py'),
                            'minai.core.AccelerateCB.backward': ('core.html#acceleratecb.backward', 'minai/core.py'),
                            'minai.core.AccelerateCB.before_fit': ('core.html#acceleratecb.before_fit', 'minai/core.py'),
                            'minai.core.ActivationStats': ('core.html#activationstats', 'minai/core.py'),
                            'minai.core.ActivationStats.__init__': ('core.html#activationstats.__init__', 'minai/core.py'),
                            'minai.core.ActivationStats.color_dim': ('core.html#activationstats.color_dim', 'minai/core.py'),
                            'minai.core.ActivationStats.dead_chart': ('core.html#activationstats.dead_chart', 'minai/core.py'),
                            'minai.core.ActivationStats.plot_stats': ('core.html#activationstats.plot_stats', 'minai/core.py'),
                            'minai.core.BaseSchedCB': ('core.html#baseschedcb', 'minai/core.py'),
                            'minai.core.BaseSchedCB.__init__': ('core.html#baseschedcb.__init__', 'minai/core.py'),
                            'minai.core.BaseSchedCB._step': ('core.html#baseschedcb._step', 'minai/core.py'),
                            'minai.core.BaseSchedCB.before_fit': ('core.html#baseschedcb.before_fit', 'minai/core.py'),
                            'minai.core.BatchSchedCB': ('core.html#batchschedcb', 'minai/core.py'),
                            'minai.core.BatchSchedCB.after_batch': ('core.html#batchschedcb.after_batch', 'minai/core.py'),
                            'minai.core.BatchTransformCB': ('core.html#batchtransformcb', 'minai/core.py'),
                            'minai.core.BatchTransformCB.__init__': ('core.html#batchtransformcb.__init__', 'minai/core.py'),
                            'minai.core.BatchTransformCB.before_batch': ('core.html#batchtransformcb.before_batch', 'minai/core.py'),
                            'minai.core.Callback': ('core.html#callback', 'minai/core.py'),
                            'minai.core.CancelBatchException': ('core.html#cancelbatchexception', 'minai/core.py'),
                            'minai.core.CancelEpochException': ('core.html#cancelepochexception', 'minai/core.py'),
                            'minai.core.CancelFitException': ('core.html#cancelfitexception', 'minai/core.py'),
                            'minai.core.CapturePreds': ('core.html#capturepreds', 'minai/core.py'),
                            'minai.core.CapturePreds.after_batch': ('core.html#capturepreds.after_batch', 'minai/core.py'),
                            'minai.core.CapturePreds.after_fit': ('core.html#capturepreds.after_fit', 'minai/core.py'),
                            'minai.core.CapturePreds.before_fit': ('core.html#capturepreds.before_fit', 'minai/core.py'),
                            'minai.core.CycleDL': ('core.html#cycledl', 'minai/core.py'),
                            'minai.core.CycleDL.__init__': ('core.html#cycledl.__init__', 'minai/core.py'),
                            'minai.core.CycleDL.__iter__': ('core.html#cycledl.__iter__', 'minai/core.py'),
                            'minai.core.CycleDL.__len__': ('core.html#cycledl.__len__', 'minai/core.py'),
                            'minai.core.DataLoaders': ('core.html#dataloaders', 'minai/core.py'),
                            'minai.core.DataLoaders.__init__': ('core.html#dataloaders.__init__', 'minai/core.py'),
                            'minai.core.DataLoaders.from_dd': ('core.html#dataloaders.from_dd', 'minai/core.py'),
                            'minai.core.Dataset': ('core.html#dataset', 'minai/core.py'),
                            'minai.core.Dataset.__getitem__': ('core.html#dataset.__getitem__', 'minai/core.py'),
                            'minai.core.Dataset.__init__': ('core.html#dataset.__init__', 'minai/core.py'),
                            'minai.core.Dataset.__len__': ('core.html#dataset.__len__', 'minai/core.py'),
                            'minai.core.DeviceCB': ('core.html#devicecb', 'minai/core.py'),
                            'minai.core.DeviceCB.__init__': ('core.html#devicecb.__init__', 'minai/core.py'),
                            'minai.core.DeviceCB.before_batch': ('core.html#devicecb.before_batch', 'minai/core.py'),
                            'minai.core.DeviceCB.before_fit': ('core.html#devicecb.before_fit', 'minai/core.py'),
                            'minai.core.EpochSchedCB': ('core.html#epochschedcb', 'minai/core.py'),
                            'minai.core.EpochSchedCB.after_epoch': ('core.html#epochschedcb.after_epoch', 'minai/core.py'),
                            'minai.core.GeneralRelu': ('core.html#generalrelu', 'minai/core.py'),
                            'minai.core.GeneralRelu.__init__': ('core.html#generalrelu.__init__', 'minai/core.py'),
                            'minai.core.GeneralRelu.forward': ('core.html#generalrelu.forward', 'minai/core.py'),
                            'minai.core.HasLearnCB': ('core.html#haslearncb', 'minai/core.py'),
                            'minai.core.HasLearnCB.after_fit': ('core.html#haslearncb.after_fit', 'minai/core.py'),
                            'minai.core.HasLearnCB.before_fit': ('core.html#haslearncb.before_fit', 'minai/core.py'),
                            'minai.core.Hook': ('core.html#hook', 'minai/core.py'),
                            'minai.core.Hook.__del__': ('core.html#hook.__del__', 'minai/core.py'),
                            'minai.core.Hook.__init__': ('core.html#hook.__init__', 'minai/core.py'),
                            'minai.core.Hook.remove': ('core.html#hook.remove', 'minai/core.py'),
                            'minai.core.Hooks': ('core.html#hooks', 'minai/core.py'),
                            'minai.core.Hooks.__del__': ('core.html#hooks.__del__', 'minai/core.py'),
                            'minai.core.Hooks.__delitem__': ('core.html#hooks.__delitem__', 'minai/core.py'),
                            'minai.core.Hooks.__enter__': ('core.html#hooks.__enter__', 'minai/core.py'),
                            'minai.core.Hooks.__exit__': ('core.html#hooks.__exit__', 'minai/core.py'),
                            'minai.core.Hooks.__init__': ('core.html#hooks.__init__', 'minai/core.py'),
                            'minai.core.Hooks.remove': ('core.html#hooks.remove', 'minai/core.py'),
                            'minai.core.HooksCallback': ('core.html#hookscallback', 'minai/core.py'),
                            'minai.core.HooksCallback.__init__': ('core.html#hookscallback.__init__', 'minai/core.py'),
                            'minai.core.HooksCallback.__iter__': ('core.html#hookscallback.__iter__', 'minai/core.py'),
                            'minai.core.HooksCallback.__len__': ('core.html#hookscallback.__len__', 'minai/core.py'),
                            'minai.core.HooksCallback._hookfunc': ('core.html#hookscallback._hookfunc', 'minai/core.py'),
                            'minai.core.HooksCallback.after_fit': ('core.html#hookscallback.after_fit', 'minai/core.py'),
                            'minai.core.HooksCallback.before_fit': ('core.html#hookscallback.before_fit', 'minai/core.py'),
                            'minai.core.LRFinderCB': ('core.html#lrfindercb', 'minai/core.py'),
                            'minai.core.LRFinderCB.__init__': ('core.html#lrfindercb.__init__', 'minai/core.py'),
                            'minai.core.LRFinderCB.after_batch': ('core.html#lrfindercb.after_batch', 'minai/core.py'),
                            'minai.core.LRFinderCB.before_fit': ('core.html#lrfindercb.before_fit', 'minai/core.py'),
                            'minai.core.LRFinderCB.cleanup_fit': ('core.html#lrfindercb.cleanup_fit', 'minai/core.py'),
                            'minai.core.Learner': ('core.html#learner', 'minai/core.py'),
                            'minai.core.Learner.__getattr__': ('core.html#learner.__getattr__', 'minai/core.py'),
                            'minai.core.Learner.__init__': ('core.html#learner.__init__', 'minai/core.py'),
                            'minai.core.Learner._fit': ('core.html#learner._fit', 'minai/core.py'),
                            'minai.core.Learner._one_batch': ('core.html#learner._one_batch', 'minai/core.py'),
                            'minai.core.Learner._one_epoch': ('core.html#learner._one_epoch', 'minai/core.py'),
                            'minai.core.Learner.callback': ('core.html#learner.callback', 'minai/core.py'),
                            'minai.core.Learner.fit': ('core.html#learner.fit', 'minai/core.py'),
                            'minai.core.Learner.one_epoch': ('core.html#learner.one_epoch', 'minai/core.py'),
                            'minai.core.Learner.training': ('core.html#learner.training', 'minai/core.py'),
                            'minai.core.MetricsCB': ('core.html#metricscb', 'minai/core.py'),
                            'minai.core.MetricsCB.__init__': ('core.html#metricscb.__init__', 'minai/core.py'),
                            'minai.core.MetricsCB._log': ('core.html#metricscb._log', 'minai/core.py'),
                            'minai.core.MetricsCB.after_batch': ('core.html#metricscb.after_batch', 'minai/core.py'),
                            'minai.core.MetricsCB.after_epoch': ('core.html#metricscb.after_epoch', 'minai/core.py'),
                            'minai.core.MetricsCB.before_epoch': ('core.html#metricscb.before_epoch', 'minai/core.py'),
                            'minai.core.MetricsCB.before_fit': ('core.html#metricscb.before_fit', 'minai/core.py'),
                            'minai.core.MixedPrecision': ('core.html#mixedprecision', 'minai/core.py'),
                            'minai.core.MixedPrecision.__init__': ('core.html#mixedprecision.__init__', 'minai/core.py'),
                            'minai.core.MixedPrecision.after_loss': ('core.html#mixedprecision.after_loss', 'minai/core.py'),
                            'minai.core.MixedPrecision.backward': ('core.html#mixedprecision.backward', 'minai/core.py'),
                            'minai.core.MixedPrecision.before_batch': ('core.html#mixedprecision.before_batch', 'minai/core.py'),
                            'minai.core.MixedPrecision.before_fit': ('core.html#mixedprecision.before_fit', 'minai/core.py'),
                            'minai.core.MixedPrecision.step': ('core.html#mixedprecision.step', 'minai/core.py'),
                            'minai.core.MomentumLearner': ('core.html#momentumlearner', 'minai/core.py'),
                            'minai.core.MomentumLearner.__init__': ('core.html#momentumlearner.__init__', 'minai/core.py'),
                            'minai.core.MomentumLearner.zero_grad': ('core.html#momentumlearner.zero_grad', 'minai/core.py'),
                            'minai.core.ProgressCB': ('core.html#progresscb', 'minai/core.py'),
                            'minai.core.ProgressCB.__init__': ('core.html#progresscb.__init__', 'minai/core.py'),
                            'minai.core.ProgressCB._log': ('core.html#progresscb._log', 'minai/core.py'),
                            'minai.core.ProgressCB.after_batch': ('core.html#progresscb.after_batch', 'minai/core.py'),
                            'minai.core.ProgressCB.before_epoch': ('core.html#progresscb.before_epoch', 'minai/core.py'),
                            'minai.core.ProgressCB.before_fit': ('core.html#progresscb.before_fit', 'minai/core.py'),
                            'minai.core.RandCopy': ('core.html#randcopy', 'minai/core.py'),
                            'minai.core.RandCopy.__init__': ('core.html#randcopy.__init__', 'minai/core.py'),
                            'minai.core.RandCopy.forward': ('core.html#randcopy.forward', 'minai/core.py'),
                            'minai.core.RandErase': ('core.html#randerase', 'minai/core.py'),
                            'minai.core.RandErase.__init__': ('core.html#randerase.__init__', 'minai/core.py'),
                            'minai.core.RandErase.forward': ('core.html#randerase.forward', 'minai/core.py'),
                            'minai.core.RecorderCB': ('core.html#recordercb', 'minai/core.py'),
                            'minai.core.RecorderCB.__init__': ('core.html#recordercb.__init__', 'minai/core.py'),
                            'minai.core.RecorderCB.after_batch': ('core.html#recordercb.after_batch', 'minai/core.py'),
                            'minai.core.RecorderCB.before_fit': ('core.html#recordercb.before_fit', 'minai/core.py'),
                            'minai.core.RecorderCB.plot': ('core.html#recordercb.plot', 'minai/core.py'),
                            'minai.core.SingleBatchCB': ('core.html#singlebatchcb', 'minai/core.py'),
                            'minai.core.SingleBatchCB.after_batch': ('core.html#singlebatchcb.after_batch', 'minai/core.py'),
                            'minai.core.TfmDataset': ('core.html#tfmdataset', 'minai/core.py'),
                            'minai.core.TfmDataset.__getitem__': ('core.html#tfmdataset.__getitem__', 'minai/core.py'),
                            'minai.core.TfmDataset.__init__': ('core.html#tfmdataset.__init__', 'minai/core.py'),
                            'minai.core.TrainCB': ('core.html#traincb', 'minai/core.py'),
                            'minai.core.TrainCB.__init__': ('core.html#traincb.__init__', 'minai/core.py'),
                            'minai.core.TrainCB.backward': ('core.html#traincb.backward', 'minai/core.py'),
                            'minai.core.TrainCB.get_loss': ('core.html#traincb.get_loss', 'minai/core.py'),
                            'minai.core.TrainCB.predict': ('core.html#traincb.predict', 'minai/core.py'),
                            'minai.core.TrainCB.step': ('core.html#traincb.step', 'minai/core.py'),
                            'minai.core.TrainCB.zero_grad': ('core.html#traincb.zero_grad', 'minai/core.py'),
                            'minai.core.TrainLearner': ('core.html#trainlearner', 'minai/core.py'),
                            'minai.core.TrainLearner.__init__': ('core.html#trainlearner.__init__', 'minai/core.py'),
                            'minai.core.TrainLearner.backward': ('core.html#trainlearner.backward', 'minai/core.py'),
                            'minai.core.TrainLearner.get_loss': ('core.html#trainlearner.get_loss', 'minai/core.py'),
                            'minai.core.TrainLearner.predict': ('core.html#trainlearner.predict', 'minai/core.py'),
                            'minai.core.TrainLearner.step': ('core.html#trainlearner.step', 'minai/core.py'),
                            'minai.core.TrainLearner.zero_grad': ('core.html#trainlearner.zero_grad', 'minai/core.py'),
                            'minai.core._flops': ('core.html#_flops', 'minai/core.py'),
                            'minai.core._get_inp': ('core.html#_get_inp', 'minai/core.py'),
                            'minai.core._get_lbl': ('core.html#_get_lbl', 'minai/core.py'),
                            'minai.core._get_preds': ('core.html#_get_preds', 'minai/core.py'),
                            'minai.core._rand_copy1': ('core.html#_rand_copy1', 'minai/core.py'),
                            'minai.core._rand_erase1': ('core.html#_rand_erase1', 'minai/core.py'),
                            'minai.core.append_stats': ('core.html#append_stats', 'minai/core.py'),
                            'minai.core.capture_preds': ('core.html#capture_preds', 'minai/core.py'),
                            'minai.core.clean_ipython_hist': ('core.html#clean_ipython_hist', 'minai/core.py'),
                            'minai.core.clean_mem': ('core.html#clean_mem', 'minai/core.py'),
                            'minai.core.clean_tb': ('core.html#clean_tb', 'minai/core.py'),
                            'minai.core.collate_device': ('core.html#collate_device', 'minai/core.py'),
                            'minai.core.collate_dict': ('core.html#collate_dict', 'minai/core.py'),
                            'minai.core.get_dls': ('core.html#get_dls', 'minai/core.py'),
                            'minai.core.get_grid': ('core.html#get_grid', 'minai/core.py'),
                            'minai.core.get_hist': ('core.html#get_hist', 'minai/core.py'),
                            'minai.core.get_min': ('core.html#get_min', 'minai/core.py'),
                            'minai.core.lr_find': ('core.html#lr_find', 'minai/core.py'),
                            'minai.core.rand_copy': ('core.html#rand_copy', 'minai/core.py'),
                            'minai.core.rand_erase': ('core.html#rand_erase', 'minai/core.py'),
                            'minai.core.run_cbs': ('core.html#run_cbs', 'minai/core.py'),
                            'minai.core.set_seed': ('core.html#set_seed', 'minai/core.py'),
                            'minai.core.show_image_batch': ('core.html#show_image_batch', 'minai/core.py'),
                            'minai.core.show_images': ('core.html#show_images', 'minai/core.py'),
                            'minai.core.subplots': ('core.html#subplots', 'minai/core.py'),
                            'minai.core.summary': ('core.html#summary', 'minai/core.py'),
                            'minai.core.to_cpu': ('core.html#to_cpu', 'minai/core.py'),
                            'minai.core.to_device': ('core.html#to_device', 'minai/core.py'),
                            'minai.core.with_cbs': ('core.html#with_cbs', 'minai/core.py'),
                            'minai.core.with_cbs.__call__': ('core.html#with_cbs.__call__', 'minai/core.py'),
                            'minai.core.with_cbs.__init__': ('core.html#with_cbs.__init__', 'minai/core.py')},
            'minai.version': {}}}
