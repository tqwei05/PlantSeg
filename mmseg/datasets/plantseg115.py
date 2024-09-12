# Copyright (c) OpenMMLab. All rights reserved.
from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class PlantSeg115Dataset(BaseSegDataset):
    """COCO-Stuff dataset.

    In segmentation map annotation for COCO-Stuff, Train-IDs of the 10k version
    are from 1 to 171, where 0 is the ignore index, and Train-ID of COCO Stuff
    164k is from 0 to 170, where 255 is the ignore index. So, they are all 171
    semantic categories. ``reduce_zero_label`` is set to True and False for the
    10k and 164k versions, respectively. The ``img_suffix`` is fixed to '.jpg',
    and ``seg_map_suffix`` is fixed to '.png'.
    """
    METAINFO = dict(
        classes=('', 'apple black rot', 'apple mosaic virus', 'apple rust', 'apple scab', 'banana anthracnose',
                 'banana black leaf streak', 'banana bunchy top', 'banana cigar end rot', 'banana cordana leaf spot',
                 'banana panama disease', 'basil downy mildew', 'bean halo blight', 'bean mosaic virus', 'bean rust',
                 'bell pepper bacterial spot', 'bell pepper blossom end rot', 'bell pepper frogeye leaf spot',
                 'bell pepper powdery mildew', 'blueberry anthracnose', 'blueberry botrytis blight',
                 'blueberry mummy berry', 'blueberry rust', 'blueberry scorch', 'broccoli alternaria leaf spot',
                 'broccoli downy mildew', 'broccoli ring spot', 'cabbage alternaria leaf spot', 'cabbage black rot',
                 'cabbage downy mildew', 'carrot alternaria leaf blight', 'carrot cavity spot',
                 'carrot cercospora leaf blight', 'cauliflower alternaria leaf spot', 'cauliflower bacterial soft rot',
                 'celery anthracnose', 'celery early blight', 'cherry leaf spot', 'cherry powdery mildew',
                 'citrus canker', 'citrus greening disease', 'coffee berry blotch', 'coffee black rot',
                 'coffee brown eye spot', 'coffee leaf rust', 'corn gray leaf spot', 'corn northern leaf blight',
                 'corn rust', 'corn smut', 'cucumber angular leaf spot', 'cucumber bacterial wilt',
                 'cucumber powdery mildew', 'eggplant cercospora leaf spot', 'eggplant phomopsis fruit rot',
                 'eggplant phytophthora blight', 'garlic leaf blight', 'garlic rust', 'ginger leaf spot',
                 'ginger sheath blight', 'grape black rot', 'grape downy mildew', 'grape leaf spot',
                 'grapevine leafroll disease', 'lettuce downy mildew', 'lettuce mosaic virus', 'maple tar spot',
                 'peach anthracnose', 'peach brown rot', 'peach leaf curl', 'peach rust', 'peach scab',
                 'plum bacterial spot', 'plum brown rot', 'plum pocket disease', 'plum pox virus', 'plum rust',
                 'potato early blight', 'potato late blight', 'raspberry fire blight', 'raspberry gray mold',
                 'raspberry leaf spot', 'raspberry yellow rust', 'rice blast', 'rice sheath blight',
                 'soybean bacterial blight', 'soybean brown spot', 'soybean downy mildew', 'soybean frog eye leaf spot',
                 'soybean mosaic', 'soybean rust', 'squash powdery mildew', 'strawberry anthracnose',
                 'strawberry leaf scorch', 'tobacco blue mold', 'tobacco brown spot', 'tobacco frogeye leaf spot',
                 'tobacco mosaic virus', 'tomato bacterial leaf spot', 'tomato early blight', 'tomato late blight',
                 'tomato leaf mold', 'tomato mosaic virus', 'tomato septoria leaf spot',
                 'tomato yellow leaf curl virus', 'wheat bacterial leaf streak (black chaff)', 'wheat head scab',
                 'wheat leaf rust', 'wheat loose smut', 'wheat powdery mildew', 'wheat septoria blotch',
                 'wheat stem rust', 'wheat stripe rust', 'zucchini bacterial wilt', 'zucchini downy mildew',
                 'zucchini powdery mildew', 'zucchini yellow mosaic virus'),

        palette=[[120, 120, 120], [0, 192, 64], [0, 192, 64], [0, 64, 96], [128, 192, 192],
                 [0, 64, 64], [0, 192, 224], [0, 192, 192], [128, 192, 64],
                 [0, 192, 96], [128, 192, 64], [128, 32, 192], [0, 0, 224],
                 [0, 0, 64], [0, 160, 192], [128, 0, 96], [128, 0, 192],
                 [0, 32, 192], [128, 128, 224], [0, 0, 192], [128, 160, 192],
                 [128, 128, 0], [128, 0, 32], [128, 32, 0], [128, 0, 128],
                 [64, 128, 32], [0, 160, 0], [0, 0, 0], [192, 128, 160],
                 [0, 32, 0], [0, 128, 128], [64, 128, 160], [128, 160, 0],
                 [0, 128, 0], [192, 128, 32], [128, 96, 128], [0, 0, 128],
                 [64, 0, 32], [0, 224, 128], [128, 0, 0], [192, 0, 160],
                 [0, 96, 128], [128, 128, 128], [64, 0, 160], [128, 224, 128],
                 [128, 128, 64], [192, 0, 32], [128, 96, 0], [128, 0, 192],
                 [0, 128, 32], [64, 224, 0], [0, 0, 64], [128, 128, 160],
                 [64, 96, 0], [0, 128, 192], [0, 128, 160], [192, 224, 0],
                 [0, 128, 64], [128, 128, 32], [192, 32, 128], [0, 64, 192],
                 [0, 0, 32], [64, 160, 128], [128, 64, 64], [128, 0, 160],
                 [64, 32, 128], [128, 192, 192], [0, 0, 160], [255, 192, 203],
                 [128, 192, 0], [128, 0, 96], [192, 32, 0], [128, 64, 128],
                 [64, 128, 96], [64, 160, 0], [0, 64, 0], [192, 128, 224],
                 [64, 32, 0], [0, 192, 128], [64, 128, 224], [192, 160, 0],
                 [0, 192, 0], [192, 128, 96], [192, 96, 128], [0, 64, 128],
                 [64, 0, 96], [64, 224, 128], [128, 64, 0], [192, 0, 224],
                 [64, 96, 128], [128, 192, 128], [64, 0, 224], [192, 224, 128],
                 [128, 192, 64], [192, 0, 96], [192, 96, 0], [128, 64, 192],
                 [0, 128, 96], [0, 224, 0], [64, 64, 64], [128, 128, 224],
                 [0, 96, 0], [64, 192, 192], [0, 128, 224], [128, 224, 0],
                 [64, 192, 64], [128, 128, 96], [128, 32, 128], [64, 0, 192],
                 [0, 64, 96], [0, 160, 128], [192, 0, 64], [128, 64, 224],
                 [0, 32, 128], [192, 128, 192], [0, 64, 224], [128, 160, 128],
                 [192, 128, 0], [128, 64, 32], [128, 32, 64], [192, 0, 128],
                 [64, 192, 32], [0, 160, 64], [64, 0, 0], [192, 192, 160],
                 [0, 32, 64], [64, 128, 128], [64, 192, 160], [128, 160, 64],
                 [64, 128, 0], [192, 192, 32], [128, 96, 192], [64, 0, 128],
                 [64, 64, 32], [0, 224, 192], [192, 0, 0], [192, 64, 160],
                 [0, 96, 192], [192, 128, 128], [64, 64, 160], [128, 224, 192],
                 [192, 128, 64], [192, 64, 32], [128, 96, 64], [192, 0, 192],
                 [0, 192, 32], [64, 224, 64], [64, 0, 64], [128, 192, 160],
                 [64, 96, 64], [64, 128, 192], [0, 192, 160], [192, 224, 64],
                 [64, 128, 64], [128, 192, 32], [192, 32, 192], [64, 64, 192],
                 [0, 64, 32], [64, 160, 192], [192, 64, 64], [128, 64, 160],
                 [64, 32, 192], [192, 192, 192], [0, 64, 160], [192, 160, 192],
                 [192, 192, 0], [128, 64, 96], [192, 32, 64], [192, 64, 128],
                 [64, 192, 96], [64, 160, 64], [64, 64, 0]][:116])

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
