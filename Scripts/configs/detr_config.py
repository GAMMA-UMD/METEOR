# Set the path to the base config file
_base_ = 'mmdetection/configs/detr/detr_r50_8x2_150e_coco.py'

model = dict(
    pretrained=None,
    bbox_head=dict(num_classes=15))

dataset_type = 'COCODataset'
classes = ("Car", "MotorBike", "Truck", "MotorizedTricycle", "Scooter", "Tractor", "Pedestrian", "Van", "Bicycle", "Bus", "ConstructionVehicle", "Animal", "AgricultureVehicle", "MultiWheeler", "TriCycle")

data = dict(
    train=dict(
        img_prefix='',
        classes=classes,
        # Set the path to the train_annotations file
        ann_file='Annotations/train_annotations.json'),
    val=dict(
        img_prefix='',
        classes=classes,
        ann_file='Annotations/train_annotations.json'),
    test=dict(
        img_prefix='',
        classes=classes,
        # Set the path to the test_annotations file
        ann_file='Annotations/test_annotations.json'))     
        
runner = dict(type='EpochBasedRunner', max_epochs=5)        

# Set the path to the pre-trained model to obtain higher performance
load_from = 'detr_r50_8x2_150e_coco_20201130_194835-2c4b8974.pth'
