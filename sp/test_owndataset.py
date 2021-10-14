_base_='../swin/mask_rcnn_swin-t-p4-w7_fpn_1x_coco.py'
dataset_type='CocoDataset'
prefix='../coco-annotator/datasets/test/'
classes=('plasticbottle','alu can','box')
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=3),
        mask_head=dict(num_classes=3)))

data=dict(
    train=dict(
        type=dataset_type,
        classes=classes,
        ann_file='data/own/test-1.json',
        img_prefix=prefix
    ),

    val=dict(
        type=dataset_type,
        classes=classes,
        ann_file='data/own/test-1.json',
        img_prefix=prefix
    ),

    test=dict(
        type=dataset_type,
        classes=classes,
        ann_file='data/own/test-1.json',
        img_prefix=prefix
    )
)