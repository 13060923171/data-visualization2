from pyecharts.charts import WordCloud
from pyecharts.charts import Geo
from pyecharts.charts import Line,Pie,Page
from pyecharts.globals import CurrentConfig,ThemeType
import pandas as pd
from pyecharts.charts import Bar, Geo, Grid
from pyecharts import options as opts
from pyecharts.charts import Geo

df = pd.read_excel('python_lagou.xlsx').loc[:, ['city', 'salary', 'education', 'positionAdvantage']]

salary = ['16','13.5','14.5','11','9','14','9.6','11','12','9']
company = ['北京','深圳','上海','广州','成都','杭州','武汉','南京','厦门','西安']

a = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(company)
    .add_yaxis("一线城市平均工资", salary)
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        title_opts=opts.TitleOpts(title="一线城市平均工资"),
        yaxis_opts=opts.AxisOpts(
            name="平均工资",
            type_="value",
            min_=0,
            max_=20,
            interval=5,
            axislabel_opts=opts.LabelOpts(formatter="{value}k"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
)


df1 = df['city']
data = df1.value_counts()
data_pair_1 = [(i, int(j)) for i, j in zip(data.index, data.values)]
# print(data_pair_1)
y_data = [i for i in data.index]
y_list = [3216, 2310, 1966, 1649, 868, 827, 427, 118, 94, 90]
b = (
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
        series_name="人才渴望度最高的十个城市",
        y_axis=y_list,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=True),
    )
)



df2 = df['salary']
list_float = []
try:
    for i in df2:
        i = str(i)
        if 'k' not in i:
            list_float.append(i)
except:
    pass
df3 = df[-df.salary.isin(list_float)]
df4 = df['city']
list_city = []
for j in df4:
    j = str(j)
    if len(j) >3:
        list_city.append(j)
df5 = df3[-df3.salary.isin(['有挑战性','1，负责课程咨询及招生工作，完', '无办公室政治', '每年涨薪制度', '互联网行业', '齐齐哈尔', '周末双休', '沟通能力好'])]
data = df5['city'].value_counts()
data_pair_1 = [(i, int(j)) for i, j in zip(data.index,data.values)]
data1 = [("江苏", 99), ("广东", 3420), ("山东", 36), ("河南", 83), ("湖北", 366), ("四川", 52), ("湖南", 70), ("河北",
    61), ("安徽", 57), ("辽宁", 64), ("浙江", 708), ("江西", 15), ("陕西", 74), ("北京", 2789), ("福建", 85),
    ("山西",33),("云南",32),("黑龙江",39),("广西",38),("贵州",29),("重庆",54),("上海",1710),("吉林",37),
    ("天津",24),("新疆",18),("内蒙古",17),("甘肃",22),("海南",8),("宁夏",8),("青海",4),("西藏",4)]

c = (
    Geo()
        .add_schema(maptype="china")
        .add("", data1)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(is_piecewise=True,min_=0,max_=4000),
        title_opts=opts.TitleOpts(title="招聘热度"),
    )
)



df9 = df['education']
data3 = df9.value_counts()
xueli = ['本科', '大专', '不限', '硕士 ', '博士']
shuju = ['8248', '2589', '1162', '376', '19']
data_pair_3 = [(str(i), int(j)) for i, j in zip(xueli, shuju)]
d = (
    Pie(init_opts=opts.InitOpts(theme="学历占比情况"))
    .add(
        "",
        data_pair_3,
        label_opts=opts.LabelOpts(is_show=True)
    )
    .set_colors(['red', 'blue', 'green', 'yellow', 'purple'])
    .set_global_opts(title_opts=opts.TitleOpts(title="学历占比情况"),
                         legend_opts=opts.LegendOpts(is_show=False))
)



df10 = df['positionAdvantage']
data = df10.value_counts()
data_pair_4 = [(i, int(j)) for i, j in zip(data.index, data.values)]
data_pair1 = data_pair_4[:50]
e = (
    WordCloud()
        .add(series_name="福利频次", data_pair=data_pair1, word_size_range=[6, 66])
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title="福利频次", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
)


page = (
    Page(layout=Page.DraggablePageLayout)
    .add(a,b,c,d,e)
    .save_resize_html(cfg_file="chart_config.json")
)

