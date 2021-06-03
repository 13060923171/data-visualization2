import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
from pyecharts.globals import ThemeType

df = pd.read_excel('./数据/中共信息.xls').loc[:,['时间','内容']]
list_time = []
x_data = []
y_data = []
for i in df['时间']:
    l = i.split('（')
    x_data.append(i)
    y_data.append(l[1].replace('）','').replace(')','').replace('年',''))


time_1950 = []
time_1980 = []
time_2020 = []
for i in range(len(y_data)):
    if int(y_data[i]) > int(1920) and int(y_data[i]) <= int(1950):
        time_1950.append(x_data[i])
    elif int(y_data[i]) > int(1950) and int(y_data[i]) <= int(1980):
        time_1980.append(x_data[i])
    elif int(y_data[i]) > int(1980) and int(y_data[i]) < int(2020):
        time_2020.append(x_data[i])

x_data_50 = [50,10,5,10,5,5,30,10,5,10,50,5,5,5]
data_pair_1 = [list(z) for z in zip(time_1950,x_data_50)]
x_data_80 = [40,10,10,20,10]
data_pair_2 = [list(z) for z in zip(time_1980,x_data_80)]
x_data_2020 = [30,10,10,30,10,10,10,10]
data_pair_3 = [list(z) for z in zip(time_2020,x_data_2020)]
list_sum = []
list_sum.append(data_pair_1)
list_sum.append(data_pair_2)
list_sum.append(data_pair_3)
time_list= ['1920-1950','1950-1980','1980-2020']
def timer_shaft():
    tl = Timeline()
    for i in range(len(time_list)):
        pie = (
            Pie(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
            .add(
                "",
                list_sum[i],
                rosetype="radius",
                radius=["30%", "55%"],

            )
            .set_global_opts(title_opts=opts.TitleOpts("党100年内所发生的重大事件",pos_left="center",pos_top="top"),legend_opts=opts.LegendOpts(is_show=False))
            .set_series_opts(
                tooltip_opts=opts.TooltipOpts(
                    trigger="item", formatter="{b}"
                ),
            )
        )
        tl.add(pie, "{}年".format(time_list[i]))
        tl.add_schema(
            # 播放速度
            play_interval=1000,
            # 是否显示timeline组件
            is_timeline_show=True,
            # 是否自动播放
            is_auto_play=True,
        )
    return tl