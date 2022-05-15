from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
import pandas as pd


def data1():
    #读取国内的文本内容
    df1 = pd.read_csv('./国外-桂林/餐饮/情感分析.csv')
    #设置排序，按照category这一列，从小到大进行排序
    df1 = df1.sort_values(by=['Category'],ascending=False)
    #设置一个字典
    d = {}
    #把内容保存为字典
    for j,k in zip(df1['Category'],df1['Count']):
        d[j] = k

    try:
        positive = d['Positive']
    except:
        positive = 0

    try:
        neutral = d['Neutral']
    except:
        neutral = 0

    try:
        negative = d['Negative']
    except:
        negative = 0

    list_data = []

    #计算正向负向中立的占比情况
    Positive = '%0.2lf' %(positive / (positive + neutral + negative))
    list_data.append(float(Positive))
    Neutral = '%0.2lf' % (neutral / (positive + neutral + negative))
    list_data.append(float(Neutral))
    Negative = '%0.2lf' % (negative / (positive + neutral + negative))
    list_data.append(float(Negative))

    #传入到一个新的字典里面
    list1 = []
    for i in list_data:
        d1 = {
            "value": int(i * 100), "percent": i
        }
        list1.append(d1)

    return list1


def data2():
    df1 = pd.read_csv('./国外-桂林/出行/情感分析.csv')
    df1 = df1.sort_values(by=['Category'],ascending=False)
    d = {}
    for j,k in zip(df1['Category'],df1['Count']):
        d[j] = k

    try:
        positive = d['Positive']
    except:
        positive = 0

    try:
        neutral = d['Neutral']
    except:
        neutral = 0

    try:
        negative = d['Negative']
    except:
        negative = 0

    list_data = []

    Positive = '%0.2lf' %(positive / (positive + neutral + negative))
    list_data.append(float(Positive))
    Neutral = '%0.2lf' % (neutral / (positive + neutral + negative))
    list_data.append(float(Neutral))
    Negative = '%0.2lf' % (negative / (positive + neutral + negative))
    list_data.append(float(Negative))

    list1 = []
    for i in list_data:
        d1 = {
            "value": int(i * 100), "percent": i
        }
        list1.append(d1)

    return list1


def data3():
    df1 = pd.read_csv('./国外-桂林/购物/情感分析.csv')
    df1 = df1.sort_values(by=['Category'],ascending=False)
    d = {}
    for j,k in zip(df1['Category'],df1['Count']):
        d[j] = k

    try:
        positive = d['Positive']
    except:
        positive = 0

    try:
        neutral = d['Neutral']
    except:
        neutral = 0

    try:
        negative = d['Negative']
    except:
        negative = 0

    list_data = []

    Positive = '%0.2lf' %(positive / (positive + neutral + negative))
    list_data.append(float(Positive))
    Neutral = '%0.2lf' % (neutral / (positive + neutral + negative))
    list_data.append(float(Neutral))
    Negative = '%0.2lf' % (negative / (positive + neutral + negative))
    list_data.append(float(Negative))

    list1 = []
    for i in list_data:
        d1 = {
            "value": int(i * 100), "percent": i
        }
        list1.append(d1)

    return list1


def data4():
    df1 = pd.read_csv('./国外-桂林/景点/情感分析.csv')
    df1 = df1.sort_values(by=['Category'],ascending=False)
    d = {}
    for j,k in zip(df1['Category'],df1['Count']):
        d[j] = k

    try:
        positive = d['Positive']
    except:
        positive = 0

    try:
        neutral = d['Neutral']
    except:
        neutral = 0

    try:
        negative = d['Negative']
    except:
        negative = 0

    list_data = []

    Positive = '%0.2lf' %(positive / (positive + neutral + negative))
    list_data.append(float(Positive))
    Neutral = '%0.2lf' % (neutral / (positive + neutral + negative))
    list_data.append(float(Neutral))
    Negative = '%0.2lf' % (negative / (positive + neutral + negative))
    list_data.append(float(Negative))

    list1 = []
    for i in list_data:
        d1 = {
            "value": int(i * 100), "percent": i
        }
        list1.append(d1)

    return list1


def data5():
    df1 = pd.read_csv('./国外-桂林/游玩/情感分析.csv')
    df1 = df1.sort_values(by=['Category'],ascending=False)
    d = {}
    for j,k in zip(df1['Category'],df1['Count']):
        d[j] = k

    try:
        positive = d['Positive']
    except:
        positive = 0

    try:
        neutral = d['Neutral']
    except:
        neutral = 0

    try:
        negative = d['Negative']
    except:
        negative = 0

    list_data = []

    Positive = '%0.2lf' %(positive / (positive + neutral + negative))
    list_data.append(float(Positive))
    Neutral = '%0.2lf' % (neutral / (positive + neutral + negative))
    list_data.append(float(Neutral))
    Negative = '%0.2lf' % (negative / (positive + neutral + negative))
    list_data.append(float(Negative))

    list1 = []
    for i in list_data:
        d1 = {
            "value": int(i * 100), "percent": i
        }
        list1.append(d1)

    return list1


def data6():
    df1 = pd.read_csv('./国外-桂林/住宿/情感分析.csv')
    df1 = df1.sort_values(by=['Category'],ascending=False)
    d = {}
    for j,k in zip(df1['Category'],df1['Count']):
        d[j] = k

    try:
        positive = d['Positive']
    except:
        positive = 0

    try:
        neutral = d['Neutral']
    except:
        neutral = 0

    try:
        negative = d['Negative']
    except:
        negative = 0

    list_data = []

    Positive = '%0.2lf' %(positive / (positive + neutral + negative))
    list_data.append(float(Positive))
    Neutral = '%0.2lf' % (neutral / (positive + neutral + negative))
    list_data.append(float(Neutral))
    Negative = '%0.2lf' % (negative / (positive + neutral + negative))
    list_data.append(float(Negative))

    list1 = []
    for i in list_data:
        d1 = {
            "value": int(i * 100), "percent": i
        }
        list1.append(d1)

    return list1


list1 = data1()
list2 = data2()
list3 = data3()
list4 = data4()
list5 = data5()
list6 = data6()

#设置正向的列表样式
pos_list = [
    {'value': list1[0]['value'], 'percent': list1[0]['percent']},
    {'value': list2[0]['value'], 'percent': list2[0]['percent']},
    {'value': list3[0]['value'], 'percent': list3[0]['percent']},
    {'value': list4[0]['value'], 'percent': list4[0]['percent']},
    {'value': list5[0]['value'], 'percent': list5[0]['percent']},
    {'value': list6[0]['value'], 'percent': list6[0]['percent']},
]
#设置中立的列表样式
neu_list = [
    {'value': list1[1]['value'], 'percent': list1[1]['percent']},
    {'value': list2[1]['value'], 'percent': list2[1]['percent']},
    {'value': list3[1]['value'], 'percent': list3[1]['percent']},
    {'value': list4[1]['value'], 'percent': list4[1]['percent']},
    {'value': list5[1]['value'], 'percent': list5[1]['percent']},
    {'value': list6[1]['value'], 'percent': list6[1]['percent']},
]
#设置负向列表的样式
neg_list = [
    {'value': list1[2]['value'], 'percent': list1[2]['percent']},
    {'value': list2[2]['value'], 'percent': list2[2]['percent']},
    {'value': list3[2]['value'], 'percent': list3[2]['percent']},
    {'value': list4[2]['value'], 'percent': list4[2]['percent']},
    {'value': list5[2]['value'], 'percent': list5[2]['percent']},
    {'value': list6[2]['value'], 'percent': list6[2]['percent']},
]


def gn_data1():
    #读取国内的文档数据
    df = pd.read_csv('./国内-桂林/清洗好的文本内容.csv')
    #先确定数据的样式
    keyword1 = '食物'
    keyword2 = '餐饮'
    keyword3 = '吃的'
    keyword4 = '美食'
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                        (df['正文'].str.contains('{}'.format(keyword3), case=False)) | (
                    df['正文'].str.contains('{}'.format(keyword4), case=False)))]
    text = new_df['情感分值']
    #读取每一类出现的数量，并且按照index进行排序
    new_data = text.value_counts()
    new_data = new_data.sort_index()
    #设置字典样式
    d = {}
    #往字典里面的添加样式
    for j, k in zip(new_data.index, new_data.values):
        d[j] = k
    
    try:
        positive = d[1]
    except:
        positive = 0
    
    try:
        neutral = d[2]
    except:
        neutral = 0

    try:
        negative = d[0]
    except:
        negative = 0
    #计算正向负向中立的占比情况
    list_data = []
    try:
        Positive = '%0.2lf' % (positive / (positive + neutral + negative))
    except:
        Positive = 0
    list_data.append(float(Positive))
    try:
        Neutral = '%0.2lf' % (neutral / (positive + neutral + negative))
    except:
        Neutral = 0
    list_data.append(float(Neutral))
    try:
        Negative = '%0.2lf' % (negative / (positive + neutral + negative))
    except:
        Negative = 0
    list_data.append(float(Negative))
    #最后构建一个新的样式
    list1 = []
    for i in list_data:
        d1 = {
            "value": int(i * 100), "percent": i
        }
        list1.append(d1)

    return list1


def gn_data2():
    df = pd.read_csv('./国内-桂林/清洗好的文本内容.csv')
    keyword1 = '出行'
    keyword2 = '公交'
    keyword3 = '交通'
    keyword4 = '小车'
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                        (df['正文'].str.contains('{}'.format(keyword3), case=False)) | (
                    df['正文'].str.contains('{}'.format(keyword4), case=False)))]
    text = new_df['情感分值']
    new_data = text.value_counts()
    new_data = new_data.sort_index()
    d = {}
    for j, k in zip(new_data.index, new_data.values):
        d[j] = k

    try:
        positive = d[1]
    except:
        positive = 0

    try:
        neutral = d[2]
    except:
        neutral = 0

    try:
        negative = d[0]
    except:
        negative = 0

    list_data = []
    try:
        Positive = '%0.2lf' % (positive / (positive + neutral + negative))
    except:
        Positive = 0
    list_data.append(float(Positive))
    try:
        Neutral = '%0.2lf' % (neutral / (positive + neutral + negative))
    except:
        Neutral = 0
    list_data.append(float(Neutral))
    try:
        Negative = '%0.2lf' % (negative / (positive + neutral + negative))
    except:
        Negative = 0
    list_data.append(float(Negative))

    list1 = []
    for i in list_data:
        d1 = {
            "value": int(i * 100), "percent": i
        }
        list1.append(d1)

    return list1


def gn_data3():
    df = pd.read_csv('./国内-桂林/清洗好的文本内容.csv')
    keyword1 = '购物'
    keyword2 = '商场'
    keyword3 = '买东西'
    keyword4 = '打卡'
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                        (df['正文'].str.contains('{}'.format(keyword3), case=False)) | (
                    df['正文'].str.contains('{}'.format(keyword4), case=False)))]
    text = new_df['情感分值']
    new_data = text.value_counts()
    new_data = new_data.sort_index()
    d = {}
    for j, k in zip(new_data.index, new_data.values):
        d[j] = k

    try:
        positive = d[1]
    except:
        positive = 0

    try:
        neutral = d[2]
    except:
        neutral = 0

    try:
        negative = d[0]
    except:
        negative = 0

    list_data = []
    try:
        Positive = '%0.2lf' % (positive / (positive + neutral + negative))
    except:
        Positive = 0
    list_data.append(float(Positive))
    try:
        Neutral = '%0.2lf' % (neutral / (positive + neutral + negative))
    except:
        Neutral = 0
    list_data.append(float(Neutral))
    try:
        Negative = '%0.2lf' % (negative / (positive + neutral + negative))
    except:
        Negative = 0
    list_data.append(float(Negative))

    list1 = []
    for i in list_data:
        d1 = {
            "value": int(i * 100), "percent": i
        }
        list1.append(d1)

    return list1


def gn_data4():
    df = pd.read_csv('./国内-桂林/清洗好的文本内容.csv')
    keyword1 = '景点'
    keyword2 = '景色'
    keyword3 = '风景'
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                    (df['正文'].str.contains('{}'.format(keyword3), case=False)))]
    text = new_df['情感分值']
    new_data = text.value_counts()
    new_data = new_data.sort_index()
    d = {}
    for j, k in zip(new_data.index, new_data.values):
        d[j] = k

    try:
        positive = d[1]
    except:
        positive = 0

    try:
        neutral = d[2]
    except:
        neutral = 0

    try:
        negative = d[0]
    except:
        negative = 0

    list_data = []
    try:
        Positive = '%0.2lf' % (positive / (positive + neutral + negative))
    except:
        Positive = 0
    list_data.append(float(Positive))
    try:
        Neutral = '%0.2lf' % (neutral / (positive + neutral + negative))
    except:
        Neutral = 0
    list_data.append(float(Neutral))
    try:
        Negative = '%0.2lf' % (negative / (positive + neutral + negative))
    except:
        Negative = 0
    list_data.append(float(Negative))

    list1 = []
    for i in list_data:
        d1 = {
            "value": int(i * 100), "percent": i
        }
        list1.append(d1)

    return list1


def gn_data5():
    df = pd.read_csv('./国内-桂林/清洗好的文本内容.csv')
    keyword1 = '游玩'
    keyword2 = '好玩'
    keyword3 = '玩耍'
    keyword4 = '旅游'
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                        (df['正文'].str.contains('{}'.format(keyword3), case=False)) | (
                    df['正文'].str.contains('{}'.format(keyword4), case=False)))]
    text = new_df['情感分值']
    new_data = text.value_counts()
    new_data = new_data.sort_index()
    d = {}
    for j, k in zip(new_data.index, new_data.values):
        d[j] = k

    try:
        positive = d[1]
    except:
        positive = 0

    try:
        neutral = d[2]
    except:
        neutral = 0

    try:
        negative = d[0]
    except:
        negative = 0

    list_data = []
    try:
        Positive = '%0.2lf' % (positive / (positive + neutral + negative))
    except:
        Positive = 0
    list_data.append(float(Positive))
    try:
        Neutral = '%0.2lf' % (neutral / (positive + neutral + negative))
    except:
        Neutral = 0
    list_data.append(float(Neutral))
    try:
        Negative = '%0.2lf' % (negative / (positive + neutral + negative))
    except:
        Negative = 0
    list_data.append(float(Negative))

    list1 = []
    for i in list_data:
        d1 = {
            "value": int(i * 100), "percent": i
        }
        list1.append(d1)

    return list1

def gn_data6():
    df = pd.read_csv('./国内-桂林/清洗好的文本内容.csv')
    keyword1 = '住宿'
    keyword2 = '居住'
    keyword3 = '酒店'
    keyword4 = '民宿'
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                        (df['正文'].str.contains('{}'.format(keyword3), case=False)) | (
                    df['正文'].str.contains('{}'.format(keyword4), case=False)))]
    text = new_df['情感分值']
    new_data = text.value_counts()
    new_data = new_data.sort_index()
    d = {}
    for j, k in zip(new_data.index, new_data.values):
        d[j] = k

    try:
        positive = d[1]
    except:
        positive = 0

    try:
        neutral = d[2]
    except:
        neutral = 0

    try:
        negative = d[0]
    except:
        negative = 0

    list_data = []
    try:
        Positive = '%0.2lf' % (positive / (positive + neutral + negative))
    except:
        Positive = 0
    list_data.append(float(Positive))
    try:
        Neutral = '%0.2lf' % (neutral / (positive + neutral + negative))
    except:
        Neutral = 0
    list_data.append(float(Neutral))
    try:
        Negative = '%0.2lf' % (negative / (positive + neutral + negative))
    except:
        Negative = 0
    list_data.append(float(Negative))

    list1 = []
    for i in list_data:
        d1 = {
            "value": int(i * 100), "percent": i
        }
        list1.append(d1)

    return list1

#获取国内的最终数据
gn_list1 = gn_data1()
gn_list2 = gn_data2()
gn_list3 = gn_data3()
gn_list4 = gn_data4()
gn_list5 = gn_data5()
gn_list6 = gn_data6()

#设置正向的数据样式
gn_pos_list = [
    {'value': gn_list1[0]['value'], 'percent': gn_list1[0]['percent']},
    {'value': gn_list2[0]['value'], 'percent': gn_list2[0]['percent']},
    {'value': gn_list3[0]['value'], 'percent': gn_list3[0]['percent']},
    {'value': gn_list4[0]['value'], 'percent': gn_list4[0]['percent']},
    {'value': gn_list5[0]['value'], 'percent': gn_list5[0]['percent']},
    {'value': gn_list6[0]['value'], 'percent': gn_list6[0]['percent']},
]
#设置中立的数据样式
gn_neu_list = [
    {'value': gn_list1[1]['value'], 'percent': gn_list1[1]['percent']},
    {'value': gn_list2[1]['value'], 'percent': gn_list2[1]['percent']},
    {'value': gn_list3[1]['value'], 'percent': gn_list3[1]['percent']},
    {'value': gn_list4[1]['value'], 'percent': gn_list4[1]['percent']},
    {'value': gn_list5[1]['value'], 'percent': gn_list5[1]['percent']},
    {'value': gn_list6[1]['value'], 'percent': gn_list6[1]['percent']},
]
#设置负向的数据样式
gn_neg_list = [
    {'value': gn_list1[2]['value'], 'percent': gn_list1[2]['percent']},
    {'value': gn_list2[2]['value'], 'percent': gn_list2[2]['percent']},
    {'value': gn_list3[2]['value'], 'percent': gn_list3[2]['percent']},
    {'value': gn_list4[2]['value'], 'percent': gn_list4[2]['percent']},
    {'value': gn_list5[2]['value'], 'percent': gn_list5[2]['percent']},
    {'value': gn_list6[2]['value'], 'percent': gn_list6[2]['percent']},
]


c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    #设置x轴的内容
    .add_xaxis(['餐饮', '出行', '购物','景点','游玩','住宿'])
    #设置y轴的内容
    .add_yaxis("gn_pos", gn_pos_list, stack="stack1", category_gap="50%")
    .add_yaxis("gn_neu", gn_neu_list, stack="stack1", category_gap="50%")
    .add_yaxis("gn_neg", gn_neg_list, stack="stack1", category_gap="50%")
    .add_yaxis("pos", pos_list, stack="stack2", category_gap="50%")
    .add_yaxis("neu", neu_list, stack="stack2", category_gap="50%")
    .add_yaxis("neg", neg_list, stack="stack2", category_gap="50%")
    #设置图片样式
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            is_show=False,
            formatter=JsCode(
                "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
            ),
        )
    )
    #设置标题
    .set_global_opts(
        title_opts={"text": "国内外桂林6个维度对比", "subtext": "gn指的是国内"}
    )
    #导出样式结果
    .render("情感分析对比.html")
)
