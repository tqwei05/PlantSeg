_base_ = './deeplabv3-160k_plantseg_binary-128x128.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))
