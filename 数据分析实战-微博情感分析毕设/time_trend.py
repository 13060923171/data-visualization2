import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

data1 = pd.read_excel('./data/数据(1).xlsx')
data2 = pd.read_excel('./data/数据(2).xlsx')
data3 = pd.read_excel('./data/数据(3).xlsx')
data4 = pd.read_excel('./data/数据(4).xlsx')
data5 = pd.read_excel('./data/数据(5).xlsx')
data6 = pd.read_excel('./data/数据(6).xlsx')
data7 = pd.read_excel('./data/数据(7).xlsx')
data8 = pd.read_excel('./data/数据(8).xlsx')
sum_data = pd.concat([data1,data2,data3,data4,data5,data6,data7,data8])


def get_line():
    def time_split(x):
        x = str(x)
        x = x.split(" ")
        x = x[0]
        return x

    sum_data['create_time'] = sum_data['create_time'].apply(time_split)
    df2 = sum_data['create_time'].value_counts()
    df3 = pd.DataFrame()
    df3['time'] = df2.index
    df3['count'] = df2.values
    df3.sort_values(by=['time'], ascending=True, inplace=True)

    x_data = list(df3['time'])
    y_data = list(df3['count'])

    c = (

        Line(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#ADFF2F",
            y_axis=y_data,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="时间趋势"),
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


def get_bar():
    sum_data.dropna(how='any', inplace=True)
    x_data = sum_data['commentor_name']
    y_data = sum_data['like_count']

    data_pair2 = [(x, int(y)) for x, y in zip(x_data, y_data)]
    data_pair2.sort(key=lambda x: x[1], reverse=True)

    data_pair3 = list(set(data_pair2))
    data_pair3.sort(key=lambda x: x[1], reverse=True)

    x_data1 = []
    y_data1 = []
    for k, j in data_pair3[0:20]:
        x_data1.append(k)
        y_data1.append(j)

    x_data1.reverse()
    y_data1.reverse()
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
            .add_xaxis(x_data1)
            .add_yaxis("", y_data1, label_opts=opts.LabelOpts(is_show=False))
            .reversal_axis()
            .set_global_opts(
            title_opts={"text": "前20影响力最大的人"}
        )
    )
    return c

