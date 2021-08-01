import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

df = pd.read_excel('dates.xls').loc[35:41,['2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']]
df.fillna(value=df.mean(),inplace=True)

x_data = [str(i) for i in range(2009,2020)]
list_dalian = [int(i) for i in df.iloc[0]]
list_shenyang = [int(i) for i in df.iloc[1]]
list_changchun = [int(i) for i in df.iloc[2]]
list_haerbin = [int(i) for i in df.iloc[3]]
list_qingdao = [int(i) for i in df.iloc[4]]
list_xiamen = [int(i) for i in df.iloc[5]]
list_shenzhen = [int(i) for i in df.iloc[6]]

c = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis("大连", list_dalian , stack="stack1")
    .add_yaxis("沈阳", list_shenyang, stack="stack1")
    .add_yaxis("长春", list_changchun, stack="stack1")
    .add_yaxis("哈尔滨", list_haerbin, stack="stack1")
    .add_yaxis("青岛", list_qingdao, stack="stack1")
    .add_yaxis("厦门", list_xiamen, stack="stack1")
    .add_yaxis("深圳", list_shenzhen, stack="stack1")

    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="合同利用外资项目数_外商直接投资_市辖区"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name="个",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .render("bar_stack0.html")
)