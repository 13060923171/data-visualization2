import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line,Timeline
from pyecharts.globals import ThemeType

df = pd.read_excel('2017年双十一销售额实时数据.xlsx').loc[:,['时间', '金额（亿元）']]

time_list = []
for t in df['时间']:
    t = str(t)
    t = t.replace('00分10秒','00:00').replace('02分00秒','00:02').replace('03分01秒','00:03').replace('6分05秒','00:06').replace('40分12秒','00:40')
    t = t.replace('点',':').replace('分','').replace('20:','20:00').replace('23:','23:00')
    time_list.append(t)

data_list = []
for d in df['金额（亿元）']:
    data_list.append(d[:-1])
x_data = ["{}分".format(i) for i in time_list]

data_list_1 = []
x_data_1 = []
data_list_1.append(data_list[0:5])
data_list_1.append(data_list[5:10])
data_list_1.append(data_list[10:15])
data_list_1.append(data_list[15:20])
x_data_1.append(x_data[0:5])
x_data_1.append(x_data[5:10])
x_data_1.append(x_data[10:15])
x_data_1.append(x_data[15:20])

tl = Timeline({'theme':ThemeType.MACARONS})
for i in range(len(x_data_1)):
    c = (
        Line({"theme": ThemeType.MACARONS})
        .add_xaxis(x_data_1[i])
        .add_yaxis("商家A", data_list_1[i],is_connect_nones=True)
        .set_global_opts(
            title_opts=opts.TitleOpts("Timeline-Bar-Reversal (时间: {} 年)".format(i))
        )
    )
    tl.add(c, "{}年".format(i))
tl.render("timeline_bar_reversa2.html")