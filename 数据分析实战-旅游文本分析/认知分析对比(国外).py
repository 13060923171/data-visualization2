import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
from pyecharts.globals import ThemeType
from multiprocessing import Process
import multiprocessing


def catering():
    #读取文档
    df = pd.read_csv('./国外-桂林/餐饮/词频.csv',error_bad_lines=False)
    #读取关键词，把关键词转化为列表的形式
    data = [(i,int(j)) for i,j in zip(df['Keyword/Phrase'],df['Occurences'])]
    #生成词云图
    c = (
        #词云的类型
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            #词云的分布状态
            .add("", data, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            #词云的标题
            .set_global_opts(title_opts=opts.TitleOpts(title="Guilin-catering"))
            .render("./词云图(国外)/Guilin-catering.html")
    )


def trip():
    df = pd.read_csv('./国外-桂林/出行/词频.csv',error_bad_lines=False)
    data = [(i,int(j)) for i,j in zip(df['Keyword/Phrase'],df['Occurences'])]
    c = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add("", data, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="Guilin-trip"))
            .render("./词云图(国外)/Guilin-trip.html")
    )


def shopping():
    df = pd.read_csv('./国外-桂林/购物/词频.csv',error_bad_lines=False)
    data = [(i,int(j)) for i,j in zip(df['Keyword/Phrase'],df['Occurences'])]
    c = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add("", data, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="Guilin-shopping"))
            .render("./词云图(国外)/Guilin-shopping.html")
    )


def scenic():
    df = pd.read_csv('./国外-桂林/景点/词频.csv',error_bad_lines=False)
    data = [(i,int(j)) for i,j in zip(df['Keyword/Phrase'],df['Occurences'])]
    c = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add("", data, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="Guilin-scenic"))
            .render("./词云图(国外)/Guilin-scenic.html")
    )


def play():
    df = pd.read_csv('./国外-桂林/游玩/词频.csv',error_bad_lines=False)
    data = [(i,int(j)) for i,j in zip(df['Keyword/Phrase'],df['Occurences'])]
    c = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add("", data, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="Guilin-play"))
            .render("./词云图(国外)/Guilin-play.html")
    )


def stay():
    df = pd.read_csv('./国外-桂林/住宿/词频.csv',error_bad_lines=False)
    data = [(i,int(j)) for i,j in zip(df['Keyword/Phrase'],df['Occurences'])]
    c = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add("", data, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="Guilin-stay"))
            .render("./词云图(国外)/Guilin-stay.html")
    )


def total():
    df1 = pd.read_csv('./国外-桂林/餐饮/词频.csv', error_bad_lines=False)
    df2 = pd.read_csv('./国外-桂林/出行/词频.csv', error_bad_lines=False)
    df3 = pd.read_csv('./国外-桂林/购物/词频.csv', error_bad_lines=False)
    df4 = pd.read_csv('./国外-桂林/景点/词频.csv', error_bad_lines=False)
    df5 = pd.read_csv('./国外-桂林/游玩/词频.csv', error_bad_lines=False)
    df6 = pd.read_csv('./国外-桂林/住宿/词频.csv', error_bad_lines=False)
    df7 = pd.concat([df1,df2,df3,df4,df5,df6],axis=0)
    data = [(i, int(j)) for i, j in zip(df7['Keyword/Phrase'], df7['Occurences'])]
    c = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add("", data, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="Guilin-total"))
            .render("./词云图(国外)/Guilin-total.html")
    )


if __name__ == '__main__':
    #采用多进程的方式一起处理，这样做的目的就是为了运算速度提升，节省时间
    process = [multiprocessing.Process(target=catering),
               multiprocessing.Process(target=trip),
               multiprocessing.Process(target=shopping),
               multiprocessing.Process(target=scenic),
               multiprocessing.Process(target=play),
               multiprocessing.Process(target=stay),
               multiprocessing.Process(target=total)]
    [p.start() for p in process]  # 开启了两个进程
    [p.join() for p in process]  # 等待两个进程依次结束



