import requests
import json
import re
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Map
from pyecharts import options
from pyecharts.charts import Bar,Pie


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
    number = province['value']
    number = int(number)
    province_data.append((province['name'], number))
city = []
confirmed_number = []
province_data.sort(key=lambda x:x[1],reverse=False)



def map1():
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
        .render('map.html')
    )



def bar1():
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
        .render('bar.html')
    )

def pie1():
    econNum_data1 = []
    econNum_data2 = []
    for province in table['data']['list']:
        number = province['econNum']
        number = int(number)
        name = province['name']
        if name == '台湾' or name == '香港' or name == '澳门':
            econNum_data1.append(number)
        else:
            econNum_data2.append(number)

    x_data = ['港澳台病例', '31省本土病例']
    y_data = [sum(econNum_data1), sum(econNum_data2)]
    data_pair = [(i, int(j)) for i, j in zip(x_data, y_data)]
    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
            .add(
            "占比",
            data_pair,
            center=['50%', '50%'],
            label_opts=opts.LabelOpts(is_show=True)
        )
            .set_colors(['SteelBlue', 'DarkCyan', 'DarkOrange', 'Salmon'])
            .set_global_opts(title_opts=opts.TitleOpts(title="全国现有确诊构成", pos_left="center",
                                                       pos_top="top", ), legend_opts=opts.LegendOpts(is_show=False))
            .set_series_opts(tooltip_opts=opts.TooltipOpts(trigger='item', formatter="{a} <br/>{b}-{c}:<br/>{d}%"))
        .render('pie.html')
    )


if __name__ == '__main__':
    map1()
    bar1()
    pie1()

