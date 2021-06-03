from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
import pandas as pd
df = pd.read_excel('eqdata.xls').loc[:,['震级','经度','纬度','地点']]

data_x = []
for i in df['地点']:
    data_x.append(i)
data_y = []
for i in df['震级']:
    i = float(i)
    data_y.append(i)
headers = ["地点", "震级"]
data_z = []
for i in range(len(data_x)):
    data_z.append([data_x[i],data_y[i]])
data_z.sort(key=lambda x:x[1],reverse=True)

def table():
    c = (
        Table()
        .add(headers, data_z[0:15])
        .set_global_opts(
                title_opts=ComponentTitleOpts(title="地震数据分析")
        )
    )
    return c
