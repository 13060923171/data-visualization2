from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import itertools
import pandas as pd
corpus = []
# 读取预料 一行预料为一个文档
for line in open('./output/C-class-fenci.txt', 'r', encoding='utf-8').readlines():
    corpus.append(line.strip())

stop_words = []
with open('常用英文停用词(NLP处理英文必备)stopwords.txt','r',encoding='utf-8')as f:
    lines = f.readlines()
    for line in lines:
        stop_words.append(line.strip().replace("'",""))

# 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = TfidfVectorizer()

# 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
tfidf = vectorizer.fit_transform(corpus)
# 获取词袋模型中的所有词语
word = vectorizer.get_feature_names()

# 将tf-idf矩阵抽取出来 元素w[i][j]表示j词在i类文本中的tf-idf权重
weight = tfidf.toarray()

data = {'word': word,
        'tfidf': weight.sum(axis=0).tolist()}

df = pd.DataFrame(data)
df.sort_values(by="tfidf" , ascending=False)
df.to_csv('./output/tfidf词权重值.csv',encoding='utf-8-sig',index=None)

df1 = pd.read_csv('./output/tfidf词权重值.csv')

for j,k in zip(df1['word'],df1['tfidf']):
    if float(k) > 100 or float(k) < 0.25:
        with open('新增停用词.txt','a+',encoding='utf-8-sig')as f:
            f.write(j+'\n')