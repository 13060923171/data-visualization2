import pandas as pd
import re
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
from pyecharts.globals import ThemeType

def main_word():
    df = pd.read_csv('data.csv')
    def zhuanhuan(x):
        x1 = str(x)
        x1 = x1.replace('途经：','')
        return x1

    df['途径'] = df['途径'].apply(zhuanhuan)

    dit1 = {}
    for d in df['途径']:
        d1 = str(d)
        strinfo = re.compile('\(.*?\)')
        d2 = strinfo.sub(' ', d1)
        strinfo1 = re.compile('\(.*?... ')
        d3 = strinfo1.sub(' ', d2)
        strinfo2 = re.compile('[a-zA-Z]')
        d4 = strinfo2.sub(' ', d3)
        d5 = d4.strip(' ').replace('.','')
        d5 = d5.split(' ')
        for i in d5:
            dit1[i] = dit1.get(i,0)+1

    ls = list(dit1.items())
    ls.sort(key=lambda x:x[1],reverse=True)
    ls = ls[1:51]

    c = (
        WordCloud({"theme": ThemeType.MACARONS})
            .add("", ls, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="热门旅游地区", pos_left="center",pos_top="20"))
    )

    return c