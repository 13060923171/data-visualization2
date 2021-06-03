import pyecharts.options as opts
from pyecharts.charts import WordCloud
import pandas as pd

df = pd.read_excel('python_lagou.xlsx').loc[:,['positionAdvantage']]
df1 = df['positionAdvantage']
data = df1.value_counts()

data_pair_1 = [(i, int(j)) for i, j in zip(data.index,data.values)]
data_pair = data_pair_1[:50]

w = (
    WordCloud()
    .add(series_name="福利最高频次的词云", data_pair=data_pair, word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="福利最高频次的词云", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("basic_wordcloud.html")
)