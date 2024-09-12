CUDA_VISIBLE_DEVICES=0 python tools/train.py  configs/deeplabv3/deeplabv3_r50-d8_4xb4-40k_plantseg115-512x512.py

CUDA_VISIBLE_DEVICES=0 python tools/train.py  configs/deeplabv3/deeplabv3_r101-d8_4xb4-40k_plantseg115-512x512.py

CUDA_VISIBLE_DEVICES=0 python tools/train.py  configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-40k_plantseg115-512x512.py

CUDA_VISIBLE_DEVICES=0 python tools/train.py  configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-40k_plantseg115-512x512.py

CUDA_VISIBLE_DEVICES=0 python tools/train.py  configs/san/san_b16_plantseg115.py

CUDA_VISIBLE_DEVICES=0 python tools/train.py  configs/san/san_l14_plantseg115.py

CUDA_VISIBLE_DEVICES=0 python tools/train.py  configs/segnext/segnext_mscan-l_1xb16-adamw-40k_plantseg115-512x512.py










