from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode
import pandas as pd
import pyecharts
print(pyecharts.__version__)

df = pd.read_excel('中小学吸烟报告(数据来源：湖南学校数据).xls',sheet_name='吸烟习惯').loc[2:4,['Unnamed: 0','Unnamed: 1']]

df1 = pd.read_excel('中小学吸烟报告(数据来源：湖南学校数据).xls',sheet_name='学生家长吸烟的占比').loc[2:4,['Unnamed: 0','Unnamed: 1']]

list_1 = []
for i in df['Unnamed: 0']:
    list_1.append(i)

list_2 = []
for i in df['Unnamed: 1']:
    list_2.append(i)

list_3 = []
for i in df1['Unnamed: 0']:
    list_3.append(i)

list_4 = []
for i in df1['Unnamed: 1']:
    list_4.append(i)

def buildLiquid(name, data, center):
    l1 = (
        Liquid()
        .add(
            name,
            data,
            center=center,
            label_opts=opts.LabelOpts(
                position="inside",
                color="white",
            ),
            background_color={
                "type": 'linear',
                "x": 1,
                "y": 0,
                "x2": 0.5,
                "y2": 1,
                "colorStops": [{
                    "offset": 1,
                    "color": 'rgba(68, 145, 253, 0)'
                }, {
                    "offset": 0.5,
                    "color": 'rgba(68, 145, 253, .25)'
                }, {
                    "offset": 0,
                    "color": 'rgba(68, 145, 253, 1)'
                }],
                "globalCoord": False
            },
            color=[{
                "type": 'linear',
                "x": 0,
                "y": 0,
                "x2": 0,
                "y2": 1,
                "colorStops": [{
                    "offset": 1,
                    "color": 'rgba(58, 71, 212, 0)'
                }, {
                    "offset": 0.5,
                    "color": 'rgba(31, 222, 225, .2)'
                }, {
                    "offset": 0,
                    "color": 'rgba(31, 222, 225, 1)'
                }],
                "globalCoord": False
            }],
            outline_border_distance=0.,
            outline_itemstyle_opts=opts.ItemStyleOpts(
                border_width=20,
                border_color={
                    "type": 'linear',
                    "x": 0,
                    "y": 0,
                    "x2": 0,
                    "y2": 1,
                    "colorStops": [{
                        "offset": 0,
                        "color": 'rgba(69, 73, 240, 0)'
                    }, {
                        "offset": 0.5,
                        "color": 'rgba(69, 73, 240, .25)'
                    }, {
                        "offset": 1,
                        "color": 'rgba(69, 73, 240, 1)'
                    }],
                    "globalCoord": False
                }
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="中学生与家长吸烟占比",
                title_link="https://new.qq.com/omn/20201004/20201004A0098Z00.html",
                pos_left="32%",
                pos_top="15%",
                title_textstyle_opts=opts.TextStyleOpts(
                    color="white",
                    font_size=30,
                )
            )
        )
    )
    return l1


l1 = buildLiquid("中学生吸烟占比", [list_1[0]], ["30%", "50%"])
l2 = buildLiquid("中学生家长吸烟占比", [list_3[0]], ["70%", "50%"])

grid = (
    Grid(init_opts=opts.InitOpts(
        bg_color=JsCode(
            """
            new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
            offset: 0,
            color: '#431ab8'
            }, {
            offset: 1,
            color: '#471bba'
            }])
            """
        )
    ))
    .add(
        l1,
        grid_opts=opts.GridOpts()
    )
    .add(
        l2,
        grid_opts=opts.GridOpts()
    )
)

grid.render("multiple_liquid.html")