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


(
    Line(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#d14a61",
        y_axis=data_list,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=3)
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国造林时间趋势图"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            axislabel_opts=opts.LabelOpts(formatter="{value}/千公顷"),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,axisline_opts=opts.AxisLineOpts(
                is_on_zero=False,
            )),
    )
    .render("./data/全国造林时间趋势图.html")
)

