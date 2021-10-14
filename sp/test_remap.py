_base_='../swin/mask_rcnn_swin-t-p4-w7_fpn_1x_coco.py'
dataset_type='CocoDataset'
prefix='../coco-annotator/datasets/test/'
classes=('plasticbottle','alu can','box')
# classes=('',)
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=3),
        mask_head=dict(num_classes=3)))

# train_pipeline = [
#     dict(type='LoadImageFromFile'),
#     dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
#     dict(type='Resize', img_scale=(128,128), keep_ratio=True),
#     dict(type='RandomFlip', flip_ratio=0.5),
#     dict(type='Normalize', **img_norm_cfg),
#     dict(type='Pad', size_divisor=32),
#     dict(type='DefaultFormatBundle'),
#     dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks']),
# # ]
# train1=dict(
#         type=dataset_type,
#         classes=classes,
#         ann_file=['data/own/test-1.json'],
#         img_prefix=prefix,
#         pipeline=train_pipeline
#     )
# train2=dict(
#         type=dataset_type,
#         classes=classes,
#         ann_file=['data/own/ann_map_to_1.json'],
#         img_prefix=prefix,
#         pipeline=train_pipeline
#     )
data=dict(
    train=dict(
        type=dataset_type,
        classes=classes,
        ann_file=['data/own/test-1.json','data/own/ann_map_to_1.json'],
        img_prefix=prefix
    ),
    # train=[train1,train2],
    val=dict(
        type=dataset_type,
        classes=classes,
        ann_file='data/own/ann_map_to_1.json',
        img_prefix=prefix
    ),

    test=dict(
        type=dataset_type,
        classes=classes,
        ann_file='data/own/ann_map_to_1.json',
        img_prefix=prefix
    )
)