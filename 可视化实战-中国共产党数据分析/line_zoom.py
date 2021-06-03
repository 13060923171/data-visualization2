import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar,Timeline

y_data = [
    3.5,
    3.2,
    3.0,
    3.1,
    2.8,
    2.5,
    2.3,
    1.6,
    4.2,
    8.5,
    7.2,
    5.7,
    4.5,
    3.1,
    1.7,
    0.6,
    3.8,
    10.2,
    12.7,
    14.8,
    17.2,
    ]

x_data = ["{}年".format(i) for i in range(2000, 2021)]
def Line_zoom():
    c = (
        Line({"theme": ThemeType.INFOGRAPHIC})
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="",
            y_axis=y_data,
            symbol="emptyCircle",
            is_symbol_show=True,
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=True),
        )
        .set_global_opts(datazoom_opts=opts.DataZoomOpts(),
                         title_opts=opts.TitleOpts(
                             title="中国人民的幸福指数",
                             pos_left="left",
                             pos_top="top", )
                         )
    )

    return c