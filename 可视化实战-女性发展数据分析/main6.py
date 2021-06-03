import pyecharts.options as opts
from pyecharts.charts import Line


x_data = ['公司提供的晋升机会有限','个人能力和经验不足','领导和上级任人唯亲','论资排辈，不重能力','同等资历的人才多，竞争激烈','领导不赏识','个人不追求晋升，更在意工作和家庭的平衡','照顾家庭，职场精力分散','处于婚育阶段，被动失去晋升','性别歧视']
y_woman = ['69.04','32.06','20.94','19.42','22.76','16.27','10.07','8.30','9.02','6.01']

def main_line():
    c = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="女性",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#d14a61",
            y_axis=y_woman,
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=4)
        )

        .set_global_opts(

            title_opts=opts.TitleOpts(title="女性在职场面临的发展障碍"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axislabel_opts=opts.LabelOpts(formatter="{value} %"),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,axisline_opts=opts.AxisLineOpts(
                    is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                )),
        )

    )
    return c

