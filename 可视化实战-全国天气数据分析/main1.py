from pyecharts import options as opts
from pyecharts.charts import Gauge
import pandas as pd

df = pd.read_csv('./csv_file/当前空气质量.csv',encoding='gbk')
a = ','.join(df.columns)
a = a.split(',')

c = (
    Gauge()
        .add(
        "",
        [("{}".format(a[2]), a[1])],
        split_number=10,
        min_=0,
        max_=500,
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
            )
        ),
        detail_label_opts=opts.LabelOpts(formatter="{value}"),
    )
        .set_global_opts(
        title_opts={"text": "{}".format(a[0]), "subtext": "{}".format(a[-1])},
        legend_opts=opts.LegendOpts(is_show=False),
    )
        .render("gauge_splitnum_label.html")
)