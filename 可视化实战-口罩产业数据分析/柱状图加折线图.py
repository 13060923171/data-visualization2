import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line

df = pd.read_excel('口罩产业.xlsx',sheet_name='Sheet3').loc[1:6,['2015-2019年医用口罩产业产值情况（单位：亿元）','Unnamed: 1','Unnamed: 2']]
time_list = []
x_data1 = []
x_data2 = []
for t in df['2015-2019年医用口罩产业产值情况（单位：亿元）']:
    t = str(t)
    time_list.append(t)

for x_1 in df['Unnamed: 1']:
    x_data1.append(x_1)

for x_2 in df['Unnamed: 2']:
    x_2 = float(x_2*100)
    x_2 = '{:0.2f}'.format(x_2)
    x_2 = x_2.replace('0.00','0')
    x_data2.append(x_2)



bar = (
    Bar()
    .add_xaxis(time_list)
    .add_yaxis(
        "",
        x_data1,
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
        y_axis=x_data2,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=4)
    )
)



bar.overlap(line)
grid = Grid()
grid.add(bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True)
grid.render("图1.html")