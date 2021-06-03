import pandas as pd

from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import WordCloud
import jieba
df = pd.read_csv('NIKE 510.csv').loc[:,['商品名称']]
d = {}

for i in df['商品名称']:
    i = i.replace('【','').replace('】','').replace("，","").replace("。","").replace("‘","").replace("：","").replace(" ","").replace("\n","").replace("-","").replace("/","")
    fenchi = jieba.lcut(i)
    for fen in fenchi:
        d[fen] = d.get(fen,0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)


(
    WordCloud(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
    .add(series_name="标题-热词", data_pair=ls, word_size_range=[8, 88])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="标题-热词", title_textstyle_opts=opts.TextStyleOpts(font_size=32)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("wordcloud_.html")
)