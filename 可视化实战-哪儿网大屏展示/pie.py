import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType


def main_pie():
    df = pd.read_csv('data.csv')
    def zhuanhuan(x):
        x1 = str(x)
        if '万' in x1:
            x1 = x1.replace('万','')
            x1 = int(float(x1) * 10000)
            return x1
        else:
            return x1
    df['观看量'] = df['观看量'].apply(zhuanhuan)
    def type_number(x):
        x = int(x)
        if x <= 10000:
            return 1
        elif 10000 < x <= 20000:
            return 2
        elif 20000 < x <= 50000:
            return 3
        elif 50000 < x <= 100000:
            return 4
        else:
            return 5
    df['观看量类型'] = df['观看量'].apply(type_number)
    new_df = df['观看量类型'].value_counts()
    x_data = ['1w以下','1w-2w','2w-5w','5w-10w','10w以上']
    y_data = [int(y) for y in new_df.values]
    c = (
        Line({"theme": ThemeType.MACARONS})
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#5DADE2",
            y_axis=y_data,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )

            .set_global_opts(
            title_opts=opts.TitleOpts(title="观看量状况", pos_left="center", pos_top="20"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False, axisline_opts=opts.AxisLineOpts(
                is_on_zero=False,
            )),
        )
    )
    return c


