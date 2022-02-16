import pandas as pd
import re
import jieba
#可视化库
from snownlp import SnowNLP
from snownlp import sentiment
import stylecloud
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
import time
from collections import Counter
import matplotlib.pyplot as plt
data1 = pd.read_excel('./data/数据(1).xlsx')
data2 = pd.read_excel('./data/数据(2).xlsx')
data3 = pd.read_excel('./data/数据(3).xlsx')
data4 = pd.read_excel('./data/数据(4).xlsx')
data5 = pd.read_excel('./data/数据(5).xlsx')
data6 = pd.read_excel('./data/数据(6).xlsx')
data7 = pd.read_excel('./data/数据(7).xlsx')
data8 = pd.read_excel('./data/数据(8).xlsx')
sum_data = pd.concat([data1,data2,data3,data4,data5,data6,data7,data8])


#删除空值和重复项
sum_data.dropna(how='any', inplace=True)
sum_data.drop_duplicates(keep='first', inplace=True)


#删除标点符号
def clear_characters(text):
    return re.sub('\W', '', text)


sum_data['comment_text'] = sum_data['comment_text'].astype(str)
sum_data['comment_text'] = sum_data['comment_text'].apply(clear_characters)


#定义机械压缩函数
def yasuo(st):
    for i in range(1,int(len(st)/2)+1):
        for j in range(len(st)):
            if st[j:j+i] == st[j+i:j+2*i]:
                k = j + i
                while st[k:k+i] == st[k+i:k+2*i] and k<len(st):
                    k = k + i
                st = st[:j] + st[k:]
    return st


def train_model(texts):
    comm = str(texts)
    if comm != "":
        text = re.sub(r'(?:回复)?(?://)?@[\w\u2E80-\u9FFF]+:?|\[\w+\]', ',',comm)
        score = SnowNLP(text)
        return score.sentiments


sum_data['comment_text'] = sum_data['comment_text'].apply(yasuo)
sum_data['data_emotion'] = sum_data['comment_text'].apply(train_model)

df = sum_data
df.create_time = pd.to_datetime(sum_data.create_time)
df.index = df.create_time
df1 = df.data_emotion.resample('D').mean()
x_data = list(df1.index)
y_data = list(df1.values)
x_data1 = []
for x in x_data:
    x1 = pd.to_datetime(x)
    x1 = str(x1)
    x1 = x1.split(" ")
    x_data1.append(x1[0])


def get_line1():
    c = (

        Line(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
            .add_xaxis(xaxis_data=x_data1)
            .add_yaxis(
            series_name="",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#ADFF2F",
            y_axis=y_data,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="时间情感趋势"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False, axisline_opts=opts.AxisLineOpts(
                is_on_zero=False,
            )),
        )
    )
    return c


