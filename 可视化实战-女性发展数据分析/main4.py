from pyecharts import options as opts
from pyecharts.charts import Polar
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

x_data = ['高中及以下','大专','本科','硕士及以上']


def main_polar():
    c = (
        Polar({"theme": ThemeType.ROMA})
        .add_schema(angleaxis_opts=opts.AngleAxisOpts(data=x_data, type_="category", is_clockwise=True))
        .add("女", [7.9, 28.6, 56.7, 6.8], type_="bar", stack="stack0")
        .add("男", [15.5,35.6,43.7,5.5], type_="bar", stack="stack0")
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c}%"
            ),
            label_opts=opts.LabelOpts(is_show=False)
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="女性在传媒教育的相关情况"))
    )
    return c