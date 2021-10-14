import pandas as pd
import csv
import json
with open('./ann_0_ann_05val.json','r') as f:
    dataset=json.loads(f.read())

original_class=['plasticbottle','alu can','box']
remap_class=['box','box','box']

# df=pd.DataFrame({'col1':original_class,'col2':remap_class})
# df.to_csv('remap.csv',index=False,header=False)



# print(dataset.keys())
# print(dataset['images'])
result=[]
for item in dataset['categories']:
    result.append(item['name'])
print(result)
# print(dataset['annotations'])