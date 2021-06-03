import pandas as pd

import pyecharts.options as opts
from pyecharts.charts import Pie
df = pd.read_excel('iPhone数据.xlsx',sheet_name='摄像头').loc[:,['摄像头']]

#通过Pandas库来读取数据
list1 = []
for d in df['摄像头']:
    d = d.split(' ')
    for i in d:
        list1.append(i)
d = {}
#创建一个字典去读取这个词出现的频率
for j in list1:
    d[j] = d.get(j,0)+1
ls = list(d.items())
#将列表从大到小进行排序
ls.sort(key=lambda x:x[1],reverse=True)

(
    #创建饼图的大小和主题
    Pie(init_opts=opts.InitOpts(width="1280px", height="620px", bg_color="#2c343c"))
    .add(
        #饼图的一些参数内容和位置
        series_name="摄像头参数",
        data_pair=ls,
        rosetype="radius",
        radius="55%",
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    #饼图标题的参数和颜色
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="摄像头参数",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    #饼图文字的大小和形式
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    .render("iPhone-pie.html")
)

