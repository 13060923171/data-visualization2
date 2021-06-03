import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line

df = pd.read_csv('./csv_file/未来15天的天气状况.csv',encoding='gbk').loc[:,['时间','温度','等级','风力等级']]
df.dropna(axis=0,how='any',inplace=True)
df[df.isnull().T.any()]

list_data = []
for i in df['时间']:
    i = str(i)
    i = i[4:-1]
    list_data.append(i)

list_wendu_high = []
list_wendu_low = []
for i in df['温度']:
    i = i.replace('℃','')
    i = i.split('/')
    list_wendu_low.append(int(i[0]))
    list_wendu_high.append(int(i[1]))

c = (
    Line(init_opts=opts.InitOpts(width="1300px", height="600px"))
    .add_xaxis(xaxis_data=list_data)
    .add_yaxis(
        series_name="温度最低温走势",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#d14a61",
        y_axis=list_wendu_low,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=5)
    )
    .add_yaxis(
        series_name="温度最高温走势",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#6e9ef1",
        y_axis=list_wendu_high,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=5)
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="未来15天气的状况"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,axisline_opts=opts.AxisLineOpts(
                is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            )),
    )
    .render("天气.html")
)


