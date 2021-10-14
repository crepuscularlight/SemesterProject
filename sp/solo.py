_base_='../solo/solo_r50_fpn_1x_coco.py'

dataset_type='CocoDataset'
prefix='../coco-annotator/datasets/test/'
classes=('plasticbottle','alu can','box')
model = dict(
    mask_head=dict(num_classes=3))

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