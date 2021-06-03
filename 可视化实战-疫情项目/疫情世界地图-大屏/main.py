from pyecharts.charts import Map
from pyecharts.commons.utils import JsCode
import pandas as pd
from pyecharts.charts import Geo
from pyecharts .globals import ChartType, SymbolType
from pyecharts import options as opts
from pyecharts.charts import Bar,Timeline,Page
from pyecharts.globals import ThemeType
from pyecharts.charts import Line
from pyecharts.components import Table
def map_basic() -> Map:

    x_data = ['Australia', 'Canada', 'United Kingdom', 'United States', 'China']
    y_data_1 = ['0', '0', '0', '0', '9336']
    y_data_2 = ['0', '14', '19', '64', '35420']
    y_data_3 = ['0', '8591', '25474', '161367', '2895']
    y_data_4 = ['6766', '53021', '171253', '1092656', '897']
    y_data_5 = ['7185', '90516', '274762', '1797949', '119']
    y_data_6 = ['7836', '103918', '312654', '2695685', '516']
    y_data_7 = ['16303', '115935', '301455', '4570103', '2227']
    y_data_8 = ['25670', '127673', '332752', '6141778', '649']
    y_data_9 = ['27078', '158425', '453264', '7413600', '365']
    y_data_10 = ['27580', '229438', '989745', '9336073', '521']

    y_data = []
    y_data.append(y_data_1)
    y_data.append(y_data_2)
    y_data.append(y_data_3)
    y_data.append(y_data_4)
    y_data.append(y_data_5)
    y_data.append(y_data_6)
    y_data.append(y_data_7)
    y_data.append(y_data_8)
    y_data.append(y_data_9)
    y_data.append(y_data_10)

    time_list = ['202001', '202002', '202003', '202004', '202005', '202006', '202007', '202008', '202009', '202010']
    tl = Timeline()
    for i in range(1, 11):
        map = (
            Map()
            .add(
                "",
                [list(z) for z in zip(x_data, y_data[int(i - 1)])],
                "world",
                label_opts=opts.LabelOpts(is_show=False),
                is_map_symbol_show=False,
                itemstyle_opts={
                    "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                    "emphasis": {
                        "label": {"show": Timeline},
                        "areaColor": "rgba(255,255,255, 0.5)",
                    },
                },
                    )
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title='World Trade Monitoring' + "" + str(time_list[int(i - 1)]),
                    pos_left="center",
                    pos_top="top",
                    title_textstyle_opts=opts.TextStyleOpts(
                        font_size=32, color="rgba(255,255,255, 0.9)"
                    ), ),
                visualmap_opts=opts.VisualMapOpts(
                    is_calculable=True,
                    dimension=0,
                    pos_left="5",
                    pos_top="center",
                    range_text=["High", "Low"],
                    range_color=["lightskyblue", "yellow", "orangered"],
                    textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                    min_=0,
                    max_=4000000,
                ),
            )
        )
        tl.add(map, "{}".format(time_list[int(i - 1)]))
        tl.add_schema(
            # 播放速度
            play_interval=2000,
            # 是否显示timeline组件
            is_timeline_show=False,
            # 是否自动播放
            is_auto_play=True,
        )
    return tl

def geo_basic() -> Geo:
    df = pd.read_excel('data.xlsx', sheet_name='comtrade').loc[:,
         ['Period', 'Period Desc.', 'Reporter', 'Partner', 'Trade Value (US$)']]

    Reporter_list_01 = []
    Partner_list_01 = []
    Trade_list_01 = []

    Reporter_list_02 = []
    Partner_list_02 = []
    Trade_list_02 = []

    Reporter_list_03 = []
    Partner_list_03 = []
    Trade_list_03 = []

    Reporter_list_04 = []
    Partner_list_04 = []
    Trade_list_04 = []

    Reporter_list_05 = []
    Partner_list_05 = []
    Trade_list_05 = []

    Reporter_list_06 = []
    Partner_list_06 = []
    Trade_list_06 = []

    Reporter_list_07 = []
    Partner_list_07 = []
    Trade_list_07 = []

    Reporter_list_08 = []
    Partner_list_08 = []
    Trade_list_08 = []

    Reporter_list_09 = []
    Partner_list_09 = []
    Trade_list_09 = []

    Reporter_list_10 = []
    Partner_list_10 = []
    Trade_list_10 = []

    for d in range(len(df['Period Desc.'])):
        time = str(df['Period Desc.'][d])
        time = time[0:7]

        if '2020-01' in time:
            Reporter = df['Reporter'][d]
            Reporter_list_01.append(Reporter)
            Partner = df['Partner'][d]
            Partner_list_01.append(Partner)
            Trade = df['Trade Value (US$)'][d]
            Trade_list_01.append(Trade)

        if '2020-02' in time:
            Reporter = df['Reporter'][d]
            Reporter_list_02.append(Reporter)
            Partner = df['Partner'][d]
            Partner_list_02.append(Partner)
            Trade = df['Trade Value (US$)'][d]
            Trade_list_02.append(Trade)

        if '2020-03' in time:
            Reporter = df['Reporter'][d]
            Reporter_list_03.append(Reporter)
            Partner = df['Partner'][d]
            Partner_list_03.append(Partner)
            Trade = df['Trade Value (US$)'][d]
            Trade_list_03.append(Trade)

        if '2020-04' in time:
            Reporter = df['Reporter'][d]
            Reporter_list_04.append(Reporter)
            Partner = df['Partner'][d]
            Partner_list_04.append(Partner)
            Trade = df['Trade Value (US$)'][d]
            Trade_list_04.append(Trade)

        if '2020-05' in time:
            Reporter = df['Reporter'][d]
            Reporter_list_05.append(Reporter)
            Partner = df['Partner'][d]
            Partner_list_05.append(Partner)
            Trade = df['Trade Value (US$)'][d]
            Trade_list_05.append(Trade)

        if '2020-06' in time:
            Reporter = df['Reporter'][d]
            Reporter_list_06.append(Reporter)
            Partner = df['Partner'][d]
            Partner_list_06.append(Partner)
            Trade = df['Trade Value (US$)'][d]
            Trade_list_06.append(Trade)

        if '2020-07' in time:
            Reporter = df['Reporter'][d]
            Reporter_list_07.append(Reporter)
            Partner = df['Partner'][d]
            Partner_list_07.append(Partner)
            Trade = df['Trade Value (US$)'][d]
            Trade_list_07.append(Trade)

        if '2020-08' in time:
            Reporter = df['Reporter'][d]
            Reporter_list_08.append(Reporter)
            Partner = df['Partner'][d]
            Partner_list_08.append(Partner)
            Trade = df['Trade Value (US$)'][d]
            Trade_list_08.append(Trade)

        if '2020-09' in time:
            Reporter = df['Reporter'][d]
            Reporter_list_09.append(Reporter)
            Partner = df['Partner'][d]
            Partner_list_09.append(Partner)
            Trade = df['Trade Value (US$)'][d]
            Trade_list_09.append(Trade)

        if '2020-10' in time:
            Reporter = df['Reporter'][d]
            Reporter_list_10.append(Reporter)
            Partner = df['Partner'][d]
            Partner_list_10.append(Partner)
            Trade = df['Trade Value (US$)'][d]
            Trade_list_10.append(Trade)

    data_pair_01_1 = [(i, int(j)) for i, j in zip(Partner_list_01, Trade_list_01)]
    data_pair_01_2 = [(i, j) for i, j in zip(Reporter_list_01, Partner_list_01)]

    data_pair_02_1 = [(i, int(j)) for i, j in zip(Partner_list_02, Trade_list_02)]
    data_pair_02_2 = [(i, j) for i, j in zip(Reporter_list_02, Partner_list_02)]

    data_pair_03_1 = [(i, int(j)) for i, j in zip(Partner_list_03, Trade_list_03)]
    data_pair_03_2 = [(i, j) for i, j in zip(Reporter_list_03, Partner_list_03)]

    data_pair_04_1 = [(i, int(j)) for i, j in zip(Partner_list_04, Trade_list_04)]
    data_pair_04_2 = [(i, j) for i, j in zip(Reporter_list_04, Partner_list_04)]

    data_pair_05_1 = [(i, int(j)) for i, j in zip(Partner_list_05, Trade_list_05)]
    data_pair_05_2 = [(i, j) for i, j in zip(Reporter_list_05, Partner_list_05)]

    data_pair_06_1 = [(i, int(j)) for i, j in zip(Partner_list_06, Trade_list_06)]
    data_pair_06_2 = [(i, j) for i, j in zip(Reporter_list_06, Partner_list_06)]

    data_pair_07_1 = [(i, int(j)) for i, j in zip(Partner_list_07, Trade_list_07)]
    data_pair_07_2 = [(i, j) for i, j in zip(Reporter_list_07, Partner_list_07)]

    data_pair_08_1 = [(i, int(j)) for i, j in zip(Partner_list_08, Trade_list_08)]
    data_pair_08_2 = [(i, j) for i, j in zip(Reporter_list_08, Partner_list_08)]

    data_pair_09_1 = [(i, int(j)) for i, j in zip(Partner_list_09, Trade_list_09)]
    data_pair_09_2 = [(i, j) for i, j in zip(Reporter_list_09, Partner_list_09)]

    data_pair_10_1 = [(i, int(j)) for i, j in zip(Partner_list_10, Trade_list_10)]
    data_pair_10_2 = [(i, j) for i, j in zip(Reporter_list_10, Partner_list_10)]

    data_pair_sum = []
    data_pair_sum.append(data_pair_01_1)
    data_pair_sum.append(data_pair_02_1)
    data_pair_sum.append(data_pair_02_1)
    data_pair_sum.append(data_pair_03_1)
    data_pair_sum.append(data_pair_04_1)
    data_pair_sum.append(data_pair_05_1)
    data_pair_sum.append(data_pair_06_1)
    data_pair_sum.append(data_pair_07_1)
    data_pair_sum.append(data_pair_08_1)
    data_pair_sum.append(data_pair_09_1)
    data_pair_sum.append(data_pair_10_1)

    data_pair_sum_2 = []
    data_pair_sum_2.append(data_pair_01_2)
    data_pair_sum_2.append(data_pair_02_2)
    data_pair_sum_2.append(data_pair_02_2)
    data_pair_sum_2.append(data_pair_03_2)
    data_pair_sum_2.append(data_pair_04_2)
    data_pair_sum_2.append(data_pair_05_2)
    data_pair_sum_2.append(data_pair_06_2)
    data_pair_sum_2.append(data_pair_07_2)
    data_pair_sum_2.append(data_pair_08_2)
    data_pair_sum_2.append(data_pair_09_2)
    data_pair_sum_2.append(data_pair_10_2)
    time_list = ['202001', '202002', '202003', '202004', '202005', '202006', '202007', '202008', '202009', '202010']
    tl = Timeline()
    for i in range(1, 11):
        geo = (
            Geo()
            .add_coordinate(name="China", longitude=104.195, latitude=35.675)
            .add_coordinate(name="Australia", longitude=133.775, latitude=-25.274)
            .add_coordinate(name="Canada", longitude=-106.346, latitude=56.130)
            .add_coordinate(name="United Kingdom", longitude=-1.25596, latitude=51.75222)
            .add_coordinate(name="United States", longitude=-100.346, latitude=39.675)
            .add_schema(
                maptype="world",
                itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
            )
            .add(
                "Trade Value (US$)",
                data_pair_sum[int(i - 1)],
                color='#152BEF',
                type_=ChartType.EFFECT_SCATTER,
            )
            .add(
                "Direction of trade flow",
                data_pair_sum_2[int(i - 1)],
                color='#152BEF',
                type_=ChartType.LINES,
                effect_opts=opts.EffectOpts(
                    symbol=SymbolType.ARROW, symbol_size=6, color="GreenYellow"
                ),
                linestyle_opts=opts.LineStyleOpts(curve=0.2),
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        tl.add(geo, "{}".format(time_list[int(i - 1)]))
        tl.add_schema(
            # 播放速度
            play_interval=2000,
            # 是否显示timeline组件
            is_timeline_show=False,
            # 是否自动播放
            is_auto_play=True,
        )
    return tl

def bar_basic() -> Bar:
    x_data = ['Australia', 'Canada', 'UK', 'USA', 'China']
    y_data_1 = ['0', '0', '0', '0', '9336']
    y_data_2 = ['0', '14', '19', '64', '35420']
    y_data_3 = ['0', '8591', '25474', '161367', '2895']
    y_data_4 = ['6766', '53021', '171253', '1092656', '897']
    y_data_5 = ['7185', '90516', '274762', '1797949', '119']
    y_data_6 = ['7836', '103918', '312654', '2695685', '516']
    y_data_7 = ['16303', '115935', '301455', '4570103', '2227']
    y_data_8 = ['25670', '127673', '332752', '6141778', '649']
    y_data_9 = ['27078', '158425', '453264', '7413600', '365']
    y_data_10 = ['27580', '229438', '989745', '9336073', '521']

    y_data = []
    y_data.append(y_data_1)
    y_data.append(y_data_2)
    y_data.append(y_data_3)
    y_data.append(y_data_4)
    y_data.append(y_data_5)
    y_data.append(y_data_6)
    y_data.append(y_data_7)
    y_data.append(y_data_8)
    y_data.append(y_data_9)
    y_data.append(y_data_10)
    time_list = ['202001', '202002', '202003', '202004', '202005', '202006', '202007', '202008', '202009', '202010']
    tl = Timeline({"theme": ThemeType.MACARONS})
    for i in range(1, 11):
        bar = (
            Bar(init_opts=opts.InitOpts(width="300px", height="200px",theme=ThemeType.MACARONS))
            .add_xaxis(x_data)
            .add_yaxis(
                "",
                y_data[int(i - 1)],
                category_gap="60%",
                label_opts=opts.LabelOpts(
                    is_show=True, position="right", formatter="{b} : {c}"
                ),
            )
            .reversal_axis()
            .set_series_opts(
                itemstyle_opts={
                    "normal": {
                        "color": JsCode(
                            """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: 'rgba(0, 244, 255, 1)'
                    }, {
                        offset: 1,
                        color: 'rgba(0, 77, 167, 1)'
                    }], false)"""
                        ),
                        "barBorderRadius": [30, 30, 30, 30],
                        "shadowColor": "rgb(0, 160, 221)",
                    }
                }
            )
            .set_global_opts(
                title_opts=opts.TitleOpts("{} Number of confirmed cases".format(time_list[int(i - 1)]),pos_left="35%", pos_top="5%")
            )
        )
        tl.add(bar, "{}".format(time_list[int(i - 1)]))
        tl.add_schema(
            # 播放速度
            play_interval=2000,
            # 是否显示timeline组件
            is_timeline_show=False,
            # 是否自动播放
            is_auto_play=True,
        )
    return tl

def line_basic() -> Line:
    df = pd.read_excel('data.xlsx').loc[:,['Country','Month','Number']]

    x_data = []
    y_Australia = []
    y_Canada = []
    y_United_Kingdom = []
    y_United_States_of_America = []
    y_China = []

    for i in df['Month'][0:10]:
        i = str(i)
        x_data.append(i)
    for a in df['Number'][0:10]:
        y_Australia.append(a)

    for c in df['Number'][10:20]:
        y_Canada.append(c)

    for u_k in df['Number'][20:30]:
        y_United_Kingdom.append(u_k)

    for u_s_a in df['Number'][30:40]:
        y_United_States_of_America.append(u_s_a)

    for c_a in df['Number'][40:50]:
        y_China.append(c_a)



    c = (
        Line(init_opts=opts.InitOpts(width="700px", height="350px"))
        .add_xaxis(x_data)
        .add_yaxis("Australia",y_Australia, is_smooth=True,color="#ADD8E6",symbol="emptyCircle")
        .add_yaxis("Canada", y_Canada, is_smooth=True,color="#008080",symbol="emptyCircle")
        .add_yaxis("UK", y_United_Kingdom, is_smooth=True,color="#7CFC00",symbol="emptyCircle")
        .add_yaxis("USA", y_United_States_of_America, is_smooth=True,color="#00FFFF",symbol="emptyCircle")
        .add_yaxis("China", y_China, is_smooth=True,color="#A9A9A9",symbol="emptyCircle")
        .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Changes in national trade", pos_left="25%", pos_top="5%"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
            ),
        )
    )
    return c

def table_base() -> Table:
    headers = ["Quantum of world trade", "The total number of confirmed"]
    rows = [
        [1704236942191, 37129547],
    ]
    table = (
            Table()
            .add(headers, rows)
        )
    return table

def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        map_basic(),
        geo_basic(),
        bar_basic(),
        line_basic(),
        table_base()
    )
    page.save_resize_html(cfg_file="chart_config.json")
    # page.render()

if __name__ == '__main__':
    page_draggable_layout()


