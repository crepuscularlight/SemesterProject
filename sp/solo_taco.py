_base_='../solo/solo_r50_fpn_1x_coco.py'

dataset_type='CocoDataset'
prefix='./data/taco/'

classes=('Aluminium foil', 'Can', 'Carton', 'Cup', 'Glass bottle', 'Metal bottle cap', 'Other', 'Paper', 'Plastic bottle', 'Plastic bottle cap', 'Plastic container', 'Plastic film', 'Plastic lid', 'Pop tab', 'Straw', 'Styrofoam piece', 'Wrapper')

model = dict(
    mask_head=dict(num_classes=17))

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

