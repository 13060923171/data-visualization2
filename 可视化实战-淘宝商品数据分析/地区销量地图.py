import pandas as pd
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType
from pyecharts.commons.utils import JsCode

df = pd.read_excel('商品的基本信息.xlsx')

deal_list = []
for d in df['付款人数']:
    d = str(d)
    d = d.replace('(','').replace(')','').replace(',','').replace("'","").\
        replace('人','').replace('付款','').replace('万','0000').replace('.0','').replace('+','').replace('1.50000','15000')
    d = d.replace('\n','0')
    deal_list.append(d)


location_list = []
for l in df['发货地址']:
    l = str(l)
    l = l.replace('(','').replace(')','').replace(',','').replace("'","")
    l = l[0:2]
    location_list.append(l)



price_hubei = []
price_zhejian = []
price_beijing = []
price_tianjian = []
price_guangdong = []
price_anhui = []
price_fujian = []
price_hebei = []
price_jianshu = []
price_shanghai = []
for i in range(len(location_list)):
    if '湖北' in location_list[i]:
        hubei_price = int(deal_list[i])
        price_hubei.append(hubei_price)
    if '浙江' in location_list[i]:
        zhejian_price = int(deal_list[i])
        price_zhejian.append(zhejian_price)
    if '北京' in location_list[i]:
        beijing_price = int(deal_list[i])
        price_beijing.append(beijing_price)
    if '天津' in location_list[i]:
        tianjin_price = int(deal_list[i])
        price_tianjian.append(tianjin_price)
    if '广东' in location_list[i]:
        guangdong_price = int(deal_list[i])
        price_guangdong.append(guangdong_price)
    if '安徽' in location_list[i]:
        anhui_price = int(deal_list[i])
        price_anhui.append(anhui_price)
    if '福建' in location_list[i]:
        fujian_price = int(deal_list[i])
        price_fujian.append(fujian_price)
    if '河北' in location_list[i]:
        hebei_price = int(deal_list[i])
        price_hebei.append(hebei_price)
    if '江苏' in location_list[i]:
        jiangsu_price = int(deal_list[i])
        price_jianshu.append(jiangsu_price)
    if '上海' in location_list[i]:
        shanghai_price = deal_list[i]
        price_shanghai.append(shanghai_price)



#湖北
price_hubei_sum = sum(price_hubei)
print(price_hubei_sum)

#浙江
price_zhejian_sum = sum(price_zhejian)
print(price_zhejian_sum)

#北京
price_beijing_sum = sum(price_beijing)
print(price_beijing_sum)

#天津
price_tianjian_sum = sum(price_tianjian)
print(price_tianjian_sum)

#广东
price_guangdong_sum = sum(price_guangdong)
print(price_guangdong_sum)

#安徽
price_anhui_sum = sum(price_anhui)
print(price_anhui_sum)

#福建
price_fujian_sum = sum(price_fujian)
print(price_fujian_sum)

#河北
price_hebei_sum = sum(price_hebei)
print(price_hebei_sum)

#江苏
price_jianshu_sum = sum(price_jianshu)
print(price_jianshu_sum)

#上海
for p in price_shanghai:
    p = str(p)
    if p == '':
        price_shanghai.remove('')
    if p ==  '':
        price_shanghai.remove( '')

sum_shanghai = 0
for i in price_shanghai:
    i = int(i)
    sum_shanghai += i
print(sum_shanghai)

city_list = ['湖北','浙江','北京','天津','广东','安徽','福建','河北','江苏','上海']
price_sum = ['5325','310896','61341','12731','224823','2397','54415','3915','142673','165253']

data_pair_1 = [(i, int(j)) for i, j in zip(city_list, price_sum)]
data_pair_1 = sorted(data_pair_1,key=lambda x: x[1])

def genGeo(data):
    c = (
        Map(init_opts=opts.InitOpts(
            width='1300px',
            height='700px',
            bg_color='#0F1C3C',
        ))
        .add(  # 添加散点图
            "",
            data,
            label_opts=opts.LabelOpts(
                is_show=True,
                color="#00f",
                border_width=2.,
                font_size=18,
                position="inside",
                # formatter=JsCode(
                #     """
                #     function f(param){
                #         return param.name + ','+ param.value[1]
                #     }
                #     """
                # ),
            )
        )
        .set_series_opts(
            range_size=[12, 40],
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=1.0,
                border_color='#215495',
            ),
            areastyle_opts=opts.AreaStyleOpts(
                color={
                    "x": 0,
                    "y": 0,
                    "x2": 0,
                    "y2": 1,
                    "colorStops": [{
                        "offset": 0,
                        "color": '#073684'
                    }, {
                        "offset": 1,
                        "color": '#061E3D'
                    }],
                }
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="全国各省份卫衣销量地图",
                pos_left='40%',
                pos_top='10%',
                title_textstyle_opts=opts.TextStyleOpts(
                    color='white',
                    font_size=20
                )
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                type_='color',
                min_=2000,
                max_=320000,
                is_piecewise=True,
                pos_left="30%",
                pos_top="70%",
                range_color=['#C0F1F4', '#60BDCB', '#316870', '#EA7552'],
                textstyle_opts=opts.TextStyleOpts(
                    color='white',
                    font_size=18,
                )

            ),
            legend_opts=opts.LegendOpts(
                is_show=False
            ),
            tooltip_opts=opts.TooltipOpts(
                trigger="item",
                formatter=JsCode(
                    """
                    function f(param){
                        return param.name + '卫衣销量:'+ param.value
                    }
                    """
                )
            )
        )
        .render("map.html")
    )


genGeo(data_pair_1)