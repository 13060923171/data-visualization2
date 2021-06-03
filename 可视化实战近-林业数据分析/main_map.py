import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Map,Timeline

df_2001 = pd.read_excel('./data/2000-2001.xlsx').loc[3:,['Unnamed: 0','Unnamed: 1','Unnamed: 2']]
df_2002 = pd.read_excel('./data/2002-2003.xlsx').loc[3:,['Unnamed: 0','Unnamed: 1','Unnamed: 2']]
df_2004 = pd.read_excel('./data/2004-2005.xlsx').loc[3:,['Unnamed: 0','Unnamed: 1','Unnamed: 2']]
df_2006 = pd.read_excel('./data/2006-2007.xlsx').loc[3:,['Unnamed: 0','Unnamed: 1','Unnamed: 2']]
df_2008 = pd.read_excel('./data/2008-2009.xlsx').loc[3:,['Unnamed: 0','Unnamed: 1','Unnamed: 2']]
df_2010 = pd.read_excel('./data/2010-2011.xlsx').loc[3:,['Unnamed: 0','Unnamed: 1','Unnamed: 2']]
df_2012 = pd.read_excel('./data/2012-2013.xlsx').loc[3:,['Unnamed: 0','Unnamed: 1','Unnamed: 2']]
df_2014 = pd.read_excel('./data/2014-2015.xlsx').loc[3:,['Unnamed: 0','Unnamed: 1','Unnamed: 2']]
df_2016 = pd.read_excel('./data/2016-2017.xlsx').loc[3:,['Unnamed: 0','Unnamed: 1','Unnamed: 2']]
df_2018 = pd.read_excel('./data/2018-2019.xlsx').loc[3:,['Unnamed: 0','Unnamed: 1','Unnamed: 2']]

city_list = []
for c in df_2001['Unnamed: 0']:
    c = str(c)
    c = c.strip(' ')
    city_list.append(c)

df_2006['Unnamed: 1'] = [(str(i).replace(" ", "").replace("．", ".")) for i in df_2006['Unnamed: 1']]
df_2006['Unnamed: 2'] = [(str(i).replace(" ", "").replace("．", ".")) for i in df_2006['Unnamed: 2']]
df_2008['Unnamed: 1'] = [(str(i).replace(" ", "").replace("．", ".")) for i in df_2008['Unnamed: 1']]
df_2008['Unnamed: 2'] = [(str(i).replace(" ", "").replace("．", ".")) for i in df_2008['Unnamed: 2']]


data_pair_1 = [list(z) for z in zip(city_list,df_2001['Unnamed: 1'])]
data_pair_2 = [list(z) for z in zip(city_list,df_2001['Unnamed: 2'])]
data_pair_3 = [list(z) for z in zip(city_list,df_2002['Unnamed: 1'])]
data_pair_4 = [list(z) for z in zip(city_list,df_2002['Unnamed: 2'])]
data_pair_5 = [list(z) for z in zip(city_list,df_2004['Unnamed: 1'])]
data_pair_6 = [list(z) for z in zip(city_list,df_2004['Unnamed: 2'])]

data_pair_7 = [list(z) for z in zip(city_list,df_2006['Unnamed: 1'].map(float))]
data_pair_8 = [list(z) for z in zip(city_list,df_2006['Unnamed: 2'].map(float))]
data_pair_9 = [list(z) for z in zip(city_list,df_2008['Unnamed: 1'].map(float))]
data_pair_10 = [list(z) for z in zip(city_list,df_2008['Unnamed: 2'].map(float))]
data_pair_11 = [list(z) for z in zip(city_list,df_2010['Unnamed: 1'].map(float))]
data_pair_12 = [list(z) for z in zip(city_list,df_2010['Unnamed: 2'].map(float))]
data_pair_13 = [list(z) for z in zip(city_list,df_2012['Unnamed: 1'])]
data_pair_14 = [list(z) for z in zip(city_list,df_2012['Unnamed: 2'])]
data_pair_15 = [list(z) for z in zip(city_list,df_2014['Unnamed: 1'].map(float))]
data_pair_16 = [list(z) for z in zip(city_list,df_2014['Unnamed: 2'].map(float))]
data_pair_17 = [list(z) for z in zip(city_list,df_2016['Unnamed: 1'].map(float))]
data_pair_18 = [list(z) for z in zip(city_list,df_2016['Unnamed: 2'].map(float))]
data_pair_19 = [list(z) for z in zip(city_list,df_2018['Unnamed: 1'].map(float))]
data_pair_20 = [list(z) for z in zip(city_list,df_2018['Unnamed: 2'].map(float))]

sum_list = []
sum_list.append(data_pair_1)
sum_list.append(data_pair_2)
sum_list.append(data_pair_3)
sum_list.append(data_pair_4)
sum_list.append(data_pair_5)
sum_list.append(data_pair_6)
sum_list.append(data_pair_7)
sum_list.append(data_pair_8)
sum_list.append(data_pair_9)
sum_list.append(data_pair_10)
sum_list.append(data_pair_11)
sum_list.append(data_pair_12)
sum_list.append(data_pair_13)
sum_list.append(data_pair_14)
sum_list.append(data_pair_15)
sum_list.append(data_pair_16)
sum_list.append(data_pair_17)
sum_list.append(data_pair_18)
sum_list.append(data_pair_19)
sum_list.append(data_pair_20)


def time_map():
    time_list = [i for i in range(2000, 2020)]
    tl = Timeline()
    for i in range(20):
        map = (
            Map(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
                .add(
                "",
                sum_list[i],
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
                    title="{}年造林总面积".format(time_list[i]),
                    pos_left="center",
                    pos_top="top",
                    title_textstyle_opts=opts.TextStyleOpts(
                        font_size=25, color="rgba(47, 7, 19, 0.9)"
                    ), ),
                tooltip_opts=opts.TooltipOpts(
                    trigger="item", formatter="{b}<br/>{c} (/千公顷)"
                ),
                visualmap_opts=opts.VisualMapOpts(
                    is_calculable=True,
                    dimension=0,
                    pos_left="10",
                    pos_top="center",
                    range_text=["High", "Low"],
                    range_color=["White", "Aquamarine", "MediumAquamarine", "SpringGreen", "Lime"],
                    textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                    min_=0,
                    max_=1000,
                    is_show=False
                ),
            )
        )
        tl.add(map, "{}年".format(time_list[i]))
        tl.add_schema(
            # 播放速度
            play_interval=3000,
            # 是否显示timeline组件
            is_timeline_show=False,
            # 是否自动播放
            is_auto_play=True,
        )
    tl.render('./data/全国造林总面积.html')

if __name__ == '__main__':
    time_map()




