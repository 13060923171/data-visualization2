import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie

# df = pd.read_csv('NIKE 510.csv').loc[:,['是否广告']]
# df = df['是否广告'].value_counts()
df = pd.read_csv('NIKE 510.csv').loc[:,['价格','评价人数']]


list_500 = []
list_1000 = []
list_1500 = []
list_2000 = []
list_2500 = []
list_3000 = []
for i in range(len(df['价格'])):
    if int(df['价格'][i]) <= int(500):
        list_500.append(df['价格'][i])
    if int(500) < int(df['价格'][i]) <= int(1000):
        list_1000.append(df['价格'][i])
    if int(1000) < int(df['价格'][i]) <= int(1500):
        list_1500.append(df['价格'][i])
    if int(1500) < int(df['价格'][i]) <= int(2000):
        list_2000.append(df['价格'][i])
    if int(2000) < int(df['价格'][i]) <= int(2500):
        list_2500.append(df['价格'][i])
    if int(df['价格'][i]) > int(2500):
        list_3000.append(df['价格'][i])

data_pair_1 = [('0-500','256'),('500-1000','179'),('1000-1500','52'),('1500-2000','9'),('2000-2500','5'),('2500以上','9')]

c = (
    Pie(init_opts=opts.InitOpts(width="1100px",height='500px'))
    .add(
        "",
        data_pair_1,
        center=['50%','50%'],
        label_opts=opts.LabelOpts(is_show=True)
    )
    .set_colors(['MediumPurple','Thistle','Plum','Violet','Orchid','Fuchsia'])
    .set_global_opts(title_opts=opts.TitleOpts(title="价格区间占比图"),legend_opts=opts.LegendOpts(is_show=False))
    .set_series_opts(tooltip_opts=opts.TooltipOpts(trigger='item',formatter="{a} <br/>{b}: {c} ({d}%)"))
    .render("pie_.html")
)