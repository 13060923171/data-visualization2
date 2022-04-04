from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.feature_extraction import DictVectorizer
import matplotlib.pyplot as plt
import matplotlib
import jieba
import pandas as pd
from collections import Counter
import jieba.analyse
import re
import string
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
df = pd.read_excel('豆瓣书籍(1).xls')
plt.style.use('ggplot')
matplotlib.rcParams['axes.unicode_minus']=False

def cbs():
    train_features = df['出版社']
    train_features = train_features.fillna(method='ffill')

    def is_all_chinese(strs):
        for _char in strs:
            if not '\u4e00' <= _char <= '\u9fa5':
                return False
        return True

    f = open('fenci.txt', 'w', encoding='utf-8')
    jieba.analyse.set_stop_words('stopwords_cn.txt')
    for line in train_features:
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
    for line in open('fenci.txt', 'r', encoding='utf-8').readlines():
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

    data = {'word': word,
            'tfidf': weight.sum(axis=0).tolist()}
    tf_df = pd.DataFrame(data)

    def str_count(str):
        count_en = count_dg = count_sp = count_zh = count_pu = 0
        for s in str:
            if s in string.ascii_letters:
                count_en += 1
            elif s.isdigit():
                count_dg += 1
            elif s.isspace():
                count_sp += 1
            elif s.isalpha():
                count_zh += 1
            else:
                count_pu += 1
        return count_zh

    tf_df['zh'] = tf_df['word'].apply(str_count)
    word1 = []
    tfidf1 = []

    for w, t, z in zip(tf_df['word'], tf_df['tfidf'], tf_df['zh']):
        if z >= 1:
            word1.append(w)
            tfidf1.append(t)
        else:
            pass
    tf_df1 = pd.DataFrame()
    tf_df1['word'] = word1
    tf_df1['tfidf'] = tfidf1
    tf_df1.sort_values(by="tfidf", ascending=False, inplace=True)
    tf_df1.to_excel('出版社-tf-idf.xlsx')
    # dvec = DictVectorizer(sparse=False)
    # train_features=dvec.fit_transform(train_features.to_dict(orient='record'))
    kmeans = KMeans(n_clusters=3, init='k-means++', n_init=10, max_iter=300, tol=0.0001, algorithm='auto')
    # min_max_scaler = preprocessing.MinMaxScaler()
    # train_x = min_max_scaler.fit_transform(train_features)
    # kmeans.fit(train_x)
    predict_y = kmeans.fit_predict(weight)
    # 中心点
    print('出版社质心:',kmeans.inertia_)
    counts = {}
    for p in predict_y:
        counts[p] = counts.get(p,0)+1
    ls = list(counts.items())
    ls.sort(key=lambda x:x[0],reverse=False)
    x_data = []
    y_data = []
    for key,values in ls:
        x_data.append(key)
        y_data.append(values)

    plt.figure(figsize=(9, 6))
    plt.bar(x_data, y_data)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("评分与出版社分类状况")
    plt.xlabel("类别")
    plt.ylabel("数量")
    plt.savefig('评分与出版社分类状况.jpg')
    plt.show()
    return predict_y,ls


def author():
    train_features = df['作者']
    train_features = train_features.fillna(method='ffill')

    def is_all_chinese(strs):
        for _char in strs:
            if not '\u4e00' <= _char <= '\u9fa5':
                return False
        return True

    f = open('fenci1.txt', 'w', encoding='utf-8')
    jieba.analyse.set_stop_words('stopwords_cn.txt')
    for line in train_features:
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
    for line in open('fenci1.txt', 'r', encoding='utf-8').readlines():
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

    data = {'word': word,
            'tfidf': weight.sum(axis=0).tolist()}
    tf_df = pd.DataFrame(data)

    def str_count(str):
        count_en = count_dg = count_sp = count_zh = count_pu = 0
        for s in str:
            if s in string.ascii_letters:
                count_en += 1
            elif s.isdigit():
                count_dg += 1
            elif s.isspace():
                count_sp += 1
            elif s.isalpha():
                count_zh += 1
            else:
                count_pu += 1
        return count_zh

    tf_df['zh'] = tf_df['word'].apply(str_count)
    word1 = []
    tfidf1 = []

    for w, t, z in zip(tf_df['word'], tf_df['tfidf'], tf_df['zh']):
        if z >= 1:
            word1.append(w)
            tfidf1.append(t)
        else:
            pass
    tf_df1 = pd.DataFrame()
    tf_df1['word'] = word1
    tf_df1['tfidf'] = tfidf1
    tf_df1.sort_values(by="tfidf", ascending=False, inplace=True)
    tf_df1.to_excel('作者-tf-idf.xlsx')

    # dvec = DictVectorizer(sparse=False)
    # train_features=dvec.fit_transform(train_features.to_dict(orient='record'))
    # n_clusters既K值，一般需要多试一些K值来保证更好的聚类结果，你可以随机设置一些K值，然后选择聚类效果最好的作为最终的K值
    # max_iter最大迭代次数，如果聚类很难收敛的话，设置最大迭代次数可以让我们及时得到反馈结果，否则程序运行时间会非常长
    # n_init初始化中心点的运算次数，默认是0，程序是否能快速收敛和中心点的选择关系非常大，所以在中心点选择上多花一些时间，来争取整体时间
    # 上的快速收敛还是非常值得的。由于每一次中心点都是随机生成的，这样得到的结果就有好有坏，非常不确定，所以要运行n_init次，取其中最好的作为初始的中心点
    # 如果K值比较大的时候，你可以适当增大n_init这个值
    # init既初始值选择的方式，默认是采用优化过的K-means++　方式，你也可以自己指定中心点，或者采用ｒａｎｄｏｍ完全随机的方式。自己设置中心点一般是
    # 对于个性化的数据进行设置，很少采用random的方式则是完全随机的方式，一般推荐采用优化过的K-means ++ 方式
    # algorithm：k-means的实现算法，有“auto”“full”“elkan”三种，一般来说建议直接用默认的“auto”。简单说下这三种取值的区别，如果你选择“full”
    # 采用的是传统的K-means算法，“auto’会根据数据的特点自动选择是”full“还是”elkan“
    kmeans = KMeans(n_clusters=3, init='k-means++', n_init=10, max_iter=300, tol=0.0001, algorithm='auto')
    # min_max_scaler = preprocessing.MinMaxScaler()
    # train_x = min_max_scaler.fit_transform(train_features)
    # kmeans.fit(train_x)

    predict_y = kmeans.fit_predict(weight)
    print('作者质心:', kmeans.inertia_)
    counts = {}
    for p in predict_y:
        counts[p] = counts.get(p, 0) + 1
    ls = list(counts.items())
    ls.sort(key=lambda x: x[0], reverse=False)
    x_data = []
    y_data = []
    for key, values in ls:
        x_data.append(key)
        y_data.append(values)

    plt.figure(figsize=(9, 6))
    plt.bar(x_data, y_data)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("评分与作者分类状况")
    plt.xlabel("类别")
    plt.ylabel("数量")
    plt.savefig('评分与作者分类状况.jpg')
    plt.show()
    return predict_y, ls


def pf():
    pf_count = df['评分']
    counts = {}
    for p in pf_count:
        counts[p] = counts.get(p,0)+1
    ls = list(counts.items())
    ls.sort(key=lambda x:x[0],reverse=False)
    x_data = []
    y_data = []
    for key,values in ls:
        x_data.append(key)
        y_data.append(values)

    plt.figure(figsize=(9, 6))
    plt.bar(x_data,y_data)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("评分分部情况")
    plt.xlabel("评分")
    plt.ylabel("数量")
    plt.savefig('评分分部情况.jpg')
    plt.show()


if __name__ == '__main__':
    results1 = cbs()
    results2 = author()
    pf()
    result3 = pd.concat((df, pd.DataFrame(results1[0])), axis=1)
    result3.rename({0: '出版社聚类结果'}, axis=1, inplace=True)
    result4 = pd.concat((result3, pd.DataFrame(results2[0])), axis=1)
    result4.rename({0: '作者聚类结果'}, axis=1, inplace=True)
    result4.to_excel('新-豆瓣书籍.xlsx')