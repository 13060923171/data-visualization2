import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Boxplot
from pyecharts.globals import ThemeType

df = pd.read_excel('各区房价平均值.xlsx',sheet_name='Sheet1').loc[:,['宝山','崇明','奉贤','虹口','黄浦','嘉定','金山','静安+闸北','闵行','浦东','普陀','青浦','松江','徐汇','杨浦','长宁']]


x_data = ['宝山','崇明','奉贤','虹口','黄浦','嘉定','金山','静安+闸北','闵行','浦东','普陀','青浦','松江','徐汇','杨浦','长宁']


list_1 = []
for i in df['宝山']:
    if np.isnan(i) == False:
        list_1.append(int(i))

list_2 = []
for i in df['崇明']:
    if np.isnan(i) == False:
        list_2.append(int(i))

list_3 = []
for i in df['奉贤']:
    if np.isnan(i) == False:
        list_3.append(int(i))

list_4 = []
for i in df['虹口']:
    if np.isnan(i) == False:
        list_4.append(int(i))

list_5 = []
for i in df['黄浦']:
    if np.isnan(i) == False:
        list_5.append(int(i))

list_6 = []
for i in df['嘉定']:
    if np.isnan(i) == False:
        list_6.append(int(i))

list_7 = []
for i in df['金山']:
    if np.isnan(i) == False:
        list_7.append(int(i))

list_8 = []
for i in df['静安+闸北']:
    if np.isnan(i) == False:
        list_8.append(int(i))

list_9 = []
for i in df['闵行']:
    if np.isnan(i) == False:
        list_9.append(int(i))

list_10 = []
for i in df['浦东']:
    if np.isnan(i) == False:
        list_10.append(int(i))

list_11 = []
for i in df['普陀']:
    if np.isnan(i) == False:
        list_11.append(int(i))


list_12 = []
for i in df['青浦']:
    if np.isnan(i) == False:
        list_12.append(int(i))

list_13 = []
for i in df['松江']:
    if np.isnan(i) == False:
        list_13.append(int(i))

list_14 = []
for i in df['徐汇']:
    if np.isnan(i) == False:
        list_14.append(int(i))

list_15 = []
for i in df['杨浦']:
    if np.isnan(i) == False:
        list_15.append(int(i))

list_16 = []
for i in df['长宁']:
    if np.isnan(i) == False:
        list_16.append(int(i))

y_data = []
y_data.append(list_1)
y_data.append(list_2)
y_data.append(list_3)
y_data.append(list_4)
y_data.append(list_5)
y_data.append(list_6)
y_data.append(list_7)
y_data.append(list_8)
y_data.append(list_9)
y_data.append(list_10)
y_data.append(list_11)
y_data.append(list_12)
y_data.append(list_13)
y_data.append(list_14)
y_data.append(list_15)
y_data.append(list_16)


def main_boxplot():
    c = Boxplot(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
    c.add_xaxis(x_data)
    c.add_yaxis("", c.prepare_data(y_data))
    c.set_global_opts(title_opts=opts.TitleOpts(title="上海各区-箱线图"))
    return c