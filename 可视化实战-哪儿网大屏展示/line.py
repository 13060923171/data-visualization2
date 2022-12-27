import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

def main_line():
    df = pd.read_csv('data.csv')
    def test(x):
        x1 = str(x)
        if x1 != ' ':
            return x1
        else:
            return np.NaN

    df['费用'] = df['费用'].apply(test)
    df = df.dropna(subset=['费用'],axis=0)

    def zhuanhuan(x):
        x1 = str(x)
        x1 = x1.replace('人均','').replace('元','')
        x2 = int(x1)
        if x2 <= 500:
            return 1
        elif 500 < x2 <= 1000:
            return 2
        elif 1000 < x2 <= 3000:
            return 3
        elif 3000 < x2 <= 5000:
            return 4
        elif 5000 < x2 <= 8000:
            return 5
        elif 8000 < x2 <= 10000:
            return 6
        else:
            return 7


    df['费用'] = df['费用'].apply(zhuanhuan)
    new_df = df['费用'].value_counts()
    new_df = new_df.sort_index()
    x_data = ['500以下','500-1k', '1k-3k','3k-5k','5k-8k','8k-1w', '1w以上']
    y_data = [int(y) for y in new_df.values]

    c = (
        Pie({"theme": ThemeType.MACARONS})
            .add(
            "",
            [list(z) for z in zip(x_data,y_data)],
            radius=["30%", "75%"],
            center=["50%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="人均消费水平分布状况", pos_left="center",pos_top="20"))
    )
    return c