import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar,Timeline,Map
import pandas as pd

df = pd.read_excel('./数据/历年各地贫困人口统计.xls').loc[3:33,['中国历年分地区农村贫困人口统计','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13','Unnamed: 14','Unnamed: 15','Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20']]

list_city = []
for i in df['中国历年分地区农村贫困人口统计']:
    i = str(i)
    list_city.append(i)


list_2010 = []
for i in df['Unnamed: 11']:
    if i == "*":
        i = i.replace('*','0')
    i = int(i)
    list_2010.append(i)

list_2011 = []
for i in df['Unnamed: 12']:
    if i == "*":
        i = i.replace('*','0')
    i = int(i)
    list_2011.append(i)

list_2012 = []
for i in df['Unnamed: 13']:
    if i == "*":
        i = i.replace('*','0')
    i = int(i)
    list_2012.append(i)

list_2013 = []
for i in df['Unnamed: 14']:
    if i == "*":
        i = i.replace('*','0')
    i = int(i)
    list_2013.append(i)

list_2014 = []
for i in df['Unnamed: 15']:
    if i == "*":
        i = i.replace('*','0')
    i = int(i)
    list_2014.append(i)

list_2015 = []
for i in df['Unnamed: 16']:
    if i == "*":
        i = i.replace('*','0')
    i = int(i)
    list_2015.append(i)

list_2016 = []
for i in df['Unnamed: 17']:
    if i == "*":
        i = i.replace('*','0')
    i = int(i)
    list_2016.append(i)

list_2017 = []
for i in df['Unnamed: 18']:
    if i == "*":
        i = i.replace('*','0')
    i = int(i)
    list_2017.append(i)

list_2018 = []
for i in df['Unnamed: 19']:
    if i == "*":
        i = i.replace('*','0')
    i = int(i)
    list_2018.append(i)

list_2019 = []
for i in df['Unnamed: 20']:
    if i == "*":
        i = i.replace('*','0')
    if i == "*\n":
        i = i.replace('*\n','0')
    i = int(i)
    list_2019.append(i)

list_2000 = []
for i in df['Unnamed: 1']:
    i = int(i)
    list_2000.append(i)

list_2001 = []
for i in df['Unnamed: 2']:
    i = int(i)
    list_2001.append(i)


list_2003 = []
for i in df['Unnamed: 4']:
    i = int(i)
    list_2003.append(i)

list_2004 = []
for i in df['Unnamed: 5']:
    i = int(i)
    list_2004.append(i)

list_2005 = []
for i in df['Unnamed: 6']:
    i = int(i)
    list_2005.append(i)

list_2006 = []
for i in df['Unnamed: 7']:
    i = int(i)
    list_2006.append(i)

list_2007 = []
for i in df['Unnamed: 8']:
    i = int(i)
    list_2007.append(i)

list_2008 = []
for i in df['Unnamed: 9']:
    i = int(i)
    list_2008.append(i)

list_2009 = []
for i in df['Unnamed: 10']:
    i = int(i)
    list_2009.append(i)



list_time = []
for i in range(2000,2020):
    i = str(i)
    list_time.append(i)

del list_time[2]

list_sum = []
list_sum.append(list_2000)
list_sum.append(list_2001)
list_sum.append(list_2003)
list_sum.append(list_2004)
list_sum.append(list_2005)
list_sum.append(list_2006)
list_sum.append(list_2007)
list_sum.append(list_2008)
list_sum.append(list_2009)
list_sum.append(list_2010)
list_sum.append(list_2011)
list_sum.append(list_2012)
list_sum.append(list_2013)
list_sum.append(list_2014)
list_sum.append(list_2015)
list_sum.append(list_2016)
list_sum.append(list_2017)
list_sum.append(list_2018)
list_sum.append(list_2019)

def Map_people():
    tl = Timeline()
    for i in range(len(list_time)):
            map = (
                Map({"theme": ThemeType.ROMANTIC})
                    .add("",
                         [list(z) for z in zip(list_city, list_sum[i])],
                         "china",
                         label_opts=opts.LabelOpts(is_show=False),
                         is_map_symbol_show=False,
                         itemstyle_opts={
                             "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                             "emphasis": {
                                 "label": {"show": Timeline},
                                 "areaColor": "rgba(255,255,255, 0.5)",
                             },
                         },
                         )
                    .set_global_opts(
                    title_opts=opts.TitleOpts(
                        title="{}年中国各省贫困人口分布状况".format(list_time[i]),
                        pos_left="center",
                        pos_top="top",
                        title_textstyle_opts=opts.TextStyleOpts(
                            font_size=25, color="rgba(47, 7, 19, 0.9)"
                        ), ),
                    visualmap_opts=opts.VisualMapOpts(
                        is_calculable=True,
                        dimension=0,
                        pos_left="10",
                        pos_top="center",
                        range_text=["High", "Low"],
                        range_color=["Lavender", "LightSalmon", "OrangeRed",'Crimson','Red'],
                        textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                        min_=0,
                        max_=2000,
                    ),
                )
            )
            tl.add(map, "{}".format(list_time[i]))
            tl.add_schema(
                # 播放速度
                play_interval=1000,
                # 是否显示timeline组件
                is_timeline_show=False,
                # 是否自动播放
                is_auto_play=True,
            )
    return tl




