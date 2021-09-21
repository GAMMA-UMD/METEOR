# Set the path to the base config file
_base_ = 'mmaction2/configs/recognition/tsn/tsn_r101_1x1x5_50e_mmit_rgb.py'

model = dict(
    cls_head=dict(
    num_classes=5))

# dataset settings
dataset_type = 'RawframeDataset'
data_root = ''
data_root_val = ''
# Set the path to the train_annotations file
ann_file_train = 'Annotations/train_annotations.txt'
# Set the path to the val_annotations file
ann_file_val = 'Annotations/val_annotations.txt'
# Set the path to the test_annotations file
ann_file_test = 'Annotations/test_annotations.txt'

data = dict(
    train=dict(
        type='RawframeDataset',
        ann_file=ann_file_train,
        data_prefix='',
        num_classes=5),
    val=dict(
        type='RawframeDataset',
        ann_file=ann_file_val,
        data_prefix='',
        num_classes=5),
    test=dict(
        type='RawframeDataset',
        ann_file=ann_file_test,
        data_prefix='',
        num_classes=5))

total_epochs = 100

log_config = dict(interval=5, hooks=[dict(type='TextLoggerHook')])
evaluation = dict(interval=1, metrics=['mmit_mean_average_precision'])

# Set the path to the pre-trained model to obtain higher performance
load_from = 'tsn_r101_1x1x5_50e_mmit_rgb_20200618-642f450d.pth'
