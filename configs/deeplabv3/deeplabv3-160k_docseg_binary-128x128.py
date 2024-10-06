_base_ = [
    '../_base_/models/deeplabv3_r50-d8.py', '../_base_/datasets/docseg_binary.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
crop_size = (512, 512)
data_preprocessor = dict(size=crop_size)
model = dict(
    data_preprocessor=data_preprocessor,
    test_cfg=dict(crop_size=(512, 512), stride=(85, 85)))
