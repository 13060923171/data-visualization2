import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType

df = pd.read_excel('dates.xls').loc[28:34,['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']]
df.fillna(value=df.mean(),inplace=True)

x_data = [str(i) for i in range(2009,2020)]
list_dalian = [float(i) for i in df.iloc[0]]
list_shenyang = [float(i) for i in df.iloc[1]]
list_changchun = [float(i) for i in df.iloc[2]]
list_haerbin = [float(i) for i in df.iloc[3]]
list_qingdao = [float(i) for i in df.iloc[4]]
list_xiamen = [float(i) for i in df.iloc[5]]
list_shenzhen = [float(i) for i in df.iloc[6]]

c =(
    Line(init_opts=opts.InitOpts(width="1600px", height="800px",theme=ThemeType.CHALK))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="大连",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#ADFF2F",
        y_axis=list_dalian,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=3)
    )
    .add_yaxis(
        series_name="沈阳",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#00FA9A",
        y_axis=list_shenyang,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=3)
    )
    .add_yaxis(
        series_name="长春",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#00FA9A",
        y_axis=list_changchun,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=3)
    )
    .add_yaxis(
        series_name="哈尔滨",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#00FA9A",
        y_axis=list_haerbin,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=3)
    )
    .add_yaxis(
        series_name="青岛",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#00FA9A",
        y_axis=list_qingdao,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=3)
    )
    .add_yaxis(
        series_name="厦门",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#00FA9A",
        y_axis=list_xiamen,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=3)
    )
    .add_yaxis(
        series_name="深圳",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#00FA9A",
        y_axis=list_shenzhen,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=3)
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="户籍人口自然增长率_市辖区"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name="‰",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,axisline_opts=opts.AxisLineOpts(
                is_on_zero=False,
            )),
    )
    .render("户籍人口自然增长率_市辖区.html")
)

