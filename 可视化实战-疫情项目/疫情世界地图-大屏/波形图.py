import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line

df = pd.read_excel('data.xlsx').loc[:,['Country','Month','Number']]

x_data = []
y_Australia = []
y_Canada = []
y_United_Kingdom = []
y_United_States_of_America = []
y_China = []

for i in df['Month'][0:10]:
    i = str(i)
    x_data.append(i)
for a in df['Number'][0:10]:
    y_Australia.append(a)

for c in df['Number'][10:20]:
    y_Canada.append(c)

for u_k in df['Number'][20:30]:
    y_United_Kingdom.append(u_k)

for u_s_a in df['Number'][30:40]:
    y_United_States_of_America.append(u_s_a)

for c_a in df['Number'][40:50]:
    y_China.append(c_a)



c = (
    Line(init_opts=opts.InitOpts(width="700px", height="350px"))
    .add_xaxis(x_data)
    .add_yaxis("Australia",y_Australia, is_smooth=True,color="#ADD8E6",symbol="emptyCircle")
    .add_yaxis("Canada", y_Canada, is_smooth=True,color="#008080",symbol="emptyCircle")
    .add_yaxis("United-Kingdom", y_United_Kingdom, is_smooth=True,color="#7CFC00",symbol="emptyCircle")
    .add_yaxis("United-States-of-America", y_United_States_of_America, is_smooth=True,color="#00FFFF",symbol="emptyCircle")
    .add_yaxis("China", y_China, is_smooth=True,color="#A9A9A9",symbol="emptyCircle")
    .set_series_opts(
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="确诊人数波形图", pos_left="35%", pos_top="5%"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
            is_scale=False,
            boundary_gap=False,
        ),
    )
    .render("line.html")
)

