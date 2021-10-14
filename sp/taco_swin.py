_base_='../swin/mask_rcnn_swin-t-p4-w7_fpn_1x_coco.py'
dataset_type='CocoDataset'

classes=('Aluminium foil', 'Battery', 'Aluminium blister pack',
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
         'Glass jar','Cigarette')

# model = dict(
#     roi_head=dict(
#         bbox_head=[
#             dict(
#                 # type='Shared2FCBBoxHead',
#                 # explicitly over-write all the `num_classes` field from default 80 to 5.
#                 num_classes=64),
#             dict(
#                 # type='Shared2FCBBoxHead',
#                 # explicitly over-write all the `num_classes` field from default 80 to 5.
#                 num_classes=64),
#             dict(
#                 # type='Shared2FCBBoxHead',
#                 # explicitly over-write all the `num_classes` field from default 80 to 5.
#                 num_classes=64)],
#     # explicitly over-write all the `num_classes` field from default 80 to 5.
#     mask_head=dict(num_classes=64)))
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=62),
        mask_head=dict(num_classes=62)))
data=dict(
    train=dict(
        type=dataset_type,
        classes=classes,
        ann_file='data/taco/taco15train.json',
        img_prefix='data/taco/'
    ),

    val=dict(
        type=dataset_type,
        classes=classes,
        ann_file='data/taco/taco15train.json',
        img_prefix='data/taco/'
    ),

    test=dict(
        type=dataset_type,
        classes=classes,
        ann_file='data/taco/taco15train.json',
        img_prefix='data/taco/'
    )
)