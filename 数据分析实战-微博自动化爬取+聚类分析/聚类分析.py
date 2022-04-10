import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import jieba
import jieba.analyse
import re
import time
from collections import Counter

def fenci():
    df = pd.read_csv('new-微博热门信息.csv')
    content = df['comment']
    content = content.astype(str)
    f = open('fenci.txt', 'w', encoding='utf-8')
    jieba.analyse.set_stop_words('stopwords_cn.txt')
    for line in content:
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

fenci()

#########################################################################
#                           第一步 计算TFIDF

# 文档预料 空格连接
corpus = []

# 读取预料 一行预料为一个文档
for line in open('fenci.txt', 'r',encoding='utf-8').readlines():
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

#
########################################################################
#                               第二步 聚类Kmeans

print('Start Kmeans:')
from sklearn.cluster import KMeans

clf = KMeans(n_clusters=2)
print(clf)
pre = clf.fit_predict(weight)
print(pre)

# 中心点
print(clf.cluster_centers_)
print(clf.inertia_)

########################################################################
#                               第三步 图形输出 降维

from sklearn.decomposition import PCA

pca = PCA(n_components=2)  # 输出两维
newData = pca.fit_transform(weight)  # 载入N维

x = [n[0] for n in newData]
y = [n[1] for n in newData]
plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
plt.rcParams['axes.unicode_minus'] = False
plt.scatter(x, y, c=pre, s=100)
# plt.legend()
plt.title("词性聚类图")
plt.savefig('词性聚类图.jpg')
plt.show()