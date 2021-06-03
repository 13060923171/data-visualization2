from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType
from pyecharts.commons.utils import JsCode
import pandas as pd
df = pd.read_excel('图2数据.xls',sheet_name='Sheet1')
diqu_list = []
for line in df['地区']:
    diqu_list.append(line)
data= [(i, int(j)) for i, j in zip(diqu_list, df['数据'])]
datas = sorted(data,key=lambda x: x[1])

ENGLISH_PROVINCE_NAMES = {
        "广东": "Guangdong",
        "安徽": "Anhui",
        "福建": "Fujian",
        "甘肃": "Gansu",
        "广西": "Guangxi",
        "贵州": "Guizhou",
        "海南": "Hainan",
        "河北": "Hebei",
        "黑龙江": "Heilongjiang",
        "河南": "Henan",
        "湖北": "Hubei",
        "湖南": "Hunan",
        "江苏": "Jiangsu",
        "江西": "Jiangxi",
        "吉林": "Jilin",
        "辽宁": "Liaoning",
        "内蒙古": "Neimenggu",
        "宁夏": "Ningxia",
        "青海": "Qinghai",
        "山东": "Shandong",
        "山西": "Shanxi",
        "陕西": "Shanxi1",
        "四川": "Sichuan",
        "台湾": "Taiwan",
        "新疆": "Xinjiang",
        "西藏": "Xizang",
        "云南": "Yunnan",
        "浙江": "Zhejiang",
        "重庆": "Chongqing",
        "香港": "Hongkong",
        "澳门": "Macao",
        "南海诸岛": "South China Sea Islands",
        "北京": "Beijing",
        "天津": "Tianjin",
        "上海": "Shanghai"
    }
def genGeo(data):
    c = (
        Map(init_opts=opts.InitOpts(
            width='1200px',
            height='600px',
            bg_color='#0F1C3C',
        ))
        .add(  # 添加散点图
            "",
            data,
            name_map=ENGLISH_PROVINCE_NAMES,
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
                title="Population mobility from 2013 to 2019",
                pos_left='40%',
                pos_top='0%',
                title_textstyle_opts=opts.TextStyleOpts(
                    color='white',
                    font_size=20
                )
            ),
            visualmap_opts=opts.VisualMapOpts(
                min_=-1000,
                max_=9000,
                range_text=["High", "Low"],
                is_calculable=True,
                range_color=['#C0F1F4', '#DC143C', '#FFFFE0', '#FFD700','#FFFF00'],
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
                        return param.name + ',Year-end resident population:'+ param.value+'ten thousand'
                    }
                    """
                )
            )
        )
        .render("gdp-map.html")
    )


genGeo(data)
