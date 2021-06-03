import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar,Timeline,Grid
from pyecharts.globals import ThemeType

df = pd.read_excel('eqdata.xls').loc[:,['震级','时间','地点']]
tl = Timeline({'theme':ThemeType.MACARONS})


def bar_timeline():
    for i in range(785,(0-1),-1):
        bar = (
            Bar({'theme':ThemeType.MACARONS})
            .add_xaxis(list(df['地点'])[i*10:i*10+10][::-1])
            .add_yaxis('地震等级排名',list(df['震级'])[i*10:i*10+10][::-1])
            .reversal_axis()
            .set_global_opts(
                title_opts=opts.TitleOpts("{}".format(list(df['时间'])[i * 10]), pos_right='0%', pos_bottom='15%'),
                xaxis_opts=opts.AxisOpts(
                    splitline_opts=opts.SplitLineOpts(is_show=True)),
                yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True),
                                         axislabel_opts=opts.LabelOpts(color='#FF7F50')), )
            .set_series_opts(label_opts=opts.LabelOpts(position="right", color='#9400D3'))
        )
        grid = (
            Grid()
            #将图形整体右移
            .add(bar,grid_opts=opts.GridOpts(pos_left='25%',pos_right='0%'))

        )
        tl.add(grid,"{}年".format(i))
        tl.add_schema(
            #播放速度
            play_interval=500,
            #是否显示timeline组件
            is_timeline_show=False,
            #是否自动播放
            is_auto_play=True,
        )
    return tl
