from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
import pandas as pd
from pyecharts.globals import ChartType
from pyecharts.charts import Bar,Timeline
from pyecharts.globals import ThemeType

df = pd.read_excel('data.xlsx').loc[:,['Country','Month','Number']]

x_data = ['Australia','Canada','United Kingdom','United States','China']
y_data_1 = ['0','0','0','0','9336']
y_data_2 = ['0','14','19','64','35420']
y_data_3 = ['0','8591','25474','161367','2895']
y_data_4 = ['6766','53021','171253','1092656','897']
y_data_5 = ['7185','90516','274762','1797949','119']
y_data_6 = ['7836','103918','312654','2695685','516']
y_data_7 = ['16303','115935','301455','4570103','2227']
y_data_8 = ['25670','127673','332752','6141778','649']
y_data_9 = ['27078','158425','453264','7413600','365']
y_data_10 = ['27580','229438','989745','9336073','521']

y_data = []
y_data.append(y_data_1)
y_data.append(y_data_2)
y_data.append(y_data_3)
y_data.append(y_data_4)
y_data.append(y_data_5)
y_data.append(y_data_6)
y_data.append(y_data_7)
y_data.append(y_data_8)
y_data.append(y_data_9)
y_data.append(y_data_10)

time_list = ['202001','202002','202003','202004','202005','202006','202007','202008','202009','202010']
tl = Timeline()
for i in range(1,11):
    map = (
        Map()
        .add("",
             [list(z) for z in zip(x_data, y_data[int(i-1)])],
             "world",
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
                title="Map-世界地图",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(47, 7, 19, 0.9)"
                ),),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="center",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=0,
                max_=4000000,
            ),
        )
    )
    tl.add(map, "{}".format(time_list[int(i-1)]))
    tl.add_schema(
        # 播放速度
        play_interval=1000,
        # 是否显示timeline组件
        is_timeline_show=False,
        # 是否自动播放
        is_auto_play=True,
    )
tl.render("map.html")
