import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line

df = pd.read_excel('python_lagou.xlsx').loc[:,['city']]
df1 = df['city']
data = df1.value_counts()
data_pair_1 = [(i, int(j)) for i, j in zip(data.index,data.values)]
# print(data_pair_1)
x_data = [i for i in data.values]
y_data = [i for i in data.index]
y_list = [3216, 2310, 1966, 1649, 868, 827, 427, 118, 94, 90]

a = (
    Line()
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(xaxis_data=y_data[:10])
    .add_yaxis(
        series_name="对人才渴望度最高的十个城市",
        y_axis=y_list,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=True),
    )
    .render("Line.html")
)