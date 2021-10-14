_base_='../swin/mask_rcnn_swin-t-p4-w7_fpn_1x_coco.py'


classes=('Aersol','Aluminium foil', 'Battery', 'Aluminium blister pack',
         'Carded blister pack', 'Clear plastic bottle', 'Glass bottle',
         'Other plastic bottle', 'Plastic bottle cap', 'Metal bottle cap',
         'Broken glass', 'Drink can', 'Food Can', 'Corrugated carton',
         'Drink carton', 'Egg carton', 'Meal carton', 'Other carton', 'Paper cup',
         'Disposable plastic cup', 'Foam cup', 'Glass cup', 'Other plastic cup',
         'Food waste', 'Plastic lid', 'Metal lid', 'Magazine paper', 'Tissues',
         'Wrapping paper', 'Normal paper', 'Paper bag', 'Plastified paper bag',
         'Pizza box', 'Garbage bag', 'Single-use carrier bag', 'Polypropylene bag',
         'Produce bag', 'Cereal bag', 'Bread bag', 'Plastic film', 'Crisp packet',
         'Other plastic wrapper', 'Retort pouch', 'Spread tub', 'Tupperware',
         'Disposable food container', 'Foam food container', 'Other plastic container',
         'Plastic glooves', 'Plastic utensils', 'Pop tab', 'Rope & strings',
         'Scrap metal', 'Shoe', 'Six pack rings', 'Squeezable tube', 'Plastic straw',
         'Paper straw', 'Styrofoam piece', 'Toilet tube', 'Unlabeled litter',
         'Glass jar', 'Other plastic', 'Cigarette')

model = dict(
    roi_head=dict(
        bbox_head=[
            dict(
                type='Shared2FCBBoxHead',
                # explicitly over-write all the `num_classes` field from default 80 to 5.
                num_classes=64),
            dict(
                type='Shared2FCBBoxHead',
                # explicitly over-write all the `num_classes` field from default 80 to 5.
                num_classes=64),
            dict(
                type='Shared2FCBBoxHead',
                # explicitly over-write all the `num_classes` field from default 80 to 5.
                num_classes=64)],
    # explicitly over-write all the `num_classes` field from default 80 to 5.
    mask_head=dict(num_classes=64)))
data=dict(
    train=dict(
        classes=classes,
        ann_file='data/coco/annotations/45train.json',
        img_prefix= 'data/coco/val2017/'
    ),
    val=dict(
        classes=classes,
        ann_file='data/coco/annotations/05train.json',
        img_prefix='data/coco/val2017/'
    ),
    test=dict(
        classes=classes,
        ann_file='data/coco/annotations/05train.json',
        img_prefix='data/coco/val2017/'
    )
)
#load_from='../../checkpoints/mask_rcnn_swin-t-p4-w7_fpn_1x_coco_20210902_120937-9d6b7cfa.pth'