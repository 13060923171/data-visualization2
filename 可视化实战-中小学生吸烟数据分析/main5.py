from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
import pandas as pd

df = pd.read_excel('中小学吸烟报告(数据来源：湖南学校数据).xls',sheet_name='烟草有害成分').loc[2:4,['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4']]
x_data = ['尼古丁','烟焦油','一氧化碳','氢氰酸','其他']

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

y_data = [list_1[0],list_2[0],list_3[0],list_4[0],list_5[0]]

inner_x_data = ["无害", "轻度有害", "重度有害","不知道"]

inner_y_data = [0.70, 7, 70,9]

inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]

c = (
    Pie(opts.InitOpts(bg_color="#BF8AB0"))
    .add(
        series_name="中学生对吸烟认识状况",
        data_pair=inner_data_pair,
        radius=[0, "30%"],
        label_opts=opts.LabelOpts(
            position="inner",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            is_show=False,
            ),
    )
    .add(
        "",
        [list(z) for z in zip(x_data,y_data)],
        radius=["40%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,

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
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="吸烟有害成分与中学生怎么看待吸烟占比图",
            title_link="https://new.qq.com/omn/20201004/20201004A0098Z00.html",
            pos_left="20%",
            pos_top="5%",
            title_textstyle_opts=opts.TextStyleOpts(
                color="black",
                font_size=30,
            )
        )
    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}:({d}%)"
        )
    )
    .render("pie_rich_label.html")
)

