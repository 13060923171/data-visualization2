from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType
from pyecharts.commons.utils import JsCode
import pandas as pd

df = pd.read_excel('居民消费价-数据.xlsx').loc[:,['地区','平均值']]

area_list = []
average_list = []

for a in df['地区']:
    a = str(a)
    a = a.replace('市','').replace('省','').replace('自治区','').replace('壮族','').replace('回族','').replace('维吾尔','')
    area_list.append(a)

for ave in df['平均值']:
    ave = float(ave)
    ave = '{:0.2f}'.format(ave)
    average_list.append(ave)

data_pair_1 = [(i, j) for i, j in zip(area_list,average_list)]
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
                title="全国各省份平均消费",
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
                min_=100,
                max_=105,
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
                        return param.name + '消费平均值:'+ param.value
                    }
                    """
                )
            )
        )
        .render("map.html")
    )


genGeo(data_pair_1)