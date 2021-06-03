# -*- coding: utf-8 -*-

import pandas as pd
import codecs
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import pyecharts.options as opts
from pyecharts.charts import Scatter
from sklearn.decomposition import PCA
from pyecharts.globals import ThemeType
import matplotlib.pyplot as plt


#读取数据
df = pd.read_excel('宋朝历史人物信息表.xlsx').loc[:,['姓名','籍贯','出生地','官职','入仕方式','社会区分']]
df.dropna(axis=0,how='any',inplace=True)
df.isnull().sum()
df = df.values.tolist()
corpus = [] #文档预料 空格连接
#将表格的数据生成指定的数据格式
for line in df:
    line = ','.join(line)
    corpus.append(line)

#########################################################################
#                           第一步 计算TFIDF


# 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = CountVectorizer()

# 该类会统计每个词语的tf-idf权值
transformer = TfidfTransformer()

# 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

# 获取词袋模型中的所有词语
word = vectorizer.get_feature_names()

# 将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
weight = tfidf.toarray()
#
# 打印特征向量文本内容
print('Features length: ' + str(len(word)))
resName = "BHTfidf_Result.txt"
result = codecs.open(resName, 'w', 'utf-8')
for j in range(len(word)):
    result.write(word[j] + ' ')
result.write('\r\n\r\n')

# 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
for i in range(len(weight)):
    # print u"-------这里输出第", i, u"类文本的词语tf-idf权重------"
    for j in range(len(word)):
        # print weight[i][j],
        result.write(str(weight[i][j]) + ' ')
    result.write('\r\n\r\n')

result.close()

########################################################################
#                               第二步 聚类Kmeans

print('Start Kmeans:')
clf = KMeans(n_clusters=6)  # 姓名，籍贯，出生地，官职，入仕方式，社会区分
s = clf.fit(weight)
print(s)

# 中心点
print(clf.cluster_centers_)
# 每个样本所属的簇
label = []
print(clf.labels_)
i = 1
while i <= len(clf.labels_):
    print(clf.labels_[i - 1])
    label.append(clf.labels_[i - 1])
    i = i + 1

# 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
print(clf.inertia_)
y_pred = clf.labels_

#######################################################################
# 第三步 图形输出 降维

pca = PCA(n_components=6)  # 输出六维
newData = pca.fit_transform(weight)  # 载入N维
y_pred1 = clf.fit_predict(newData)

x = [n[0] for n in newData]
y1 = [n[1] for n in newData]
y2 = [n[2] for n in newData]
y3 = [n[3] for n in newData]
y4 = [n[4] for n in newData]
y5 = [n[5] for n in newData]


#生成散点图
def main_scatter():
    (
        Scatter(init_opts=opts.InitOpts(width="1600px", height="1000px",theme=ThemeType.INFOGRAPHIC))
        .add_xaxis(xaxis_data=x)
        .add_yaxis(
            series_name="籍贯",
            y_axis=y1,
            symbol_size=20,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="出生地",
            y_axis=y2,
            symbol_size=20,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="官职",
            y_axis=y3,
            symbol_size=20,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="入仕方式",
            y_axis=y4,
            symbol_size=20,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="社会区分",
            y_axis=y5,
            symbol_size=20,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_series_opts()
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        .render("basic_scatter_chart.html")
    )





main_scatter()