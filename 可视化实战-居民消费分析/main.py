from pyecharts.charts import Map, Page
from pyecharts.charts import Line
from pyecharts.charts import Scatter
from pyecharts.commons.utils import JsCode
import pandas as pd
from pyecharts.charts import Bar

from pyecharts import options as opts
from pyecharts.charts import Sankey
from pyecharts.globals import ThemeType

def map_basic() -> Map:
    df = pd.read_excel('居民消费价-数据.xlsx').loc[:, ['地区', '平均值']]

    area_list = []
    average_list = []

    for a in df['地区']:
        a = str(a)
        a = a.replace('市', '').replace('省', '').replace('自治区', '').replace('壮族', '').replace('回族', '').replace('维吾尔',
                                                                                                               '')
        area_list.append(a)

    for ave in df['平均值']:
        ave = float(ave)
        ave = '{:0.2f}'.format(ave)
        average_list.append(ave)

    data_pair_1 = [(i, j) for i, j in zip(area_list, average_list)]
    data_pair_1 = sorted(data_pair_1, key=lambda x: x[1])
    c = (
        Map(init_opts=opts.InitOpts(
            width='1300px',
            height='700px',
            bg_color='#0F1C3C',
        ))
            .add(  # 添加散点图
            "",
            data_pair_1,
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
    )
    return c

def line_basic() -> Line:
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

    x_data = ['2019.11', '2019.12', '2020.01', '2020.02', '2020.03', '2020.04', '2020.05', '2020.06', '2020.07',
              '2020.08', '2020.09', '2020.10', '2020.11']

    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="北京",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#d14a61",
            y_axis=beijing_list,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=1)
        )
            .add_yaxis(
            series_name="广东",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#6e9ef1",
            y_axis=guangdong_list,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )
            .add_yaxis(
            series_name="上海",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#F9FF33",
            y_axis=shanghai_list,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )
            .add_yaxis(
            series_name="浙江",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#A0FF33",
            y_axis=zhejian_list,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )
            .add_yaxis(
            series_name="湖南",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#33FF76",
            y_axis=hunan_list,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )
            .add_yaxis(
            series_name="湖北",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#337FFF",
            y_axis=hubei_list,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )

            .add_yaxis(
            series_name="重庆",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#A333FF",
            y_axis=chongqing_list,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="热门省份消费水平"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                min_=98.5,
                max_=108.5,
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False, axisline_opts=opts.AxisLineOpts(
                is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            )),
        )
    )
    return line

def scatter_basic() -> Scatter:
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

    x_data = ['2019.11', '2019.12', '2020.01', '2020.02', '2020.03', '2020.04', '2020.05', '2020.06', '2020.07',
              '2020.08', '2020.09', '2020.10', '2020.11']

    c = (
        Scatter()
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
    )
    return c

def bar_revesal() -> Bar:
    df = pd.read_excel('居民消费价-数据.xlsx').loc[:, ['地区', '平均值']]

    area_list = []
    average_list = []

    for a in df['地区']:
        area_list.append(a)

    for ave in df['平均值']:
        average_list.append(ave)

    c = (
        Bar(init_opts=opts.InitOpts(width="1300px", height="600px", theme=ThemeType.DARK))
            .add_xaxis(area_list)
            .add_yaxis("平均值", average_list, label_opts=opts.LabelOpts(is_show=False))
            .reversal_axis()
            .set_global_opts(
            title_opts={"text": "各地区平均值"}
        )
    )
    return c

def bar_basic() -> Bar:
    df = pd.read_excel('居民消费价-数据.xlsx').loc[:, ['地区', '平均值']]

    area_list = []
    average_list = []

    for a in df['地区']:
        area_list.append(a)

    for ave in df['平均值']:
        average_list.append(ave)

    c = (
        Bar(init_opts=opts.InitOpts(width="1300px", height="600px", theme=ThemeType.MACARONS))
            .add_xaxis(area_list)
            .add_yaxis("平均值", average_list, label_opts=opts.LabelOpts(is_show=False))

            .set_global_opts(
            title_opts={"text": "各地区平均值"}
        )
    )
    return c

def sankey_basic() -> Sankey:
    nodes = [
        {"name": "北京"},
        {"name": "上海"},
        {"name": "广东"},
        {"name": "重庆"},
        {"name": "浙江"},
        {"name": "湖南"},
        {"name": "湖北"},
    ]

    links = [
        {"source": "北京", "target": "上海", "value": 102.09},
        {"source": "上海", "target": "广东", "value": 103.27},
        {"source": "广东", "target": "重庆", "value": 102.81},
        {"source": "重庆", "target": "浙江", "value": 102.62},
        {"source": "浙江", "target": "湖南", "value": 102.79},
        {"source": "湖南", "target": "湖北", "value": 103.30},
    ]
    c = (
        Sankey()
            .add(
            "桑基图",
            nodes,
            links,
            linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
            label_opts=opts.LabelOpts(position="right"),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="热门省份-桑基图"))
    )
    return c

def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        map_basic(),
        bar_revesal(),
        bar_basic(),
        line_basic(),
        sankey_basic(),
        scatter_basic()

    )
    page.save_resize_html(cfg_file="chart_config.json")
    # page.render()


if __name__ == '__main__':
    page_draggable_layout()
