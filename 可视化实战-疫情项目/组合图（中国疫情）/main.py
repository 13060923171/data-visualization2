import requests
import json
import re
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Map
from pyecharts import options
from pyecharts.charts import Bar,Page
#先请求到数据的页面
result = requests.get(
    'https://interface.sina.cn/news/wap/fymap2020_data.d.json?1580097300739&&callback=sinajp_1580097300873005379567841634181')
#用正则去获取具体的数字
json_str = re.search("\(+([^)]*)\)+", result.text).group(1)
html = f"{json_str}"
#然后用json把json转化为python
table = json.loads(f"{html}")
province_data = []
for province in table['data']['list']:
    province_data.append((province['name'], province['value']))



map = (
    Map()
    .set_global_opts(title_opts=options.TitleOpts(
        title="全国确诊人数：" + str(table['data']["gntotal"])),

        visualmap_opts=options.VisualMapOpts(is_piecewise=True,  # 设置是否为分段显示
                                         # 自定义数据范围和对应的颜色，这里我是取色工具获取的颜色值，不容易呀。
                                         pieces=[
                                             # 不指定 max，表示 max 为无限大（Infinity）。
                                             {"min": 1000, "label": '>1000',
                                              "color": "#6F171F"},
                                             {"min": 500, "max": 1000,
                                              "label": '500-1000', "color": "#C92C34"},
                                             {"min": 100, "max": 499,
                                              "label": '100-499', "color": "#E35B52"},
                                             {"min": 10, "max": 99,
                                              "label": '10-99', "color": "#F39E86"},
                                             {"min": 1, "max": 9, "label": '1-9', "color": "#FDEBD0"}]
                                             ))
    .add("确诊人数：", province_data, maptype="china",itemstyle_opts={"emphasis":{"areaColor": "rgba(0,0,0, 1)"}})
)

city = []
confirmed_number = []
for p in province_data:
    city.append(p[0])
    confirmed_number.append(p[1])
bar = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(city)
    .add_yaxis("city", confirmed_number)
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(title_opts=opts.TitleOpts(title="城市疫情数量排名"))
    .set_global_opts(legend_opts=opts.LegendOpts(pos_left="20%"))
)

page = (
    #布局管理器会自动寻找最佳的布局方案并给与适当的间隔
    # Page(layout=Page.SimplePageLayout)
    #布局管理器可以拖拽
    Page(layout=Page.DraggablePageLayout)
    .add(bar,map)
    .save_resize_html(cfg_file="chart_config.json")
)
