import jieba
import pandas as pd
import stylecloud
from IPython.display import Image
import matplotlib.pyplot as plt
df = pd.read_csv('../data/疫情-分类后的文本.csv')

def get_cut_words(content_series):
    # 读入停用词表
    stop_words = []

    with open("../data/stopwords_cn.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())

    # 分词
    word_num = jieba.lcut(content_series['content'].str.cat(sep='。'), cut_all=False)

    # 条件筛选
    word_num_selected = [i for i in word_num if i not in stop_words and len(i) >= 2]
    return word_num_selected

def content_number(x):
    df = x
    print(len(df))
    return len(df)

compan = df.groupby('聚类结果').apply(get_cut_words)
number = df.groupby('聚类结果').apply(content_number)
y_data1 = list(compan.values)[0]
y_data2 = list(compan.values)[1]
y_data3 = list(compan.values)[2]

y_data11 = list(number.values)[0]
y_data21 = list(number.values)[1]
y_data31 = list(number.values)[2]

x_data = ['0类','1类','2类']
y_data = [int(y_data11),int(y_data21),int(y_data31)]

plt.style.use('ggplot')
plt.figure(figsize=(12,9),dpi=300)
plt.barh(x_data,y_data)
plt.rcParams['font.sans-serif'] = ['SimHei']

plt.title("分类数量统计")
plt.ylabel("类别")
plt.xlabel("数量")
plt.savefig('../data/分类数量统计.jpg')
plt.show()

def main1():
    # 绘制词云图
    stylecloud.gen_stylecloud(text=','.join(y_data1), max_words=100,
                              collocations=False,
                              font_path='simhei.ttf',
                              icon_name='fas fa-circle',
                              size=500,
                              # palette='matplotlib.Inferno_9',
                              output_name='../data/聚类1-云图.png')
    Image(filename='../data/聚类1-云图.png')

def main2():
    # 绘制词云图
    stylecloud.gen_stylecloud(text=','.join(y_data2), max_words=100,
                              collocations=False,
                              font_path='simhei.ttf',
                              icon_name='fas fa-archway',
                              size=500,
                              # palette='matplotlib.Inferno_9',
                              output_name='../data/聚类2-云图.png')
    Image(filename='../data//聚类2-云图.png')


def main3():
    # 绘制词云图
    stylecloud.gen_stylecloud(text=','.join(y_data3), max_words=100,
                              collocations=False,
                              font_path='simhei.ttf',
                              icon_name='fas fa-bell',
                              size=500,
                              # palette='matplotlib.Inferno_9',
                              output_name='../data/聚类3-云图.png')
    Image(filename='../data/聚类3-云图.png')


if __name__ == '__main__':
    main1()
    main2()
    main3()

