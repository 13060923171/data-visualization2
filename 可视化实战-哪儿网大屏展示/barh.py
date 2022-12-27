import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

def main_barh():
    df = pd.read_csv('data.csv')
    def zhuanhuna(x):
        x1 = str(x).split('-')
        x1 = str(x1[0]) + "-" + str(x1[1])
        return x1

    df['出发时间'] = df['出发时间'].apply(zhuanhuna)
    new_df = df['出发时间'].value_counts()

    x_data = [str(x) for x in new_df.index]
    y_data = [int(y) for y in new_df.values]

    x_data1 = x_data[:10]
    y_data1 = y_data[:10]
    x_data1.reverse()
    y_data1.reverse()

    c = (
        Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(x_data1)
            .add_yaxis("", y_data1)
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="TOP10-出游最多的月份", pos_left="center", pos_top="20")
        )
    )
    return c