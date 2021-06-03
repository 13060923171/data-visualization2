import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode

sum_y_data = []
df_2001 = pd.read_excel('./data/2000-2001.xlsx').loc[2,['Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6']]
x_data = ['当年造林面积','人工造林面积','飞机播种造林面积']
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

df_2002 = pd.read_excel('./data/2002-2003.xlsx').loc[2,['Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6']]

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

df_2004 = pd.read_excel('./data/2004-2005.xlsx').loc[2,['Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6']]

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

df_2006 = pd.read_excel('./data/2006-2007.xlsx').loc[2,['Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6']]

y_data7 = []
for d in df_2006[::2]:
    d = d.split(' ')
    d = d[-1]

    y_data7.append(d)
sum_y_data.append(y_data7)
y_data8 = []
for d in df_2006[1::2]:
    d = d.split(' ')
    d = d[-1]
    y_data8.append(d)
sum_y_data.append(y_data8)

df_2008 = pd.read_excel('./data/2008-2009.xlsx').loc[2,['Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6']]

y_data9 = []
for d in df_2008[::2]:
    d = float(d)
    y_data9.append(d)
sum_y_data.append(y_data9)
y_data10 = []
for d in df_2008[1::2]:
    d = float(d)
    y_data10.append(d)
sum_y_data.append(y_data10)

df_2010 = pd.read_excel('./data/2010-2011.xlsx').loc[2,['Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6']]

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

df_2012 = pd.read_excel('./data/2012-2013.xlsx').loc[2,['Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6']]

y_data13 = []
for d in df_2012[::2]:
    d = float(d)
    y_data13.append(d)
sum_y_data.append(y_data13)
y_data14 = []
for d in df_2012[1::2]:
    y_data14.append(d)
sum_y_data.append(y_data14)

df_2014 = pd.read_excel('./data/2014-2015.xlsx').loc[2,['Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6']]

y_data15 = []
for d in df_2014[::2]:
    d = float(d)
    y_data15.append(d)
sum_y_data.append(y_data15)
y_data16 = []
for d in df_2014[1::2]:
    d = float(d)
    y_data16.append(d)
sum_y_data.append(y_data16)

df_2016 = pd.read_excel('./data/2016-2017.xlsx').loc[2,['Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6']]

y_data17 = []
for d in df_2016[::2]:
    d = float(d)
    y_data17.append(d)
sum_y_data.append(y_data17)
y_data18 = []
for d in df_2016[1::2]:
    d = float(d)
    y_data18.append(d)
sum_y_data.append(y_data18)

df_2018 = pd.read_excel('./data/2018-2019.xlsx').loc[2,['Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6']]

y_data19 = []
for d in df_2018[::2]:
    d = float(d)
    y_data19.append(d)
sum_y_data.append(y_data19)
y_data20 = []
for d in df_2018[1::2]:
    d = float(d)
    y_data20.append(d)
sum_y_data.append(y_data20)


del sum_y_data[6]
del sum_y_data[6]
sum_y_data.insert(6,[3838.8,2446.1,271.8])
sum_y_data.insert(7,[3907.7,2738.5,118.7])
from pyecharts.charts import Timeline

time_list = [i for i in range(2000,2020)]

def main_bar():
    tl = Timeline()
    for i in range(19):
        c = (
            Bar()
            .add_xaxis(x_data)
            .add_yaxis("{}".format(time_list[i]),
                       sum_y_data[i],
                       label_opts=opts.LabelOpts(
                           is_show=False
                       ),
                       bar_width='15%',
                       itemstyle_opts={
                           "normal": {
                               "color": JsCode(
                                   """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                   offset: 0,
                                   color: '#1AD66A'
                               }, {
                                   offset: 1,
                                   color: '#01E562'
                               }])"""
                               ),
                               "barBorderRadius": 11,
                           }
                       }
                       )
            .add_yaxis("{}".format(time_list[i+1]),
                           sum_y_data[i+1],
                           label_opts=opts.LabelOpts(
                               is_show=False
                           ),
                            bar_width='15%',
                       itemstyle_opts={
                           "normal": {
                               "color": JsCode(
                                   """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                   offset: 0,
                                   color: '#8bd46e'
                               }, {
                                   offset: 1,
                                   color: '#09bcb7'
                               }])"""
                               ),
                               "barBorderRadius": 11,
                           }
                       }
                           )
            .set_global_opts(
                legend_opts=opts.LegendOpts(
                    pos_top=12,
                    pos_right=10,
                    textstyle_opts=opts.TextStyleOpts(
                        color='#fff'
                    )
                ),
                tooltip_opts=opts.TooltipOpts(
                    trigger="axis",
                    axis_pointer_type="shadow",
                    textstyle_opts=opts.TextStyleOpts(
                        color="#fff"
                    )
                ),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(
                            color="	White"
                        )
                    ),
                    axislabel_opts=opts.LabelOpts(
                    )
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(
                        is_show=False
                    ),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True,
                        linestyle_opts=opts.LineStyleOpts(
                            color='rgba(255,255,255,0.3)'
                        ),
                    ),
                    axisline_opts=opts.AxisLineOpts(
                        is_show=False,
                        linestyle_opts=opts.LineStyleOpts(
                            color="	White"
                        )
                    ),
                    axislabel_opts=opts.LabelOpts()
                ),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="{}年-{}年造林面积".format(time_list[i],time_list[i+1]),title_textstyle_opts=opts.TextStyleOpts(
                        font_size=25, color="#FFFAFA")
                    ))
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
