from pyecharts import options as opts
from pyecharts.charts import Gauge
import pandas as pd


def develop_gauge():
    c = (
        Gauge()
            .add(
            "",
            [("发展阶段", 30)],
            split_number=10,
            min_=0,
            max_=100,
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#FA8072"), (0.7, "#F08080"), (1, "#CD5C5C")], width=30
                )
            ),
            detail_label_opts=opts.LabelOpts(formatter="{value}"),
        )
            .set_global_opts(
            title_opts={"text": "{}".format('我国目前仍然处于社会主义初级阶段'), "subtext": "{}".format('但是党推动我国社会主义从初级阶段向更高阶段迈进')},
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(is_show=False, formatter="{a} <br/>{b} : {c}%"),
        )
    )
    return c