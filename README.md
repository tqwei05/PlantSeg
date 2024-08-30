# PlantSeg: A Large-Scale In-the-wild Dataset for Plant Disease Segmentation
![Alt text](image/seg_samples.png "PlantSeg-logo")


The paper has been submitted to **Scientific Data**. 


## Abstract
Plant diseases pose significant threats to agriculture. Proper diagnosis and treatment are crucial for protecting crop yield. Segmentation of plant disease images is an important task, as it helps when accurately locating the diseased parts and providing detailed visual information. Traditionally, segmentation tasks require plant pathologists, but such experts are not always available. As an alternative, deep learning methods can be employed to address this need. However, the development of deep learning-based segmentation algorithms has been obstructed due to the lack of useful data. Segmentation labels are rarely provided in existing datasets. Moreover, most datasets consist of images collected in laboratory environments and do not reflect real-world conditions. Motivated by this fact, we established a large-scale plant disease segmentation dataset named PlantSeg. PlantSeg comprises more than 11,400 images of 115 different plant diseases from various environments, each annotated with its corresponding segmentation label for diseased parts. To the best of our knowledge, PlantSeg is the largest plant disease segmentation dataset containing in-the-wild images. Our dataset enables researchers to evaluate their image classification methods and provides a valid foundation for the development and benchmarking of plant disease segmentation algorithms.

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
Our dataset is accessible through [Zenodo](https://zenodo.org/records/13293891).


### 3. Environment setting
Follow [MMSegmentation](https://github.com/open-mmlab/mmsegmentation/blob/main/docs/en/get_started.md#installation) to build the environment.





## Running
```python
python tools/train.py  <CONFIG_DIR> --work-dir <WORK_DIR>
```


##  Baseline Results



Method               | Encoder | IOU | F1 
---                  | ---  | ---   | ---                  
DeepLabV3  |   ResNet50  |   |  
DeepLabV3  |   ResNet101  |   |  
DeepLabV3+  |   ResNet50  |   |  
DeepLabV3+  |   ResNet101  |   |  
SAN  |   ViT-B/16  |   |  
SAN  |   ViT-L/14  |   |  
Segformer |     |   |  
SegNext   |     |   |  


## Results





## Acknowledgments

Our code is based on [MMSegmentation](https://github.com/open-mmlab/mmsegmentation). We appreciate their wonderful work.


