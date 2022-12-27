import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.globals import ThemeType


def main_funnel():
    df = pd.read_csv('data.csv')
    new_df = df['游玩人数'].value_counts()

    x_data = [str(x) for x in new_df.index]
    y_data = [int(y) for y in new_df.values]
    del x_data[1]
    del y_data[1]

    c = (
        Funnel({"theme": ThemeType.MACARONS})
            .add("", [list(z) for z in zip(x_data, y_data)])
            .set_global_opts(title_opts=opts.TitleOpts(title="游玩人数类型分布", pos_left="center",pos_top="20"))
    )
    return c
