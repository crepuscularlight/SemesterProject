_base_='../cascade_rcnn/cascade_mask_rcnn_r50_fpn_1x_coco.py'

dataset_type='CocoDataset'
prefix='../coco-annotator/datasets/test/'
classes=('plasticbottle','alu can','box')
# model = dict(
#     roi_head=dict(
#         bbox_head=dict(num_classes=3),
#         mask_head=dict(num_classes=3)))
model = dict(
    roi_head=dict(
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