_base_='../htc/htc_r50_fpn_1x_coco.py'

data=dict(
    train=dict(
        ann_file='data/coco/annotations/instances_val2017.json',
        img_prefix= 'data/coco/val2017/'
    )
)

