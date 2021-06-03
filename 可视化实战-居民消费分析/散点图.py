import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

df = pd.read_excel('居民消费价-数据.xlsx')

beijing_list = []
for i in df.iloc[0][1:]:
    beijing_list.append(i)

shanghai_list = []
for i in df.iloc[8][1:]:
    shanghai_list.append(i)

guangdong_list = []
for i in df.iloc[18][1:]:
    guangdong_list.append(i)

chongqing_list = []
for i in df.iloc[21][1:]:
    chongqing_list.append(i)

zhejian_list = []
for i in df.iloc[10][1:]:
    zhejian_list.append(i)

hunan_list = []
for i in df.iloc[17][1:]:
    hunan_list.append(i)

hubei_list = []
for i in df.iloc[16][1:]:
    hubei_list.append(i)

x_data = ['2019.11','2019.12','2020.01','2020.02','2020.03','2020.04','2020.05','2020.06','2020.07','2020.08','2020.09','2020.10','2020.11']

c = (
    Scatter(init_opts=opts.InitOpts(width="1300px", height="600px",theme=ThemeType.VINTAGE))
    .add_xaxis(x_data)
    .add_yaxis("北京", beijing_list)
    .add_yaxis("广东", guangdong_list)
    .add_yaxis("上海", shanghai_list)
    .add_yaxis("浙江", zhejian_list)
    .add_yaxis("重庆", chongqing_list)
    .add_yaxis("湖南", hunan_list)
    .add_yaxis("湖北", hubei_list)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="热门省份-散点图"),
        visualmap_opts=opts.VisualMapOpts(type_="size", max_=110, min_=95),
        yaxis_opts=opts.AxisOpts(
                    type_="value",
                    min_=98.5,
                    max_=107.5,
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
    )
    .render("scatter.html")
)