import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType


def main_bar():
    df = pd.read_csv('data.csv')
    new_df = df['逗留时间'].value_counts()
    x_data = [str(x).replace('共','') for x in new_df.index]
    y_data = [int(y) for y in new_df.values]

    c = (
        Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(x_data[0:10])
            .add_yaxis("", y_data[0:10])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="TOP10-逗留时长", pos_left="center",pos_top="20")
        )
    )

    return c