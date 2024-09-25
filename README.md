# PlantSeg: A Large-Scale In-the-wild Dataset for Plant Disease Segmentation
![Alt text](image/seg_samples.png "PlantSeg-logo")





## Introduction
We established a large-scale plant disease segmentation dataset named PlantSeg. PlantSeg comprises more than 11,400 images of 115 different plant diseases from various environments, each annotated with its corresponding segmentation label for diseased parts. To the best of our knowledge, PlantSeg is the largest plant disease segmentation dataset containing in-the-wild images. Our dataset enables researchers to evaluate their models and provides a valid foundation for the development and benchmarking of plant disease segmentation algorithms.

## Curation of our dataset
The curation process of the PlantSeg dataset involves three main steps: image acquisition, data cleaning, and annotation. In the image acquisition stage, images were collected from various internet sources using identified keywords and then stored according to their categories. During the data cleaning phase, incorrect images were identified and removed. For the segmentation annotation process, annotators utilized LabelMe to annotate the cleaned images. These annotations were subsequently reviewed by experts and saved in JSON files.
<div align="center">
  <img width=800 src="image/workflow7.png"/>
</div>





## Preparation
### 1. Clone the repo
```bash
git clone https://github.com/tqwei05/PlantSeg.git
cd PlantSeg
```
### 2. Prepare the data
PlantSeg is accessible through [Zenodo](https://zenodo.org/records/13762907). After downloading, put PlantSeg under the "data" folder.


### 3. Environment setting
Follow [MMSegmentation](https://github.com/open-mmlab/mmsegmentation/blob/main/docs/en/get_started.md#installation) to build the environment.





## Running
```python
sh run.sh
```



##  Baseline Results



Method               | Encoder | IOU | F1 
---                  | ---  | ---   | ---                  
DeepLabV3  |   ResNet50  | 17.24 | 37.95 
DeepLabV3  |   ResNet101  | 20.72 | 40.63 
DeepLabV3+  |   ResNet50  | 25.08  |  40.66
DeepLabV3+  |   ResNet101  | 27.18  | 42.29 
SAN  |   ViT-B/16  |  34.79 |  50.19
SAN  |   ViT-L/14  |  36.91 | 52.81  
SegNext   | MSCAN-L |  44.52  |  59.95 |  

## Paper
[PlantSeg: A Large-Scale In-the-wild Dataset for Plant Disease Segmentation](https://arxiv.org/abs/2409.04038)

## Citation
If you find our work useful, please cite as follows.

```BibTeX
@article{wei2024plantseg,
  title={PlantSeg: A Large-Scale In-the-wild Dataset for Plant Disease Segmentation},
  author={Wei, Tianqi and Chen, Zhi and Yu, Xin and Chapman, Scott and Melloy, Paul and Huang, Zi},
  journal={arXiv preprint arXiv:2409.04038},
  year={2024}
}
```




## Acknowledgments

Our code is based on [MMSegmentation](https://github.com/open-mmlab/mmsegmentation). We appreciate their wonderful work.


