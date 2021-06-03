from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar,Timeline

rb=[4.89,
    4.3,
    4.12,
    4.45,
    4.82,
    4.76,
    4.53,
    4.52,
    5.04,
    5.23,
    5.7,
    6.16,
    6.2,
    5.16,
    4.85,
    4.39,
    4.92,
    4.87,
    4.95,
    5.08
    ]

fg =[ 1.36,
     1.38,
     1.49,
     1.84,
     2.12,
     2.2,
     2.32,
     2.66,
     2.92,
     2.69,
     2.64,
     2.86,
     2.68,
     2.81,
     2.85,
     2.44,
     2.47,
     2.6,
     2.79,
     2.72
     ]
mg=[
    10.25,
    10.58,
    10.94,
    11.46,
    12.21,
    13.04,
    13.81,
    14.45,
    14.71,
    14.45,
    14.99,
    15.54,
    16.2,
    16.78,
    17.53,
    18.22,
    18.71,
    19.52,
    20.58,
    21.43
]
yg=[
    1.66,
    1.64,
    1.78,
    2.05,
    2.42,
    2.54,
    2.71,
    3.1,
    2.92,
    2.41,
    2.48,
    2.66,
    2.7,
    2.79,
    3.06,
    2.93,
    2.69,
    2.67,
    2.86,
    2.83

]
zg=[
    1.21,
    1.34,
    1.47,
    1.66,
    1.96,
    2.29,
    2.75,
    3.55,
    4.59,
    5.1,
    6.09,
    7.55,
    8.53,
    9.57,
    10.48,
    11.06,
    11.23,
    12.31,
    13.89,
    14.34
]

tl = Timeline()

def Bar_gdp():
    for i in range(2000,2020):
        c = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
            .add_xaxis(["日本","法国","英国","美国","中国"])
            .add_yaxis('', [rb[i-2000],fg[i-2000],yg[i-2000],mg[i-2000],zg[i-2000]])
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
                .set_global_opts(
                title_opts={"text": "{}年-GDP(万亿美元)".format(i), "subtext": "{}".format('中国人民逐渐从幸福中走来')},
            )
        )
        tl.add(c,'{}年'.format(i))
        tl.add_schema(
            # 播放速度
            play_interval=1000,
            # 是否显示timeline组件
            is_timeline_show=False,
            # 是否自动播放
            is_auto_play=True,
        )
    return tl

