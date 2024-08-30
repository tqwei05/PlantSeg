# PlantSeg: A Large-Scale In-the-wild Dataset for Plant Disease Segmentation
![Alt text](image/seg_samples.png "PlantSeg-logo")


The paper has been submitted to **Scientific Data**. 


## Abstract
Plant diseases pose significant threats to agriculture. Proper diagnosis and treatment are crucial for protecting crop yield. Segmentation of plant disease images is an important task, as it helps when accurately locating the diseased parts and providing detailed visual information. Traditionally, segmentation tasks require plant pathologists, but such experts are not always available. As an alternative, deep learning methods can be employed to address this need. However, the development of deep learning-based segmentation algorithms has been obstructed due to the lack of useful data. Segmentation labels are rarely provided in existing datasets. Moreover, most datasets consist of images collected in laboratory environments and do not reflect real-world conditions. Motivated by this fact, we established a large-scale plant disease segmentation dataset named PlantSeg. PlantSeg comprises more than 11,400 images of 115 different plant diseases from various environments, each annotated with its corresponding segmentation label for diseased parts. To the best of our knowledge, PlantSeg is the largest plant disease segmentation dataset containing in-the-wild images. Our dataset enables researchers to evaluate their image classification methods and provides a valid foundation for the development and benchmarking of plant disease segmentation algorithms.

## Curation of our dataset
<div align="center">
  <img width=800 src="image/workflow7.png"/>
</div>





## Preparation
### 1. Clone the repo
```bash
git clone https://github.com/tqwei05/PlantSeg.git
cd PlantSeg
```
### 2. Requirements
```bash
conda create -n mvpdr python=3.8
conda activate mvpdr
pip install -r requirements.txt
# Install the according versions of torch and torchvision
conda install pytorch torchvision cudatoolkit
```

### 3. Prepare the data
Our dataset is accessible through [Zenodo](https://zenodo.org/records/13293891).



## Running
We provide the code for training and evaluation in main.py.
```python
python main.py --config <CONFIG_DIR>
```


##  Baseline Results



Method               | Encoder | IOU | F1 
---                  | ---  | ---   | ---                  
Unet       |   ResNet34  | 89.7  |  94.5
DeepLabV3  |   ResNet34  | 89.5  |  94.5


## Results





## Acknowledgments

Our code benefits from [Tip-Adapter](https://github.com/gaopengcuhk/Tip-Adapter). We appreciate their wonderful works.


