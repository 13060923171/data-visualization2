import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from imageio import imread
import nltk
import re
from nltk.stem.snowball import SnowballStemmer  # 返回词语的原型，去掉ing等
stemmer = SnowballStemmer("english")

stop_words = []
with open("常用英文停用词(NLP处理英文必备)stopwords.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        stop_words.append(line.strip())

new_stop_words = []
with open("新增停用词.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        new_stop_words.append(line.strip())


def main1():
    # 绘制词云图
    df = pd.read_csv('./output/清洗完毕的文档.csv')
    sum_cotent = []
    df['comment'] = df['comment'].astype('str')
    stop_words.extend(new_stop_words)
    for d in df['comment']:
        d = str(d).split(" ")
        for i in d:
            if i not in stop_words:
                sum_cotent.append(i)
    counts = {}
    for s in sum_cotent:
        counts[s] = counts.get(s,0)+1
    ls = list(counts.items())
    ls.sort(key=lambda x:x[1],reverse=True)
    x_data = []
    y_data = []
    for key,values in ls[:100]:
        x_data.append(key)
        y_data.append(values)

    df1 = pd.DataFrame()
    df1['word'] = x_data
    df1['counts'] = y_data
    df1.to_csv('./output/高频词TOP100.csv',encoding='utf-8-sig')

    contents_list = " ".join(sum_cotent)

    # 制作词云图，collocations避免词云图中词的重复，mask定义词云图的形状，图片要有背景色
    wc = WordCloud(
        collocations=False,
        max_words=100,
        background_color="white",
        font_path=r"C:\Windows\Fonts\simhei.ttf",
        stopwords=stop_words,
        width=1080, height=1920, random_state=42,
        mask=imread('./input/image.jpg', pilmode="RGB"))
    wc.generate(contents_list)
    # 要读取的形状的图片
    wc.to_file("./output/热词-云图.png")


if __name__ == '__main__':
    main1()


