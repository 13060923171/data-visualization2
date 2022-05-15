import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import Image
import stylecloud
import jieba
import jieba.posseg as pseg
from multiprocessing import Process
import multiprocessing
df = pd.read_csv('./国内-桂林/清洗好的文本内容.csv')
#设置停用词
stop_words = []
with open("./国内-桂林/stopwords_cn.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        stop_words.append(line.strip())
#新增无效词
new_stop_words = ['桂林','阳朔','漓江','酒店','西街','景区','梯田','景点','竹筏','时间','地方','小时']
stop_words.extend(new_stop_words)


def catering():
    #条件筛选，当出现这些关键词的时候，那么判断这一行是在说关于餐饮的
    keyword1 = '食物'
    keyword2 = '餐饮'
    keyword3 = '吃的'
    keyword4 = '美食'
    #条件筛选
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                            (df['正文'].str.contains('{}'.format(keyword3), case=False)) | (
                        df['正文'].str.contains('{}'.format(keyword4), case=False)))]
    #筛选好后的文本
    text = new_df['清洗文本']
    list_text = []
    for t in text:
        #把数据分开
        t = str(t).split(" ")
        for i in t:
            #再过滤一遍无效词
            if i not in stop_words:
                #添加到列表里面
                list_text.append(i)
    #     words = pseg.cut("{}".format(t))
    #     for word, flag in words:
    #         if word not in stop_words and len(word) >= 2:
    #             # 形容词统计
    #             if 'a' in flag or 'A' in flag:
    #                 list_text.append(word)
    #
    #然后传入词云图中，筛选最多的100个词
    stylecloud.gen_stylecloud(text=' '.join(list_text), max_words=100,
                              #不能有重复词
                              collocations=False,
                              #字体样式
                              font_path='simhei.ttf',
                              #图片形状
                              icon_name='fas fa-circle',
                              #图片大小
                              size=500,
                              # palette='matplotlib.Inferno_9',
                              #输出图片的名称和位置
                              output_name='./词云图/餐饮形象-词云图.png')
    #开始生成图片
    Image(filename='./词云图/餐饮形象-词云图.png')


def trip():
    keyword1 = '出行'
    keyword2 = '公交'
    keyword3 = '交通'
    keyword4 = '小车'
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                            (df['正文'].str.contains('{}'.format(keyword3), case=False)) | (
                        df['正文'].str.contains('{}'.format(keyword4), case=False)))]
    text = new_df['清洗文本']
    list_text = []
    for t in text:
        t = str(t).split(" ")
        for i in t:
            if i not in stop_words:
                list_text.append(i)
    #     words = pseg.cut("{}".format(t))
    #     for word, flag in words:
    #         if word not in stop_words and len(word) >= 2:
    #             # 形容词统计
    #             if 'a' in flag or 'A' in flag:
    #                 list_text.append(word)
    #
    stylecloud.gen_stylecloud(text=' '.join(list_text), max_words=100,
                              collocations=False,
                              font_path='simhei.ttf',
                              icon_name='fas fa-bomb',
                              size=500,
                              # palette='matplotlib.Inferno_9',
                              output_name='./词云图/出行形象-词云图.png')
    Image(filename='./词云图/出行形象-词云图.png')


def shopping():
    keyword1 = '购物'
    keyword2 = '商场'
    keyword3 = '买东西'
    keyword4 = '打卡'
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                        (df['正文'].str.contains('{}'.format(keyword3), case=False)) | (
                    df['正文'].str.contains('{}'.format(keyword4), case=False)))]
    text = new_df['清洗文本']
    list_text = []
    for t in text:
        t = str(t).split(" ")
        for i in t:
            if i not in stop_words:
                list_text.append(i)
    #     words = pseg.cut("{}".format(t))
    #     for word, flag in words:
    #         if word not in stop_words and len(word) >= 2:
    #             # 形容词统计
    #             if 'a' in flag or 'A' in flag:
    #                 list_text.append(word)
    #

    stylecloud.gen_stylecloud(text=' '.join(list_text), max_words=100,
                              collocations=False,
                              font_path='simhei.ttf',
                              icon_name='fas fa-bone',
                              size=500,
                              # palette='matplotlib.Inferno_9',
                              output_name='./词云图/购物形象-词云图.png')
    Image(filename='./词云图/购物形象-词云图.png')


def scenic():
    keyword1 = '景点'
    keyword2 = '景色'
    keyword3 = '风景'
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                            (df['正文'].str.contains('{}'.format(keyword3), case=False)))]
    text = new_df['清洗文本']
    list_text = []
    for t in text:
        t = str(t).split(" ")
        for i in t:
            if i not in stop_words:
                list_text.append(i)
    #     words = pseg.cut("{}".format(t))
    #     for word, flag in words:
    #         if word not in stop_words and len(word) >= 2:
    #             # 形容词统计
    #             if 'a' in flag or 'A' in flag:
    #                 list_text.append(word)
    #

    stylecloud.gen_stylecloud(text=' '.join(list_text), max_words=100,
                              collocations=False,
                              font_path='simhei.ttf',
                              icon_name='fas fa-book',
                              size=500,
                              # palette='matplotlib.Inferno_9',
                              output_name='./词云图/景点形象-词云图.png')
    Image(filename='./词云图/景点形象-词云图.png')


def play():
    keyword1 = '游玩'
    keyword2 = '好玩'
    keyword3 = '玩耍'
    keyword4 = '旅游'
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                            (df['正文'].str.contains('{}'.format(keyword3), case=False)) | (
                        df['正文'].str.contains('{}'.format(keyword4), case=False)))]
    text = new_df['清洗文本']
    list_text = []
    for t in text:
        t = str(t).split(" ")
        for i in t:
            if i not in stop_words:
                list_text.append(i)
    #     words = pseg.cut("{}".format(t))
    #     for word, flag in words:
    #         if word not in stop_words and len(word) >= 2:
    #             # 形容词统计
    #             if 'a' in flag or 'A' in flag:
    #                 list_text.append(word)
    #

    stylecloud.gen_stylecloud(text=' '.join(list_text), max_words=100,
                              collocations=False,
                              font_path='simhei.ttf',
                              icon_name='fas fa-box',
                              size=500,
                              # palette='matplotlib.Inferno_9',
                              output_name='./词云图/游玩形象-词云图.png')
    Image(filename='./词云图/游玩形象-词云图.png')

def stay():
    keyword1 = '住宿'
    keyword2 = '居住'
    keyword3 = '酒店'
    keyword4 = '民宿'
    new_df = df[((df['正文'].str.contains('{}'.format(keyword1), case=False)) | (
        df['正文'].str.contains('{}'.format(keyword2), case=False))) | (
                            (df['正文'].str.contains('{}'.format(keyword3), case=False)) | (
                        df['正文'].str.contains('{}'.format(keyword4), case=False)))]
    text = new_df['清洗文本']
    list_text = []
    for t in text:
        t = str(t).split(" ")
        for i in t:
            if i not in stop_words:
                list_text.append(i)
    #     words = pseg.cut("{}".format(t))
    #     for word, flag in words:
    #         if word not in stop_words and len(word) >= 2:
    #             # 形容词统计
    #             if 'a' in flag or 'A' in flag:
    #                 list_text.append(word)
    #

    stylecloud.gen_stylecloud(text=' '.join(list_text), max_words=100,
                              collocations=False,
                              font_path='simhei.ttf',
                              icon_name='fas fa-moon',
                              size=500,
                              # palette='matplotlib.Inferno_9',
                              output_name='./词云图/住宿形象-词云图.png')
    Image(filename='./词云图/住宿形象-词云图.png')


if __name__ == '__main__':
    # catering()
    # trip()
    # shopping()
    # scenic()
    # play()
    # stay()
    # 采用多进程的方式一起处理，这样做的目的就是为了运算速度提升，节省时间
    process = [multiprocessing.Process(target=catering),
               multiprocessing.Process(target=trip),
               multiprocessing.Process(target=shopping),
               multiprocessing.Process(target=scenic),
               multiprocessing.Process(target=play),
               multiprocessing.Process(target=stay)]
    [p.start() for p in process]  # 开启了两个进程
    [p.join() for p in process]  # 等待两个进程依次结束
