from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
import pandas as pd


def data1():
    #获取文本的数量
    df1 = pd.read_csv('./国外-桂林/餐饮/内容.csv',encoding="UTF-16",sep='\t')
    return len(df1)

def data2():
    df1 = pd.read_csv('./国外-桂林/出行/内容.csv',encoding="UTF-16",sep='\t')
    return len(df1)

def data3():
    df1 = pd.read_csv('./国外-桂林/购物/内容.csv',encoding="UTF-16",sep='\t')
    return len(df1)

def data4():
    df1 = pd.read_csv('./国外-桂林/景点/内容.csv',encoding="UTF-16",sep='\t')
    return len(df1)

def data5():
    df1 = pd.read_csv('./国外-桂林/游玩/内容.csv',encoding="UTF-16",sep='\t')
    return len(df1)

def data6():
    df1 = pd.read_csv('./国外-桂林/住宿/内容.csv',encoding="UTF-16",sep='\t')
    return len(df1)


def gn_data1():
    #先进行文本筛选，确定文本的类型
    df = pd.read_csv('./国内-桂林/清洗好的文本内容.csv')
    keyword1 = '食物'
    keyword2 = '餐饮'
    keyword3 = '吃的'
    keyword4 = '美食'
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                        (df['正文'].str.contains('{}'.format(keyword3), case=False)) | (
                    df['正文'].str.contains('{}'.format(keyword4), case=False)))]
    text = new_df['情感分值']
    #再来获取文本的数量
    return len(text)




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
    return len(text)


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
    return len(text)

def gn_data4():
    df = pd.read_csv('./国内-桂林/清洗好的文本内容.csv')
    keyword1 = '景点'
    keyword2 = '景色'
    keyword3 = '风景'
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                    (df['正文'].str.contains('{}'.format(keyword3), case=False)))]
    text = new_df['情感分值']
    return len(text)


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
    return len(text)


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
    return len(text)

#读取不同文本类型的数量，国外版
number1 = data1()
number2 = data2()
number3 = data3()
number4 = data4()
number5 = data5()
number6 = data6()
#读取不同文本类型的数量，国内版
gn_number1 = gn_data1()
gn_number2 = gn_data2()
gn_number3 = gn_data3()
gn_number4 = gn_data4()
gn_number5 = gn_data5()
gn_number6 = gn_data6()
#设定x轴的名称
x_data = ['餐饮', '出行', '购物','景点','游玩','住宿']
#设定y轴的名称
y_data = [number1,number2,number3,number4,number5,number6]
#设定y轴的名称
y_data1 = [gn_number1,gn_number2,gn_number3,gn_number4,gn_number5,gn_number6]

c = (
    #设定主题颜色
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    #加入x轴的内容
    .add_xaxis(x_data)
    #加入y轴的内容
    .add_yaxis("国内", y_data)
    .add_yaxis("国外", y_data1)
    #倒转
    .reversal_axis()
    #设定位置
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    #设置标题
    .set_global_opts(title_opts=opts.TitleOpts(title="国内外不同维度谈论情况"))
    #打印出来
    .render("国内外不同维度谈论情况.html")
)
