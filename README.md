# PlantSeg: A Large-Scale In-the-wild Dataset for Plant Disease Segmentation
![Alt text](image/seg_samples.png "PlantSeg-logo")


The paper has been submitted to **Scientific Data**. 


## Introduction
We curate an in-the-wild multimodal plant disease recognition dataset PlantWild with the largest number of disease classes. We introduce descriptive prompts in our dataset to provide rich information in textual modality. In addition, we propose a strong yet versatile baseline, which models text descriptions and visual data through multiple prototypes and can achieve outstanding performance on in-the-wild plant disease images.

### Curation of our dataset
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


