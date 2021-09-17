import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

#获取到数据
df = pd.read_excel('数据.xls').loc[:,['工作地点']]
list_city = []
d = {}
#对数据进行清洗
for c in df['工作地点']:
    c = str(c)
    c = c[0:2]
    c = c.replace('石家', '石家庄').replace('哈尔', '黑龙江').replace('广东', '广州')
    list_city.append(c)

#获取到每个城市出现的总的次数
for c in list_city:
    d[c] = d.get(c,0) +1
list1 = list(d.items())

#生成中国地图
def get_city():
    c = (
        Geo()
        #设定地图的范围
        .add_schema(
            maptype="china",
            #地图的背景
            itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
        )
        .add(
            "",
            list1,
            #数据呈现的类型
            type_=ChartType.EFFECT_SCATTER,
            #类型的颜色
            color="white",

        )
        #是否显示数值
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        #标题
        .set_global_opts(title_opts=opts.TitleOpts(title="热门城市"))
    )
    return c

