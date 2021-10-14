_base_=['../yolox/yolox_s_8x8_300e_coco.py']
dataset_type='CocoDataset'
prefix='../coco-annotator/datasets/test/'
classes=('plasticbottle','alu can','box')
model = dict(
        bbox_head=dict(num_classes=3))

train_dataset=dict(
    dataset=dict(
        type=dataset_type,
        classes=classes,
        ann_file='data/own/test-1.json',
        img_prefix=prefix
    )
)
data=dict(
    train=train_dataset,
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