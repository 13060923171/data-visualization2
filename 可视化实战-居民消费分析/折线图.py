import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line

df = pd.read_excel('居民消费价-数据.xlsx')

beijing_list = []
for i in df.iloc[0][1:]:
    beijing_list.append(i)

shanghai_list = []
for i in df.iloc[8][1:]:
    shanghai_list.append(i)

guangdong_list = []
for i in df.iloc[18][1:]:
    guangdong_list.append(i)

chongqing_list = []
for i in df.iloc[21][1:]:
    chongqing_list.append(i)

zhejian_list = []
for i in df.iloc[10][1:]:
    zhejian_list.append(i)

hunan_list = []
for i in df.iloc[17][1:]:
    hunan_list.append(i)

hubei_list = []
for i in df.iloc[16][1:]:
    hubei_list.append(i)

x_data = ['2019.11','2019.12','2020.01','2020.02','2020.03','2020.04','2020.05','2020.06','2020.07','2020.08','2020.09','2020.10','2020.11']

line = (
    Line(init_opts=opts.InitOpts(width="1300px", height="600px"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="北京",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#d14a61",
        y_axis=beijing_list,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=1)
    )
    .add_yaxis(
        series_name="广东",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#6e9ef1",
        y_axis=guangdong_list,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=2)
    )
    .add_yaxis(
            series_name="上海",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#F9FF33",
            y_axis=shanghai_list,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )
    .add_yaxis(
            series_name="浙江",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#A0FF33",
            y_axis=zhejian_list,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )
    .add_yaxis(
            series_name="湖南",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#33FF76",
            y_axis=hunan_list,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )
    .add_yaxis(
            series_name="湖北",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#337FFF",
            y_axis=hubei_list,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )

    .add_yaxis(
            series_name="重庆",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#A333FF",
            y_axis=chongqing_list,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="热门省份消费水平"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            min_=98.5,
            max_=108.5,
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,axisline_opts=opts.AxisLineOpts(
                is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            )),
    )
    .render("line.html")
)