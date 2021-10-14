_base_='../swin/mask_rcnn_swin-t-p4-w7_fpn_1x_coco.py'
dataset_type='CocoDataset'
# prefix='../coco-annotator/datasets/test/'
prefix='./data/taco/'
classes=('Aluminium foil', 'Can', 'Carton', 'Cup', 'Glass bottle', 'Metal bottle cap', 'Other', 'Paper', 'Plastic bottle', 'Plastic bottle cap', 'Plastic container', 'Plastic film', 'Plastic lid', 'Pop tab', 'Straw', 'Styrofoam piece', 'Wrapper')


# classes=('',)
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=17),
        mask_head=dict(num_classes=17)))

data=dict(
    train=dict(
        type=dataset_type,
        classes=classes,
        ann_file=['data/own/ann_0_ann_05train.json',
                  # 'data/own/ann_1_ann_05train.json',
                  # 'data/own/ann_2_ann_05train.json',
                  # 'data/own/ann_3_ann_05train.json',
                  # 'data/own/ann_4_ann_05train.json',
                  ],
        img_prefix=prefix
    ),

    val=dict(
        type=dataset_type,
        classes=classes,
        ann_file=['data/own/ann_0_ann_05val.json',
                  # 'data/own/ann_1_ann_05val.json',
                  # 'data/own/ann_2_ann_05val.json',
                  # 'data/own/ann_3_ann_05val.json',
                  # 'data/own/ann_4_ann_05val.json',
                  ],
        img_prefix=prefix
    ),

    test=dict(
        type=dataset_type,
        classes=classes,
        ann_file=['data/own/ann_0_ann_05test.json',
                  # 'data/own/ann_1_ann_05test.json',
                  # 'data/own/ann_2_ann_05test.json',
                  # 'data/own/ann_3_ann_05test.json',
                  # 'data/own/ann_4_ann_05test.json',
                  ],
        img_prefix=prefix
    )
)

# load_from='../../checkpoints/swin_tiny_patch4_window7_224.pth'
