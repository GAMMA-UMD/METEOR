# METEOR
This repository contains the official code for the paper: **METEOR: A Massive Dense & Heterogeneous Behavior Dataset for Autonomous Driving**.

*Rohan Chandra, Xijun Wang, Mridul Mahajan, Rahul Kala, Rishitha Palugulla, Chandrababu Naidu, Alok Jain, and Dinesh Manocha*

ICRA 2023 | [Preprint]([https://arxiv.org/abs/2109.07648) | [Project Page](https://gamma.umd.edu/meteor/)

<img src="https://github.com/MridulMahajan44/METEOR/blob/main/gifs/github_gif.gif"/> <img src="https://github.com/MridulMahajan44/METEOR/blob/main/gifs/WL.gif"/>



## Pre-requisites

This repository is based on [MMDetection](https://mmdetection.readthedocs.io/en/latest/get_started.html) and [MMAction2](https://mmaction2.readthedocs.io/en/latest/getting_started.html). 

## Download the Dataset
Download the dataset [**here**](https://umd.app.box.com/s/rys1c4d3dhtge775t6hm9uualkx7yn4q).

## Dataset Preparation

1. Run the following command to extract frames from the videos:

   ```bash
   python videos2frames.py --videos_directory /path/to/videos_dir --output_directory /path/to/output_dir
   ```

2. Run the following command to reorganize the dataset into COCO format for object detection:

   ```bash
   python xml2coco.py --dataset_directory /path/to/dataset_dir --output_directory /path/to/output_dir
   ```

3. Run the following command to reorganize the dataset into rawframe annotation format for behavior prediction:

   ```bash
   python xml2rawframe.py --dataset_directory /path/to/dataset_dir --output_directory /path/to/output_dir
   ```

## Config Preparation

1. Download the pre-trained DETR model from [link](https://download.openmmlab.com/mmdetection/v2.0/detr/detr_r50_8x2_150e_coco/detr_r50_8x2_150e_coco_20201130_194835-2c4b8974.pth).

2. Download the pre-trained TSN model from [link](https://download.openmmlab.com/mmaction/recognition/tsn/tsn_r101_1x1x5_50e_mmit_rgb/tsn_r101_1x1x5_50e_mmit_rgb_20200618-642f450d.pth).

3. Update the paths to the base config file, train annotations file, the test annotations file, and the pre-trained model in `detr_config.py` and `tsn_config.py`. 

## Training

1. Run the following command to initiate the training process for DETR:
    
   ```bash
   python mmdetection/tools/train.py detr_config.py
   ```

2. Run the following command to initiate the training process for TSN:
    
   ```bash
   python mmaction2/tools/train.py tsn_config.py
   ```
   
## Pre-trained Models

* [Object Detection](https://drive.google.com/file/d/17NMvTJZiRrLfSRWwjJd4zx4ELQ9_9uWq/view?usp=sharing)

* [Behavior Prediction](https://drive.google.com/file/d/1DPeiTTLZKoOboCTW-kaDDAl0UhNBCtZa/view?usp=sharing)

## Testing

1. Run the following command to initiate the testing process for DETR:
    
   ```bash
   python mmdetection/tools/test.py detr_config.py detr_pretrained.pth --eval bbox mAP recall
   ```

2. Run the following command to initiate the testing process for TSN:
    
   ```bash
   python mmaction2/tools/test.py tsn_config.py tsn_pretrained.pth --eval mmit_mean_average_precision
   ```
   
## Swin Detection (Scripts/Swin-Transformer-Object-Detection)
 
1. Installation (https://github.com/open-mmlab/mmdetection/blob/master/docs/en/get_started.md)

2. DATA ([Json file](https://drive.google.com/drive/folders/1BV2EUYH0G2rAIRrOwJaeWPkehaqEtuzg?usp=sharing)): 
 Change the frame path in json file to your own path:
 e.g. "file_name": "/scratch0/xijunwang/data/METEOR_Dataset/Frame_XML_Annotations/REC_2020_10_12_01_26_57_F/frame_000000.JPG" -> "file_name": "/xxx/REC_2020_10_12_01_26_57_F/frame_000000.JPG"

3. Train:
   ```bash
   tools/dist_train.sh configs/swin/mask_rcnn_swin_tiny_patch4_window7_mstrain_480-800_adamw_1x_metor.py 8 --cfg-options model.pretrained=<PRETRAIN_MODEL>
   ```
   
4. Reference 
   * [Swin-Transformer-Object-Detection](https://github.com/SwinTransformer/Swin-Transformer-Object-Detection)
   
   
 





 
 
