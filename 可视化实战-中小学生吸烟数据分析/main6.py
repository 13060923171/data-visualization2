from pyecharts import options as opts
from pyecharts.charts import Polar
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
import pandas as pd
import pyecharts
print(pyecharts.__version__)

df = pd.read_excel('中小学吸烟报告(数据来源：湖南学校数据).xls',sheet_name='吸烟量按一天算').loc[2:4,['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3']]

df1 = pd.read_excel('中小学吸烟报告(数据来源：湖南学校数据).xls',sheet_name='购买吸烟的价格区间').loc[2:4,['Unnamed: 0','Unnamed: 1','Unnamed: 2']]

df2 = pd.read_excel('中小学吸烟报告(数据来源：湖南学校数据).xls',sheet_name='吸烟年龄占比').loc[2:4,['Unnamed: 0','Unnamed: 1','Unnamed: 2']]

df3 = pd.read_excel('中小学吸烟报告(数据来源：湖南学校数据).xls',sheet_name='是否在公共场合吸烟').loc[2:4,['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4']]

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
for i in df1['Unnamed: 0']:
    list_5.append(i)

list_6 = []
for i in df1['Unnamed: 1']:
    list_6.append(i)

list_7 = []
for i in df1['Unnamed: 2']:
    list_7.append(i)

list_8 = []
for i in df2['Unnamed: 0']:
    list_8.append(i)

list_9 = []
for i in df2['Unnamed: 1']:
    list_9.append(i)

list_10 = []
for i in df2['Unnamed: 2']:
    list_10.append(i)

list_11 = []
for i in df3['Unnamed: 0']:
    list_11.append(i)

list_12 = []
for i in df3['Unnamed: 1']:
    list_12.append(i)

list_13 = []
for i in df3['Unnamed: 2']:
    list_13.append(i)

list_14 = []
for i in df3['Unnamed: 3']:
    list_14.append(i)

list_15 = []
for i in df3['Unnamed: 4']:
    list_15.append(i)


c = (
    Polar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_schema(angleaxis_opts=opts.AngleAxisOpts(data=['','','',''], type_="category"))
    .add("吸烟次数", [list_1[0], list_2[0], list_3[0], list_4[0]], type_="bar", stack="stack0")
    .add("香烟价格区间", [list_5[0], list_6[0], list_7[0]], type_="bar", stack="stack0")
    .add("吸烟年龄", [list_8[0], list_9[0], list_10[0]], type_="bar", stack="stack0")
    .add("是否在公共场合吸烟", [list_11[0], list_12[0], list_13[0], list_14[0],list_15[0]], type_="bar", stack="stack0")
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="中学生吸烟报告",
            title_link="https://new.qq.com/omn/20201004/20201004A0098Z00.html",
            # pos_left="28%",
            # pos_top="5%",
            title_textstyle_opts=opts.TextStyleOpts(
                color="black",
                font_size=30,
            )
        )
    )
        .set_series_opts(
        linestyle_opts=opts.LineStyleOpts(
            width=2
        )
    )
    .render("polar_angleaxis.html")
)