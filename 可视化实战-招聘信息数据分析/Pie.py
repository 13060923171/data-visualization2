import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Bar,Pie
from pyecharts.globals import CurrentConfig,ThemeType
df = pd.read_excel('python_lagou.xlsx').loc[:,['city','salary','education']]
df1 = df['education']
data = df1.value_counts()
xueli = ['本科','大专','不限','硕士 ','博士']
shuju = ['8248','2589','1162','376','19']
data_pair_1 = [(str(i), int(j)) for i, j in zip(xueli, shuju)]
c = (
    Pie(init_opts=opts.InitOpts(theme="学历占比情况",width="1100px",height='500px'))
    .add(
        "学历占比情况",
        data_pair_1,
        center=['25%','50%'],
        label_opts=opts.LabelOpts(is_show=True)
    )
    .set_colors(['red','blue','green','yellow','purple'])
    .set_global_opts(title_opts=opts.TitleOpts(title="土地出让形式&土地成交状态占比"),legend_opts=opts.LegendOpts(is_show=False))
    .render("pie_.html")
)