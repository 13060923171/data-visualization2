import requests
import json
import re
import pandas as pd
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Map
from pyecharts import options
from pyecharts.charts import Bar,Pie


df = pd.DataFrame()
df['省份'] = ['省份']
df['累积确诊'] = ['累积确诊']
df['现存确诊'] = ['现存确诊']
df['死亡'] = ['死亡']
df['治愈'] = ['治愈']
df.to_csv('data.csv',encoding='utf-8-sig',header=False,mode='w',index=False)
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
    #累积确诊数量
    number = int(province['value'])
    #省份名字
    name = province['name']
    #现存确诊
    econNum = int(province['econNum'])
    #死亡人数
    deathNum = int(province['deathNum'])
    #治愈人数
    cureNum = int(province['cureNum'])
    df['省份'] = [name]
    df['现存确诊'] = [econNum]
    df['累积确诊'] = [number]
    df['死亡'] = [deathNum]
    df['治愈'] = [cureNum]
    df.to_csv('data.csv', encoding='utf-8-sig', header=False, mode='a+',index=False)
    province_data.append((province['name'], number))
city = []
confirmed_number = []
province_data.sort(key=lambda x:x[1],reverse=False)


#中国地图绘制
def map1():
    map = (
        Map()
            .set_global_opts(title_opts=options.TitleOpts(
            title="全国累计确诊人数：" + str(table['data']["gntotal"])),

            visualmap_opts=options.VisualMapOpts(is_piecewise=True,  # 设置是否为分段显示
                                                 # 自定义数据范围和对应的颜色，这里我是取色工具获取的颜色值，不容易呀。
                                                 pieces=[
                                                     # 不指定 max，表示 max 为无限大（Infinity）。
                                                     {"min": 20000, "label": '>20000',
                                                      "color": "#6F171F"},
                                                     {"min": 10000, "max": 20000,
                                                      "label": '10000-20000', "color": "#C92C34"},
                                                     {"min": 5000, "max": 10000,
                                                      "label": '5000-10000', "color": "#E35B52"},
                                                     {"min": 1000, "max": 5000,
                                                      "label": '1000-5000', "color": "#F39E86"},
                                                     {"min": 100, "max": 1000, "label": '100-1000', "color": "#FDEBD0"}]
                                                 ))
            .add("累积确诊人数：", province_data, maptype="china",itemstyle_opts={"emphasis":{"areaColor": "rgba(0,0,0, 1)"}})
            .render('map.html')
    )


#柱状图绘制
def bar1():
    #数据获取
    for p in province_data:
        city.append(p[0])
        confirmed_number.append(p[1])
    bar = (
        Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(city)
            .add_yaxis("city", confirmed_number)
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="累积确诊-城市排名"))
            .render('bar.html')
    )

#饼图绘制
def pie1():
    #数据整理
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

    x_data = ['港澳台病例', '其他省本土病例']
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

