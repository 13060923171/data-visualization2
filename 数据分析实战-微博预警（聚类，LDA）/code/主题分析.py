import pandas as pd
import re
import jieba
import time
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pyLDAvis
import pyLDAvis.sklearn

df = pd.read_csv('../data/疫情-处理好的文本.csv')


def clear_characters(text):
    return re.sub('\W', '', text)
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

content = df['content']
content = content.drop_duplicates(keep='first')
content = content.astype(str)
content = content.apply(clear_characters)
content = content.dropna(how='any')
print(content)

cut_words = ""
all_words = ""
f = open('../data/class-fenci.txt', 'w', encoding='utf-8')
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

stop_words = []

with open("../data/stopwords_cn.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        stop_words.append(line.strip())

corpus = []

# 读取预料 一行预料为一个文档
for line in open('../data/class-fenci.txt', 'r', encoding='utf-8').readlines():
    corpus.append(line.strip())

# 设置特征数
n_features = 2000

tf_vectorizer = TfidfVectorizer(strip_accents='unicode',
                                max_features=n_features,
                                stop_words=stop_words,
                                max_df=0.99,
                                min_df=0.002)  # 去除文档内出现几率过大或过小的词汇

tf = tf_vectorizer.fit_transform(corpus)

# 设置主题数
n_topics = 3

lda = LatentDirichletAllocation(n_components=n_topics,
                                max_iter=100,
                                learning_method='online',
                                learning_offset=50,
                                random_state=0)
lda.fit(tf)

# 显示主题数 model.topic_word_
print(lda.components_)
# 几个主题就是几行 多少个关键词就是几列
print(lda.components_.shape)

# 计算困惑度
print(u'困惑度：')
print(lda.perplexity(tf,sub_sampling = False))



# 主题-关键词分布
def print_top_words(model, tf_feature_names, n_top_words):
    for topic_idx,topic in enumerate(model.components_):  # lda.component相当于model.topic_word_
        print('Topic #%d:' % topic_idx)
        print(' '.join([tf_feature_names[i] for i in topic.argsort()[:-n_top_words-1:-1]]))
        print("")

# 定义好函数之后 暂定每个主题输出前20个关键词
n_top_words = 20
tf_feature_names = tf_vectorizer.get_feature_names()
# 调用函数
print_top_words(lda, tf_feature_names, n_top_words)

data = pyLDAvis.sklearn.prepare(lda,tf,tf_vectorizer)
print(data)


pyLDAvis.save_html(data,'../data/lda-主题模型.html')