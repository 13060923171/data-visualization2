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
from pyecharts.charts import Map,Timeline


#读取数据
def getting_data():
    name = ['陈桥兵变', '雍熙北伐', '庆历新政', '王安石变法', '靖康之变', '建炎南渡', '绍兴和议', '隆兴北伐', '襄樊之战', '崖山海战']
    sum_corpus = []
    for n in name:
        df = pd.read_excel('./data/宋朝历史人物信息表.xlsx',sheet_name='{}'.format(n)).loc[:,['姓名','籍贯','出生地','官职','入仕方式','社会区分']]
        df.dropna(axis=0,how='any',inplace=True)
        df.isnull().sum()
        df = df.values.tolist()
        corpus = [] #文档预料 空格连接
        #将表格的数据生成指定的数据格式
        for line in df:
            line = ','.join(line)
            corpus.append(line)
        sum_corpus.append(corpus)
    return sum_corpus


#第一步 计算TFIDF
def calculate_tfidf():
    sum_corpus = getting_data()
    sum_weight = []
    for c in range(len(sum_corpus)):
        corpus = sum_corpus[c]
        # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
        countvectorizer = CountVectorizer()

        # 该类会统计每个词语的tf-idf权值
        tfidftransformer = TfidfTransformer()

        # 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
        tfidf = tfidftransformer.fit_transform(countvectorizer.fit_transform(corpus))

        # 获取词袋模型中的所有词语
        words = countvectorizer.get_feature_names()

        # 将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
        weight = tfidf.toarray()
        sum_weight.append(weight)
        #
        # 打印特征向量文本内容
        # print('Features length: ' + str(len(word)))
        resName = "./data/BHTfidf_Result_{}.txt".format(c+1)
        result = codecs.open(resName, 'w', 'utf-8')
        for j in range(len(words)):
            result.write(words[j] + ' ')
        result.write('\r\n\r\n')

        # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
        for i in range(len(weight)):
            # print u"-------这里输出第", i, u"类文本的词语tf-idf权重------"
            for j in range(len(words)):
                # print weight[i][j],
                result.write(str(weight[i][j]) + ' ')
            result.write('\r\n\r\n')

        result.close()

    return sum_weight


# 第二步 聚类Kmeans
# 第三步 图形输出 降维
def k_means():
    sum_weight = calculate_tfidf()
    sum_newData = []
    for weight in sum_weight:
        # print('Start Kmeans:')
        clf = KMeans(n_clusters=6)  # 姓名，籍贯，出生地，官职，入仕方式，社会区分
        s = clf.fit(weight)
        # print(s)

        # 中心点
        # print(clf.cluster_centers_)
        # 每个样本所属的簇
        label = []
        # print(clf.labels_)
        i = 1
        while i <= len(clf.labels_):
            # print(clf.labels_[i - 1])
            label.append(clf.labels_[i - 1])
            i = i + 1

        # 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
        # print(clf.inertia_)
        # y_pred = clf.labels_

        pca = PCA(n_components=6)  # 输出六维
        newData = pca.fit_transform(weight)  # 载入N维
        # y_pred1 = clf.fit_predict(newData)
        sum_newData.append(newData)

    return sum_newData


#生成散点图
def main_scatter():
    sum_newData =  k_means()
    name = ['陈桥兵变', '雍熙北伐', '庆历新政', '王安石变法', '靖康之变', '建炎南渡', '绍兴和议', '隆兴北伐', '襄樊之战', '崖山海战']
    tl = Timeline()
    for n in range(len(sum_newData)):
        newData = sum_newData[n]
        x = [n[0] for n in newData]  # 姓名
        y1 = [n[1] for n in newData]  # 籍贯
        y2 = [n[2] for n in newData]  # 出生地
        y3 = [n[3] for n in newData]  # 官职
        y4 = [n[4] for n in newData]  # 入仕方式
        y5 = [n[5] for n in newData]  # 社会区分
        c = (
            Scatter(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
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
        )
        tl.add(c, "{}".format(name[int(n)]))
        tl.add_schema(
            orient="vertical",
            is_auto_play=True,
            is_inverse=True,
            play_interval=3000,
            pos_left="3",
            pos_right="null",
            pos_top="20",
            pos_bottom="20",
            width="50",
            label_opts=opts.LabelOpts(is_show=True, color="#fff"),
        )
    return tl





