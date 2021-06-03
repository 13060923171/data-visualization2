import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line,Timeline


time_list = ['2015','2016','2017','2018','2019','2020']
x_data = ['32.54','36.95','41.21','47.55','54.91','75.82']
x_data1 = ['63.18','71.95','79.10','90.92','102.35','131.85']
y_data = ['0','12.68','11.11','14.94','12.57','28.82']
y_data1 = ['0','13.55','11.53','15.38','15.48','38.08']

y = []
y.append(y_data)
y.append(y_data1)
x = []
x.append(x_data)
x.append(x_data1)

tl = Timeline()
for i in range(2):
    bar = (
        Bar()
        .add_xaxis(time_list)
        .add_yaxis(
            "",
            x[i],
            yaxis_index=0,
            color="#5793f3",
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="增长率",
                type_="value",
                min_=0,
                max_=100,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} %"),
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2015-2020年口罩产业产值情况（单位：亿元）"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
    )

    line = (
        Line(init_opts=opts.InitOpts(width="1300px", height="600px"))
        .add_xaxis(xaxis_data=time_list)
        .add_yaxis(
            series_name="",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#675bba",
            y_axis=y[i],
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=4)
        )
    )
    bar.overlap(line)
    grid = Grid()
    grid.add(bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True)
    tl.add(grid, "{}年".format(i))
    tl.add_schema(
        # 播放速度
        play_interval=1000,
        # 是否显示timeline组件
        is_timeline_show=False,
        # 是否自动播放
        is_auto_play=True,
    )
tl.render("timeline.html")