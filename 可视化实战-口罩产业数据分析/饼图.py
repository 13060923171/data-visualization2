import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie

df = pd.read_excel('口罩产业.xlsx',sheet_name='Sheet2').loc[0:3,['2019年口罩产业产值结构情况（单位：%）','Unnamed: 1']]
x_data = []
y_data = []

for x in df['2019年口罩产业产值结构情况（单位：%）']:
    x_data.append(x)


for y in df['Unnamed: 1']:
    y = int(y*100)
    y_data.append(y)

data_pair_1 = [(i, int(j)) for i, j in zip(x_data, y_data)]

c = (
    Pie(init_opts=opts.InitOpts(width="1100px",height='500px'))
    .add(
        "",
        data_pair_1,
        center=['25%','50%'],
        label_opts=opts.LabelOpts(is_show=True)
    )
    .set_colors(['SteelBlue','DarkCyan','DarkOrange','Salmon'])
    .set_global_opts(title_opts=opts.TitleOpts(title="2019年口罩产业产值结构情况(单位：%)"),legend_opts=opts.LegendOpts(is_show=False))
    .set_series_opts(tooltip_opts=opts.TooltipOpts(trigger='item',formatter="{a} <br/>{b}:{d}%"))
    .render("pie_.html")
)