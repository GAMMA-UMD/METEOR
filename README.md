# METEOR
This repository contains the official code for the paper: **METEOR: A Massive Dense & Heterogeneous Behavior Dataset for Autonomous Driving**.

*Rohan Chandra, Mridul Mahajan, Rahul Kala, Rishitha Palugulla, Chandrababu Naidu, Alok Jain, and Dinesh Manocha*

Under Review at ICRA 2022 | [Preprint](https://arxiv.org/pdf/2109.07648v1.pdf) | [Project Page](https://gamma.umd.edu/meteor/)

<img src="https://github.com/MridulMahajan44/METEOR/blob/main/gifs/github_gif.gif"/> <img src="https://github.com/MridulMahajan44/METEOR/blob/main/gifs/WL.gif"/>



## Pre-requisites

This repository is based on [MMDetection](https://mmdetection.readthedocs.io/en/latest/get_started.html) and [MMAction2](https://mmaction2.readthedocs.io/en/latest/getting_started.html). 

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

## Inference

TODO
