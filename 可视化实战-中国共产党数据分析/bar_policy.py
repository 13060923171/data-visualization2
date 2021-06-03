from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

def Bar_policy():
    tl = Timeline()
    for i in range(2000,2020):
        bar = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC))
                .add_xaxis(['{}年'.format(i)])
                .add_yaxis("", Faker.values(),category_gap="80%")
                .set_global_opts(title_opts=opts.TitleOpts("{}年拨款(单位:亿)".format(i)))
        )
        tl.add(bar, "{}年".format(i))
        tl.add_schema(
            # 播放速度
            play_interval=1000,
            # 是否显示timeline组件
            is_timeline_show=False,
            # 是否自动播放
            is_auto_play=True,
        )
    return tl