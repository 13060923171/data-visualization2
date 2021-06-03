import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.globals import CurrentConfig,ThemeType

salary = ['16','13.5','14.5','11','9','14','9.6','11','12','9']
company = ['北京','深圳','上海','广州','成都','杭州','武汉','南京','厦门','西安']

c = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(company)
    .add_yaxis("一线城市平均工资", salary)

    .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        title_opts=opts.TitleOpts(title="一线城市平均工资"),
        yaxis_opts=opts.AxisOpts(
            name="平均工资",
            type_="value",
            min_=0,
            max_=20,
            interval=5,
            axislabel_opts=opts.LabelOpts(formatter="{value}k"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .render("bar.html")
)