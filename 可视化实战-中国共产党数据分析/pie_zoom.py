from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar,Timeline,Pie

y_data = [3.5,3.2,3.1,2.8,2.5,2.3,1.6,4.2,3.8,17.2,12.7,10.2,8.5,7.2,5.7,4.5,3.1,1.7,0.6]
y_data1 = []

for y in y_data:
    l = float((50-float(y)))
    y_data1.append(l)
year = [
    2000,
    2001,
    2002,
    2003,
    2004,
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
]
x_data = ['平均人口消费比重','贫困人口消费比重']
def Pie_zoom():
    tl = Timeline()
    for i in range(len(year)):
        c = (
            Pie({"theme": ThemeType.INFOGRAPHIC})
                .add(
                "贫困率(单位:%)",
                [list(z) for z in zip(x_data,[y_data1[i],y_data[i]])],
                radius=["40%", "55%"],
                label_opts=opts.LabelOpts(
                    is_show=True,
                    background_color="#eee",
                    border_color="#aaa",
                    border_width=1,
                    border_radius=2,
                    rich={
                        "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                        "abg": {
                            "backgroundColor": "#e3e3e3",
                            "width": "100%",
                            "align": "right",
                            "height": 22,
                            "borderRadius": [4, 4, 0, 0],
                        },
                        "hr": {
                            "borderColor": "#aaa",
                            "width": "100%",
                            "borderWidth": 0.5,
                            "height": 0,
                        },
                        "b": {"fontSize": 16, "lineHeight": 33},
                        "per": {
                            "color": "#eee",
                            "backgroundColor": "#334455",
                            "padding": [2, 4],
                            "borderRadius": 2,
                        },
                    },
                ),
            )
            .set_global_opts(legend_opts=opts.LegendOpts(is_show=False),title_opts=opts.TitleOpts(title='{}年贫困人口比重'.format(year[i]),pos_left='center'))
            .set_series_opts(
                tooltip_opts=opts.TooltipOpts(
                    trigger="item", formatter="{b}:{d}%"
                ),
            )
        )
        tl.add(c,'"{}年".format(i)')
        tl.add_schema(
            # 播放速度
            play_interval=1000,
            # 是否显示timeline组件
            is_timeline_show=False,
            # 是否自动播放
            is_auto_play=True,
        )
    return tl




