import pyecharts.options as opts
from pyecharts.charts import Bar, Line, Grid
from pyecharts.globals import ThemeType

x_data = ['赞同','不赞同','不知道','无所谓']
y_data = [0.03, 0.89, 0.08]
y2_data = [0.55, 0.15, 0.18, 0.12]


# 折线图对象
line = Line(opts.InitOpts(bg_color="#344b58"))
# 设置图形的全局参数
(
    line.set_global_opts(
        title_opts=opts.TitleOpts(
            title="家长与对学生吸烟的看法",
            subtitle="计算单位:(%)",
            title_textstyle_opts=opts.TextStyleOpts(
                color="#90979c",
                font_size="16"
            )
        ),
        legend_opts=opts.LegendOpts(
            pos_top="8%",
            textstyle_opts=opts.TextStyleOpts(
                color='#90979c'
            )
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis",
            axis_pointer_type="shadow",
            textstyle_opts=opts.TextStyleOpts(
                color="#fff"
            )
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color="#90979c"
                )
            ),
            splitline_opts=opts.SplitLineOpts(
                is_show=False
            ),
            axistick_opts=opts.AxisTickOpts(
                is_show=False
            ),
            splitarea_opts=opts.SplitAreaOpts(
                is_show=False
            ),
            axislabel_opts=opts.LabelOpts(
                interval=0
            )
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(
                is_show=False
            ),
            splitline_opts=opts.SplitLineOpts(
                is_show=False
            ),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color="#90979c"
                )
            ),
            axislabel_opts=opts.LabelOpts(
                interval=0
            ),
            splitarea_opts=opts.SplitAreaOpts(
                is_show=False
            )
        ),
        # datazoom_opts=opts.DataZoomOpts(
        #     is_show=True,
        #     xaxis_index=[0],
        #     pos_bottom=30,
        #     start_value=10,
        #     end_value=80
        # )
    )
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="家长对学生吸烟的态度",
        y_axis=y_data,
        label_opts=opts.LabelOpts(
            is_show=True,
            color="#fff",
            position="inside"
        ),
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgba(255,144,128,1)"
        )
    )
    .add_yaxis(
        series_name="家长与老师是否可以在孩子面前吸烟",
        y_axis=y2_data,
        label_opts=opts.LabelOpts(
            is_show=True,
            color="#fff",
            position="inside"
        ),
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgba(0,191,183,1)"
        )
    )
    .render("pyecharts_line.html")
)
