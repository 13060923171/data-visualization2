from pyecharts.globals import ThemeType
import pyecharts.options as opts
from pyecharts.charts import Radar, Timeline
import pandas as pd

c = ['#00c2ff','#f9cf67','#e92b77']

df = pd.read_excel('中小学吸烟报告(数据来源：湖南学校数据).xls',sheet_name='在什么场合吸烟').loc[2:4,['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5']]

list_1 = []
for i in df['Unnamed: 0']:
    list_1.append(i)

list_2 = []
for i in df['Unnamed: 1']:
    list_2.append(i)

list_3 = []
for i in df['Unnamed: 2']:
    list_3.append(i)

list_4 = []
for i in df['Unnamed: 3']:
    list_4.append(i)

list_5 = []
for i in df['Unnamed: 4']:
    list_5.append(i)

list_6 = []
for i in df['Unnamed: 5']:
    list_6.append(i)


tl = Timeline(init_opts=opts.InitOpts(theme=ThemeType.DARK)) # pyecharts 的bug ，bg_color 不起作用


rad = (
    Radar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .set_global_opts(
        legend_opts=opts.LegendOpts(
            is_show=True,
            pos_bottom=45,
            item_width=14,
            item_height=14,
            textstyle_opts=opts.TextStyleOpts(
                font_size=14,
                color='#ade3ff'
            )
        )
    )
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="在家", max_=1,color='#98F5FF'),
            opts.RadarIndicatorItem(name="校内", max_=1,color='#98F5FF'),
            opts.RadarIndicatorItem(name="校外", max_=1,color='#98F5FF'),
            opts.RadarIndicatorItem(name="娱乐场所", max_=1,color='#98F5FF'),
            opts.RadarIndicatorItem(name="聚会", max_=1,color='#98F5FF'),
            opts.RadarIndicatorItem(name="其他场所", max_=1,color='#98F5FF'),
        ],
        center=['50%', '50%'],
        textstyle_opts=opts.TextStyleOpts(
            color='red',
        ),
        splitline_opt=opts.SplitLineOpts(
            is_show= True,
            linestyle_opts=opts.LineStyleOpts(
                color='#98F5FF',
                width=1,
                type_='dotted'
            )
        ),
        axisline_opt=opts.AxisLineOpts(
            linestyle_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color='#98F5FF',
                )
            )
        ),
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True,
            areastyle_opts=opts.AreaStyleOpts(
                color=['#141c42', '#141c42']
            )
        )
    )
    .add(
            series_name='',
            data=[[list_1[0],list_2[0],list_3[0],list_4[0],list_5[0],list_6[0]]],
            color=c[0],
            label_opts=opts.LabelOpts({
            "normal": {
                "show": True,
                "position": 'top',
                "distance": 2,
                "color": '#6692e2',
                "fontSize": 14,
            }
        }
        ),
    )
    .set_series_opts(
        linestyle_opts=opts.LineStyleOpts(
            width=2
        )
    )
    .set_global_opts(
            title_opts=opts.TitleOpts(
                title="中学生一般在何地吸烟",
                title_link="https://new.qq.com/omn/20201004/20201004A0098Z00.html",
                pos_left="32%",
                # pos_top="1%",
                title_textstyle_opts=opts.TextStyleOpts(
                    color="white",
                    font_size=30,
                )
            )
        )
    .render('radar.html')
)
