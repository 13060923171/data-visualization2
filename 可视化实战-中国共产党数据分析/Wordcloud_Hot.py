import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
import jieba
df = pd.read_excel('./数据/中共信息.xls').loc[:,['时间','内容']]


comment_list = []
for i in df['内容']:
    i = str(i)
    comment_list.append(i)

stop_words = []
with open("./数据/stopwords_cn.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        stop_words.append(line.strip())
word1 = []
for i in range(0,100):
    i = str(i)
    word1.append(i)
    stop_words.extend(word1)
d = {}
for s in comment_list:
    fenchi = jieba.lcut(s,cut_all=False)
    for f in fenchi:
        if f not in stop_words and len(f) >=2:
            d[f] = d.get(f, 0) + 1
ls = list(d.items())
ls.sort(key=lambda x: x[1], reverse=True)


def wordcloud_hot():
    c = (
            WordCloud(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
            .add(
                    "",
                    ls,
                    word_size_range=[20, 100],
                    shape=SymbolType.DIAMOND,
                    textstyle_opts=opts.TextStyleOpts(font_family="cursive"), )
            .set_global_opts(title_opts=opts.TitleOpts(
                title="党的热词分析",
                pos_left="center",
                pos_top="top"
            ))
        )
    return c