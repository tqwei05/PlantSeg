_base_ = './deeplabv3plus_r50-160k_docseg_binary-128x128.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))