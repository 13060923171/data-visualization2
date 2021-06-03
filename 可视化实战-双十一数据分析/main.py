import pandas as pd
from pyecharts.charts import Bar,Timeline, Grid,Pie, Line,Page
from pyecharts import options as opts
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
x_data = ["{}".format(i) for i in time_list]

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

def get_bar_line(year: int):
    bar_1 = (
        Bar({"theme": ThemeType.MACARONS})
        .add_xaxis(x_data_1[year])
        .add_yaxis("金额(亿元)", data_list_1[year], label_opts=opts.LabelOpts(position="left"))
    )
    line = (
        Line({"theme": ThemeType.MACARONS})
        .add_xaxis(x_data_1[year])
        .add_yaxis("金额(亿元)", data_list_1[year], is_connect_nones=True)

    )
    return line.overlap(bar_1)

def get_bar(year: int):
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(x_data_1[year])
        .add_yaxis("金额(亿元)", data_list_1[year], label_opts=opts.LabelOpts(position="right"))
        .reversal_axis()
    )
    return bar

def get_pie(year: int):
    pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.SHINE))
        .add(
            "金额(亿元)",
            [list(z) for z in zip(x_data_1[year],data_list_1[year])],
            rosetype="radius",
            radius=["30%", "55%"],
        )
    )
    return pie

def get_time1():
    timeline = Timeline(
        init_opts=opts.InitOpts(theme=ThemeType.MACARONS)
    )
    for y in range(len(data_list_1)):
        g = get_bar_line(year=y)
        timeline.add(g, time_point=str(y))
    timeline.add_schema(
        # 播放速度
        play_interval=3000,
        # 是否显示timeline组件
        is_timeline_show=False,
        # 是否自动播放
        is_auto_play=True,
        label_opts=opts.LabelOpts(is_show=True, color="#fff"),
    )
    return timeline


def get_time2():
    timeline = Timeline({"theme": ThemeType.LIGHT})
    for y in range(len(data_list_1)):
        g = get_bar(year=y)
        timeline.add(g, time_point=str(y))
    timeline.add_schema(
        # 播放速度
        play_interval=3000,
        # 是否显示timeline组件
        is_timeline_show=False,
        # 是否自动播放
        is_auto_play=True,
        label_opts=opts.LabelOpts(is_show=True, color="#fff"),
    )
    return timeline

def get_time3():
    timeline = Timeline(
        init_opts=opts.InitOpts(theme=ThemeType.SHINE)
    )
    for y in range(len(data_list_1)):
        g = get_pie(year=y)
        timeline.add(g, time_point=str(y))
    timeline.add_schema(
        # 播放速度
        play_interval=3000,
        # 是否显示timeline组件
        is_timeline_show=False,
        # 是否自动播放
        is_auto_play=True,
    )
    return timeline

def get_page():
    page = (
        Page(layout=Page.DraggablePageLayout)
        .add(get_time1(), get_time2(),get_time3())
        .save_resize_html(cfg_file="chart_config.json")
    )



if __name__ == "__main__":
    get_page()





