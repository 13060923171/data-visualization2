import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.charts import Bar
from pyecharts.faker import Faker
df = pd.read_csv('./csv_file/主要污染物.csv',encoding='gbk').loc[:,['污染物','数值']]
df.dropna(axis=0,how='any',inplace=True)
df[df.isnull().T.any()]

x_data = []
for i in df['污染物']:
    x_data.append(i)

y_data = []
for i in df['数值']:
    i = int(i)
    y_data.append(i)

c = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis("污染物", y_data)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="主要污染物程度等级，颜色越深说明越严重"),
        toolbox_opts=opts.ToolboxOpts(),
        visualmap_opts=opts.VisualMapOpts(
            range_color=["GreenYellow", "LemonChiffon", "LightSalmon","HotPink","Red","Purple"],
            min_=0,
            max_=500
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .render("bar_toolbox.html")
)