_base_='../htc/htc_r50_fpn_1x_coco.py'
dataset_type='CocoDataset'
prefix='../coco-annotator/datasets/test/'
classes=('plasticbottle','alu can','box')
model = dict(
    roi_head=dict(

    ))
model = dict(
    roi_head=dict(
        semantic_head=dict(
            num_classes=3
        ),
        bbox_head=[
            dict(
                type='Shared2FCBBoxHead',
                # explicitly over-write all the `num_classes` field from default 80 to 5.
                num_classes=3),
            dict(
                type='Shared2FCBBoxHead',
                # explicitly over-write all the `num_classes` field from default 80 to 5.
                num_classes=3),
            dict(
                type='Shared2FCBBoxHead',
#                 # explicitly over-write all the `num_classes` field from default 80 to 5.
                num_classes=3)],
#     # explicitly over-write all the `num_classes` field from default 80 to 5.
    mask_head=[dict(type='HTCMaskHead',num_classes=3),
               dict(type='HTCMaskHead',num_classes=3),
               dict(type='HTCMaskHead',num_classes=3)]))
data=dict(
    train=dict(
        type=dataset_type,
        classes=classes,
        ann_file='data/own/test-1.json',
        img_prefix=prefix,
        seg_prefix='data/coco/stuffthingmaps/val2017/'#json file does not accord with the seg test
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