import pandas as pd
import json
df = pd.read_excel('eqdata.xls').loc[:,['震级','经度','纬度','地点']]
list_key = []
list_value = []



with open('city.json','a+',encoding='utf-8') as f:
    d = {}
    for i in range(len(df['地点'])):
        # list_key.append(df['地点'][i])
        # list_value.append([(df['经度'][i]),df['纬度'][i]])
        d[df['地点'][i]] = [(df['纬度'][i]), df['经度'][i]]
    f.write(json.dumps(d,ensure_ascii=False)+"\n")


