import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType

df = pd.read_excel('./data/全国造林面积.xls').loc[:,['全国造林总面积']]

data_list = []
for t in df['全国造林总面积']:
    t = float(t)
    data_list.append(t)

x_data = []
for i in range(2000,2020):
     i = '{}年'.format(i)
     x_data.append(i)

y_data1 = []
for y in range(len(data_list)):
    j = (data_list[y] - data_list[0]) / int(data_list[0] * 100)
    y_data1.append(float(j))

y_data2 = []
for y in range(len(data_list)-1):
    j = (data_list[y+1] - data_list[y]) / int(data_list[y] * 100)
    y_data2.append(float(j))

(
    Line(init_opts=opts.InitOpts(width="1600px", height="800px",theme=ThemeType.CHALK))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="2000年全国造林面积为基数-环比增长速度",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#ADFF2F",
        y_axis=y_data1,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=3)
    )
    .add_yaxis(
        series_name="环比增长速度",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#00FA9A",
        y_axis=y_data2,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=3)
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国造林面积增长速度"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,axisline_opts=opts.AxisLineOpts(
                is_on_zero=False,
            )),
    )
    .render("全国造林面积增长速度.html")
)
