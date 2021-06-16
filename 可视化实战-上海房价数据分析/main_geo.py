import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ThemeType
from pyecharts.globals import ChartType
from pyecharts.globals import ChartType, SymbolType
df = pd.read_csv('shanghai.csv',encoding='gbk').loc[:,['区域','价格（W）']]

x_data = []
y_data = []
sum_y_data = []
for x in df['区域']:
    x = str(x)
    x_data.append(x)

for y in df['价格（W）']:
    y = int(y)
    y_data.append(y)



list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
list_6 = []
list_7 = []
list_8 = []
list_9 = []
list_10 = []
list_11= []
list_12 = []
list_13 = []
list_14 = []
list_15 = []
list_16 = []

for i in range(len(x_data)):
    if x_data[i] == '宝山':
        list_1.append(y_data[i])
    elif x_data[i] == '崇明':
        list_2.append(y_data[i])
    elif x_data[i] == '奉贤':
        list_3.append(y_data[i])
    elif x_data[i] == '虹口':
        list_4.append(y_data[i])
    elif x_data[i] == '黄浦':
        list_5.append(y_data[i])
    elif x_data[i] == '嘉定':
        list_6.append(y_data[i])
    elif x_data[i] == '金山':
        list_7.append(y_data[i])
    elif x_data[i] == '静安':
        list_8.append(y_data[i])
    elif x_data[i] == '闵行':
        list_9.append(y_data[i])
    elif x_data[i] == '浦东':
        list_10.append(y_data[i])
    elif x_data[i] == '普陀':
        list_11.append(y_data[i])
    elif x_data[i] == '青浦':
        list_12.append(y_data[i])
    elif x_data[i] == '松江':
        list_13.append(y_data[i])
    elif x_data[i] == '徐汇':
        list_14.append(y_data[i])
    elif x_data[i] == '杨浦':
        list_15.append(y_data[i])
    elif x_data[i] == '长宁':
        list_16.append(y_data[i])

sum_y_data.append(max(list_1))
sum_y_data.append(max(list_2))
sum_y_data.append(max(list_3))
sum_y_data.append(max(list_4))
sum_y_data.append(max(list_5))
sum_y_data.append(max(list_6))
sum_y_data.append(max(list_7))
sum_y_data.append(max(list_8))
sum_y_data.append(max(list_9))
sum_y_data.append(max(list_10))
sum_y_data.append(max(list_11))
sum_y_data.append(max(list_12))
sum_y_data.append(max(list_13))
sum_y_data.append(max(list_14))
sum_y_data.append(max(list_15))
sum_y_data.append(max(list_16))


x_data1 = ['宝山','崇明','奉贤','虹口','黄浦','嘉定','金山','静安+闸北','闵行','浦东','普陀','青浦','松江','徐汇','杨浦','长宁']
sum_x_data = []
for i in x_data1:
    i = str(i)
    i = '{}区'.format(i)
    i = i.replace('浦东区', '浦东新区').replace('静安+闸北区', '静安区')
    sum_x_data.append(i)


def main_geo():
    c = (
        Geo(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
        .add_coordinate(name="崇明区", longitude=121.60, latitude=31.6)
        .add_coordinate(name="顾唐路地铁站", longitude=121.39, latitude=31.1)
        .add_schema(maptype="上海")
        .add(
            "",
            [list(z) for z in zip(sum_x_data, sum_y_data)],
            type_=ChartType.EFFECT_SCATTER,

        )
            .add(
            "",
            [("顾唐路地铁站", "崇明区"),("顾唐路地铁站", "金山区"),("顾唐路地铁站", "奉贤区"),("顾唐路地铁站", "青浦区"),("顾唐路地铁站", "嘉定区"),("顾唐路地铁站", "松江区"),("顾唐路地铁站", "宝山区"),("顾唐路地铁站", "闵行区"),("顾唐路地铁站", "浦东新区"),("顾唐路地铁站", "杨浦区"),("顾唐路地铁站", "静安区"),("顾唐路地铁站", "虹口区"),("顾唐路地铁站", "长宁区"),("顾唐路地铁站", "徐汇区"),("顾唐路地铁站", "黄浦区")],
            type_=ChartType.LINES,
            effect_opts=opts.EffectOpts(
                symbol=SymbolType.ARROW, symbol_size=6, color="blue"
            ),
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="上海各区-最高房价"))
    )
    return c