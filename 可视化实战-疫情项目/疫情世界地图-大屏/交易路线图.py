import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts .globals import ChartType, SymbolType, GeoType
from pyecharts.charts import Bar,Timeline

df = pd.read_excel('data.xlsx',sheet_name='comtrade').loc[:,['Period','Period Desc.','Reporter','Partner','Trade Value (US$)']]


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



data_pair_01_1 = [(i, int(j)) for i, j in zip(Partner_list_01,Trade_list_01)]
data_pair_01_2 = [(i, j) for i, j in zip(Reporter_list_01,Partner_list_01)]

data_pair_02_1 = [(i, int(j)) for i, j in zip(Partner_list_02,Trade_list_02)]
data_pair_02_2 = [(i, j) for i, j in zip(Reporter_list_02,Partner_list_02)]

data_pair_03_1 = [(i, int(j)) for i, j in zip(Partner_list_03,Trade_list_03)]
data_pair_03_2 = [(i, j) for i, j in zip(Reporter_list_03,Partner_list_03)]

data_pair_04_1 = [(i, int(j)) for i, j in zip(Partner_list_04,Trade_list_04)]
data_pair_04_2 = [(i, j) for i, j in zip(Reporter_list_04,Partner_list_04)]

data_pair_05_1 = [(i, int(j)) for i, j in zip(Partner_list_05,Trade_list_05)]
data_pair_05_2 = [(i, j) for i, j in zip(Reporter_list_05,Partner_list_05)]

data_pair_06_1 = [(i, int(j)) for i, j in zip(Partner_list_06,Trade_list_06)]
data_pair_06_2 = [(i, j) for i, j in zip(Reporter_list_06,Partner_list_06)]

data_pair_07_1 = [(i, int(j)) for i, j in zip(Partner_list_07,Trade_list_07)]
data_pair_07_2 = [(i, j) for i, j in zip(Reporter_list_07,Partner_list_07)]

data_pair_08_1 = [(i, int(j)) for i, j in zip(Partner_list_08,Trade_list_08)]
data_pair_08_2 = [(i, j) for i, j in zip(Reporter_list_08,Partner_list_08)]

data_pair_09_1 = [(i, int(j)) for i, j in zip(Partner_list_09,Trade_list_09)]
data_pair_09_2 = [(i, j) for i, j in zip(Reporter_list_09,Partner_list_09)]

data_pair_10_1 = [(i, int(j)) for i, j in zip(Partner_list_10,Trade_list_10)]
data_pair_10_2 = [(i, j) for i, j in zip(Reporter_list_10,Partner_list_10)]


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
time_list = ['202001','202002','202003','202004','202005','202006','202007','202008','202009','202010']
tl = Timeline()
for i in range(1,11):
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
            data_pair_sum[int(i-1)],
            color='#152BEF',
            type_=ChartType.EFFECT_SCATTER,

        )
        .add(
            "贸易流动方向",
            data_pair_sum_2[int(i-1)],
            color='#152BEF',
            type_=ChartType.LINES,
            effect_opts=opts.EffectOpts(
                symbol=SymbolType.ARROW, symbol_size=6, color="GreenYellow"
            ),
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Geo-Lines-background"))
    )
    tl.add(geo, "{}".format(time_list[int(i-1)]))
    tl.add_schema(
        # 播放速度
        play_interval=1000,
        # 是否显示timeline组件
        is_timeline_show=False,
        # 是否自动播放
        is_auto_play=True,
    )
tl.render("geo.html")


