import pymysql
import pandas as pd

from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar,Map,Pie,Line,WordCloud
import jieba

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    database='test'
)

sql = 'select * from test.movie'
df = pd.read_sql(sql,conn).loc[:,['title','time','country','type','comment','quote','number']]

def bar_time():
    #时间
    time_list = []
    x_data = []
    y_data = []
    for i in df['time']:
        i = str(i)
        time_list.append(i)
    d_time = {}
    for d in time_list:
        d_time[d] = d_time.get(d,0)+1

    ls = list(d_time.items())
    ls.sort(key=lambda x:x[0],reverse=False)
    for l in ls:
        x_data.append(l[0])
        y_data.append(l[1])

    c = (
        Bar({"theme": ThemeType.INFOGRAPHIC})
        .add_xaxis(x_data)
        .add_yaxis('电影数量',y_data,yaxis_index=0)
        .extend_axis(yaxis=opts.AxisOpts())
        .set_global_opts(
            datazoom_opts=opts.DataZoomOpts(),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    )
    return c


def number_bar():
    # 评分
    type_list = []
    x_data = []
    y_data = []
    for i in df['number']:
        i = str(i)
        type_list.append(i)
    d_type = {}
    for d in type_list:
        d_type[d] = d_type.get(d, 0) + 1

    ls = list(d_type.items())
    ls.sort(key=lambda x: x[1], reverse=False)
    for l in ls:
        x_data.append(l[0])
        y_data.append(l[1])
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(x_data)
            .add_yaxis("评分",y_data, label_opts=opts.LabelOpts(is_show=False))
            .reversal_axis()
            .set_global_opts(
            title_opts={"text": "电影评分数量"}

        )
    )
    return c


def type_pie():
    y_data = []
    x_data = []
    d_item = {}
    for i in df['type']:
        i = str(i)
        i = i.replace('\xa0','').split(' ')
        for j in i:
            if j != "":
                d_item[j] = d_item.get(j,0)+1
    ls = list(d_item.items())
    ls.sort(key=lambda x: x[1], reverse=False)
    for l in ls:
        x_data.append(l[0])
        y_data.append(l[1])
    data_pair = [(i, int(j)) for i, j in zip(x_data,y_data)]
    c = (
        Pie(init_opts=opts.InitOpts(width="1100px", height='500px'))
            .add(
            "类型",
            data_pair,
            center=['25%', '50%'],
            label_opts=opts.LabelOpts(is_show=True)
        )
            .set_colors(['SteelBlue', 'DarkCyan', 'DarkOrange', 'Salmon'])
            .set_global_opts(title_opts=opts.TitleOpts(title="电影类型占比图(单位：%)"),
                             legend_opts=opts.LegendOpts(is_show=False))
            .set_series_opts(tooltip_opts=opts.TooltipOpts(trigger='item', formatter="{a} <br/>{b}:{d}%"))

    )
    return c

def line_comment():
    comment_list = []
    for i in df['comment']:
        i = str(i)
        i = i.replace('人评价','')
        comment_list.append(i)

    name_list = []
    for j in df['title']:
        name_list.append(j)
    data_pair = [(i, int(j)) for i, j in zip(name_list, comment_list)]
    data_pair.sort(key=lambda x: x[1], reverse=True)
    data_pair = data_pair[0:15]
    x_data = []
    y_data = []
    for d in data_pair:
        x_data.append(d[0])
        y_data.append(d[1])

    c = (
            Line(init_opts=opts.InitOpts(width="1300px", height="600px"))
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
                series_name="评论人数",
                symbol="emptyCircle",
                is_symbol_show=False,
                color="#d14a61",
                y_axis=y_data,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=2)
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="前15部最多评论的电影"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,axisline_opts=opts.AxisLineOpts(
                        is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                    )),
            )

    )
    return c


def word():
    # 读入停用词表
    stop_words = []
    with open("stopwords_cn.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())
    d = {}
    for i in df['quote']:
        i = i.replace('。','').replace('，','').replace('！','').replace('？','').replace('“','').replace('《','').replace('——','').replace('~','').replace('+','')
        fenchi = jieba.lcut(i)
        for fen in fenchi:
            if fen not in stop_words and len(fen) >=2:
                d[fen] = d.get(fen, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[1], reverse=True)

    c = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
        .add(series_name="", data_pair=ls, word_size_range=[8, 88])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=32)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    return c


def map_country():
    y_data = []
    x_data = []
    d_item = {}
    for i in df['country']:
        i = str(i)
        i = i.replace('\xa0', '').replace('1964(中国大陆)','中国').replace('中国大陆','中国').replace('中国香港','中国').replace('中国台湾','中国').split(' ')
        for j in i:
            if j != "":
                d_item[j] = d_item.get(j, 0) + 1
    ls = list(d_item.items())
    ls.sort(key=lambda x: x[1], reverse=False)
    for l in ls:
        x_data.append(l[0])
        y_data.append(l[1])
    with open('国家英文.txt', 'r', encoding='utf-8')as f:
        content = f.readlines()

    list2 = []
    for c in content:
        c = c.strip('\n')
        list2.append(c)

    list3 = []
    for i in range(len(x_data)):
        l = x_data[i]
        for j in range(len(list2)):
            k = list2[j]
            if l == k:
                list3.append(list2[j - 2])


    w = (
        Map()
            .add("", [list(z) for z in zip(list3, y_data)], "world", label_opts=opts.LabelOpts(is_show=False),
                 is_map_symbol_show=False, )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="电影分布所在的国家",
                                      pos_left="40%", pos_top="5%"),
            visualmap_opts=opts.VisualMapOpts(max_=110),
        )
    )
    return w



