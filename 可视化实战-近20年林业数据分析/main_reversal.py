import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline
sum_y_data = []
df_2001 = pd.read_excel('./data/2000-2001.xlsx').loc[2,['Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29']]
x_data_1 = ['零星四旁植树(万株)','育苗面积','幼林抚育面积','成林抚育面积']
y_data1 = []
for d in df_2001[::2]:
    d = float(d)
    y_data1.append(d)
sum_y_data.append(y_data1)
y_data2 = []
for d in df_2001[1::2]:
    d = float(d)
    y_data2.append(d)
sum_y_data.append(y_data2)

df_2002 = pd.read_excel('./data/2002-2003.xlsx').loc[2,['Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29']]

y_data3 = []
for d in df_2002[::2]:
    d = float(d)
    y_data3.append(d)
sum_y_data.append(y_data3)
y_data4 = []
for d in df_2002[1::2]:
    d = float(d)
    y_data4.append(d)
sum_y_data.append(y_data4)

df_2004 = pd.read_excel('./data/2004-2005.xlsx').loc[2,['Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29']]

y_data5 = []
for d in df_2004[::2]:
    d = float(d)
    y_data5.append(d)
sum_y_data.append(y_data5)
y_data6 = []
for d in df_2004[1::2]:
    d = float(d)
    y_data6.append(d)
sum_y_data.append(y_data6)

df_2006 = pd.read_excel('./data/2006-2007.xlsx').loc[2,['Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29']]

y_data7 = []
for d in df_2006[::2]:
    d = d.split(' ')
    d = d[-1]
    d = d.replace('．','.')
    y_data7.append(float(d))
sum_y_data.append(y_data7)
y_data8 = []
for d in df_2006[1::2]:
    d = d.split(' ')
    d = d[-1]
    d = d.replace('．', '.')
    y_data8.append(float(d))
sum_y_data.append(y_data8)

df_2008 = pd.read_excel('./data/2008-2009.xlsx').loc[2,['Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31']]

y_data9 = []
for d in df_2008[::2]:
    d = d.split(' ')
    d = d[-1]
    d = d.replace('．', '.')
    y_data9.append(d)
sum_y_data.append(y_data9)
y_data10 = []
for d in df_2008[1::2]:
    d = d.split(' ')
    d = d[-1]
    d = d.replace('．', '.')
    y_data10.append(d)
sum_y_data.append(y_data10)

df_2010 = pd.read_excel('./data/2010-2011.xlsx').loc[2,['Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29']]

y_data11 = []
for d in df_2010[::2]:
    d = float(d)
    y_data11.append(d)
sum_y_data.append(y_data11)
y_data12 = []
for d in df_2010[1::2]:
    d = float(d)
    y_data12.append(d)
sum_y_data.append(y_data12)

df_2012 = pd.read_excel('./data/2012-2013.xlsx').loc[1,['Unnamed: 22','Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27','Unnamed: 28','Unnamed: 29']]

y_data13 = []
for d in df_2012[::2]:
    d = float(d)
    y_data13.append(d)
sum_y_data.append(y_data13)
y_data14 = []
for d in df_2012[1::2]:
    y_data14.append(d)
sum_y_data.append(y_data14)

df_2014 = pd.read_excel('./data/2014-2015.xlsx').loc[1,['Unnamed: 15','Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20']]


y_data15 = []
for d in df_2014[::2]:
    d = d.strip('/n')
    y_data15.append(float(d))
y_data15.append(0)
sum_y_data.append(y_data15)
y_data16 = []
for d in df_2014[1::2]:
    d = d.strip('/n')
    y_data16.append(float(d))
y_data16.append(0)
sum_y_data.append(y_data16)

df_2016 = pd.read_excel('./data/2016-2017.xlsx').loc[2,['Unnamed: 15','Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20']]

y_data17 = []
for d in df_2016[::2]:
    d = float(d)
    y_data17.append(d)
del y_data17[0]
y_data17.append(0)
y_data17.append(0)
sum_y_data.append(y_data17)
y_data18 = []
for d in df_2016[1::2]:
    d = float(d)
    y_data18.append(d)
del y_data18[0]
y_data18.append(0)
y_data18.append(0)

sum_y_data.append(y_data18)

df_2018 = pd.read_excel('./data/2018-2019.xlsx').loc[2,['Unnamed: 13','Unnamed: 14','Unnamed: 15','Unnamed: 16']]

y_data19 = []
for d in df_2018[::2]:
    d = float(d)
    y_data19.append(d)

y_data19.append(0)
y_data19.append(0)

sum_y_data.append(y_data19)
y_data20 = []
for d in df_2018[1::2]:
    d = float(d)
    y_data20.append(d)

y_data20.append(0)
y_data20.append(0)

sum_y_data.append(y_data20)


time_list = [i for i in range(2000,2020)]


def main_reveral():
    tl = Timeline(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    for i in range(19):
        c = (
            Bar()
                .add_xaxis(x_data_1)
                .add_yaxis("{}年".format(time_list[i]),sum_y_data[i], label_opts=opts.LabelOpts(is_show=False),bar_width='15%',color='#1AD66A')
                       # itemstyle_opts={
                       #     "normal": {
                       #         "color": JsCode(
                       #             """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                       #             offset: 0,
                       #             color: '#1AD66A'
                       #         }, {
                       #             offset: 1,
                       #             color: '#01E562'
                       #         }])"""
                       #         ),
                       #         "barBorderRadius": 11,
                       #     }
                       # })
                .add_yaxis("{}年".format(time_list[i+1]),sum_y_data[i+1], label_opts=opts.LabelOpts(is_show=False), bar_width='15%',color='#09bcb7')
                       # itemstyle_opts={
                       #     "normal": {
                       #         "color": JsCode(
                       #             """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                       #             offset: 0,
                       #             color: '#8bd46e'
                       #         }, {
                       #             offset: 1,
                       #             color: '#09bcb7'
                       #         }])"""
                       #         ),
                       #         "barBorderRadius": 11,
                       #     }
                       # })
                .reversal_axis()

                .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="{}-{}年植树的状况".format(time_list[i],time_list[i+1],
                    title_textstyle_opts=opts.TextStyleOpts(
                        font_size=25, color="#FFFAFA"
                    ), )
                )
            )
        )
        tl.add(c, "{}".format(i))
        tl.add_schema(
            # 播放速度
            play_interval=1000,
            # 是否显示timeline组件
            is_timeline_show=False,
            # 是否自动播放
            is_auto_play=True,
        )
    return tl
