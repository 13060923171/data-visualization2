from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.charts import Timeline
from pyecharts.globals import ThemeType
import pandas as pd
df = pd.read_excel('data.xlsx',sheet_name='comtrade').loc[:,['Period','Period Desc.','Reporter','Partner','Trade Value (US$)']]

Trade_list_01 = []
Trade_list_02 = []
Trade_list_03 = []
Trade_list_04 = []
Trade_list_05 = []
Trade_list_06 = []
Trade_list_07 = []
Trade_list_08 = []
Trade_list_09 = []
Trade_list_10 = []

for d in range(len(df['Period Desc.'])):
    time = str(df['Period Desc.'][d])
    time = time[0:7]

    if '2020-01' in time:
            Trade = df['Trade Value (US$)'][d]
            Trade_list_01.append(Trade)

    if '2020-02' in time:
            Trade = df['Trade Value (US$)'][d]
            Trade_list_02.append(Trade)

    if '2020-03' in time:
            Trade = df['Trade Value (US$)'][d]
            Trade_list_03.append(Trade)

    if '2020-04' in time:
            Trade = df['Trade Value (US$)'][d]
            Trade_list_04.append(Trade)

    if '2020-05' in time:
            Trade = df['Trade Value (US$)'][d]
            Trade_list_05.append(Trade)

    if '2020-06' in time:
            Trade = df['Trade Value (US$)'][d]
            Trade_list_06.append(Trade)

    if '2020-07' in time:
            Trade = df['Trade Value (US$)'][d]
            Trade_list_07.append(Trade)

    if '2020-08' in time:
            Trade = df['Trade Value (US$)'][d]
            Trade_list_08.append(Trade)

    if '2020-09' in time:
            Trade = df['Trade Value (US$)'][d]
            Trade_list_09.append(Trade)

    if '2020-10' in time:
            Trade = df['Trade Value (US$)'][d]
            Trade_list_10.append(Trade)



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


# def get_time1():
#     time_list = ['202001', '202002', '202003', '202004', '202005', '202006', '202007', '202008', '202009', '202010']
#     timeline = Timeline(
#         init_opts=opts.InitOpts(theme=ThemeType.MACARONS)
#     )
#     for y in range(len(time_list)):
#         g = table_base(year=y)
#         timeline.add(g, time_point=str(y))
#     timeline.add_schema(
#         # 播放速度
#         play_interval=3000,
#         # 是否显示timeline组件
#         is_timeline_show=False,
#         # 是否自动播放
#         is_auto_play=True,
#         label_opts=opts.LabelOpts(is_show=True, color="#fff"),
#     )
#     return timeline

if __name__ == '__main__':
    table_base()
