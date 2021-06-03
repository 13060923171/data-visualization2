import pandas as pd
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts

df = pd.read_csv('./csv_file/当前天气信息.csv',encoding='gbk').loc[:,['1','2']]
df.dropna(axis=0,how='any',inplace=True)
df[df.isnull().T.any()]

list_1 = []
for i in df['1']:
    i = str(i)
    i = i.replace("：","").strip(" ")
    list_1.append(i)

list_2 = []
for i in df['2']:
    i = str(i)
    list_2.append(i)
table = Table()
headers = ["名称", "数值"]
rows =[]
for i in range(len(list_1)):
    list_3 = [list_1[i],list_2[i]]
    rows.append(list_3)

table.add(headers, rows)
table.set_global_opts(
    title_opts=ComponentTitleOpts(title="当前天气的信息")
)
table.render("table_base.html")