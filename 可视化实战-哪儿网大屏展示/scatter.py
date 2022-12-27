from pyecharts import options as opts
from pyecharts.charts import Scatter
import pandas as pd
from pyecharts.globals import ThemeType

def main_scatter():
    df = pd.read_csv('data.csv')

    list1 = {}
    for i in df['游玩方式']:
        i = str(i).replace('\xa0','').split(' ')
        for d in i:
            list1[d] = list1.get(d,0)+1

    ls = list(list1.items())
    ls.sort(key=lambda x:x[1],reverse=True)
    ls = ls[1:]

    key = []
    values = []
    for k,v in ls:
        key.append(k)
        values.append(v)

    c = (
        Scatter({"theme": ThemeType.MACARONS})
        .add_xaxis(key[:10])
        .add_yaxis("", values[:10])
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
            title_opts=opts.TitleOpts(title="TOP10-游玩方式", pos_left="center",pos_top="20"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=70, min_=0),
        )
    )

    return c