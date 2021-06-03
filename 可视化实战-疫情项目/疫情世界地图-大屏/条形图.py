import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar,Timeline
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode

df = pd.read_excel('data.xlsx').loc[:,['Country','Month','Number']]

x_data = ['Australia','Canada','UK','USA','China']
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

sum = 0
for i in y_data_10:
    i = int(i)
    sum +=i
print(sum)
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
tl = Timeline({"theme": ThemeType.MACARONS})
for i in range(1,11):
    bar = (
        Bar(init_opts=opts.InitOpts(width="300px", height="200px",theme=ThemeType.MACARONS))
        .add_xaxis(x_data)
        .add_yaxis(
            "",
            y_data[int(i-1)],
            category_gap="60%",
            label_opts=opts.LabelOpts(
                is_show=True, position="right", formatter="{b} : {c}"
            ),
            )
        .reversal_axis()
        .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "color": JsCode(
                        """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: 'rgba(0, 244, 255, 1)'
                }, {
                    offset: 1,
                    color: 'rgba(0, 77, 167, 1)'
                }], false)"""
                    ),
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "rgb(0, 160, 221)",
                }
            }
        )
        .set_global_opts(
            title_opts=opts.TitleOpts("time:{}".format(time_list[int(i-1)]),pos_left="35%", pos_top="5%")
        )
    )
    tl.add(bar, "{}".format(time_list[int(i-1)]))
    tl.add_schema(
        # 播放速度
        play_interval=1000,
        # 是否显示timeline组件
        is_timeline_show=False,
        # 是否自动播放
        is_auto_play=True,
    )
# tl.render("bar.html")
