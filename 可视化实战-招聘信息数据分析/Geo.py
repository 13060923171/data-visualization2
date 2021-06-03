from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker

import pandas as pd

df = pd.read_excel('python_lagou.xlsx').loc[:,['city','salary']]

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
        .add("geo", data1)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(is_piecewise=True,min_=0,max_=4000),
        title_opts=opts.TitleOpts(title="招聘热度"),
    )
    .render("Geo.html")
)
