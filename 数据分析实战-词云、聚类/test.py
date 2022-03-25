import pandas as pd
import stylecloud
from IPython.display import Image
import jieba
import jieba.analyse
import re
import time
from collections import Counter
# coding=utf-8
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

df = pd.read_excel('荣耀笔记本MagicBook X 14 2021 14英寸全面屏轻薄笔记本电脑 （i3 8GB 256GB多屏协同）冰河银数据.xlsx')
df['评论内容'] = df['评论内容'].astype(str)

# 定义分词函数
def get_cut_words(content_series):
    # 读入停用词表
    stop_words = []

    with open("stopwords_cn.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())
    list_word = []
    # 分词
    word_num = jieba.lcut(content_series.str.cat(sep='。'), cut_all=False)

    # 条件筛选
    word_num_selected = [i for i in word_num if i not in stop_words and len(i) >= 2]
    return word_num_selected



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

def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True


df['评论内容'] = df['评论内容'].apply(yasuo)
df['评论内容'] = df['评论内容'].dropna(how='any')

# 绘制词云图
text1 = get_cut_words(content_series=df['评论内容'])
stylecloud.gen_stylecloud(text=','.join(text1), max_words=100,
                          collocations=False,
                          font_path='simhei.ttf',
                          icon_name='fas fa-heart',
                          size=500,
                          #palette='matplotlib.Inferno_9',
                          output_name='荣耀热词-云图.png')
Image(filename='荣耀热词-云图.png')


def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True


cut_words = ""
all_words = ""
f = open('荣耀-fenci.txt', 'w', encoding='utf-8')
jieba.analyse.set_stop_words('stopwords_cn.txt')
for line in df['评论内容']:
    line = line.strip('\n')
    # 停用词过滤
    line = re.sub('[0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", line)
    seg_list = jieba.cut(line, cut_all=False)
    cut_words = (" ".join(seg_list))

    # 计算关键词
    all_words = cut_words.split()
    c = Counter()
    for x in all_words:
        if len(x) > 1 and x != '\r\n':
            if is_all_chinese(x) == True:
                c[x] += 1
    # Top50
    output = ""
    # print('\n词频统计结果：')
    for (k, v) in c.most_common():
        # print("%s:%d"%(k,v))
        output += k + " "

    f.write(output + "\n")
else:
    f.close()


# 文档预料 空格连接
corpus = []

# 读取预料 一行预料为一个文档
for line in open('荣耀-fenci.txt', 'r',encoding='utf-8').readlines():
    corpus.append(line.strip())
# 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = CountVectorizer()

# 该类会统计每个词语的tf-idf权值
transformer = TfidfTransformer()

# 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
# 获取词袋模型中的所有词语
word = vectorizer.get_feature_names()

# 将tf-idf矩阵抽取出来 元素w[i][j]表示j词在i类文本中的tf-idf权重
weight = tfidf.toarray()

# 打印特征向量文本内容
print('Features length: ' + str(len(word)))




print('Start Kmeans:')


clf = KMeans(n_clusters=2)
print(clf)
pre = clf.fit_predict(weight)
print(pre)
#
# 中心点
print(clf.cluster_centers_)
print(clf.inertia_)

pca = PCA(n_components=2)  # 输出两维
newData = pca.fit_transform(weight)  # 载入N维
print(newData)

x = [n[0] for n in newData]
y = [n[1] for n in newData]
plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(20,9),dpi = 300)
plt.scatter(x, y, c=pre, s=100)
# plt.legend()
plt.title("荣耀-词性聚类图")
plt.savefig('荣耀-词性聚类图.jpg')
plt.show()
