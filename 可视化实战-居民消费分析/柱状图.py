import pandas as pd
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar
import pyecharts.options as opts

df = pd.read_excel('居民消费价-数据.xlsx').loc[:,['地区','平均值']]

area_list = []
average_list = []

for a in df['地区']:
    area_list.append(a)

for ave in df['平均值']:
    average_list.append(ave)

c = (
    Bar(init_opts=opts.InitOpts(width="1300px", height="600px",theme=ThemeType.MACARONS))
    .add_xaxis(area_list)
    .add_yaxis("平均值", average_list,label_opts=opts.LabelOpts(is_show=False))

    .set_global_opts(
        title_opts={"text": "各地区平均值"}
    )
    .render("bar.html")
)
