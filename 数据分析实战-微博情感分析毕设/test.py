import jieba
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import metrics
from sklearn.metrics import accuracy_score
import numpy as np
import warnings
warnings.filterwarnings('ignore')


#读取文件内容
def loadfile(file_dir, label):
    words_list = []
    labels_list = []
    with open(file_dir,'r',encoding='utf-8')as f:
        content = f.readlines()
    for c in content:
        words_list.append(c)
        labels_list.append(label)
    return words_list, labels_list


# 数据预处理
def deal_text(text, stop_path):
    stopwords = set()
    with open(stop_path, 'r', encoding='utf-8') as in_file:
        for line in in_file:
            stopwords.add(line.strip())

    text = re.sub('[!！]+', "!", text)
    text = re.sub('[?？]+', "?", text)
    text = re.sub("[a-zA-Z#$%&\'()*+,-./:;：<=>@，。★、…【】《》“”‘’[\\]^_`{|}~]+", " UNK ", text)
    text = re.sub(r"\d+", ' NUM ', text)
    text = re.sub(r"\s+", " ", text)
    text = " ".join([term for term in jieba.cut(text) if term and not term in stopwords])
    return text


train_words_list1, train_labels1 = loadfile('train_pos.txt', '1')
train_words_list2, train_labels2 = loadfile('train_neg.txt', '0')

train_words_list = train_words_list1 + train_words_list2
train_labels = train_labels1 + train_labels2

test_words_list1, test_labels1 = loadfile('test_pos.txt', '1')
test_words_list2, test_labels2 = loadfile('test_neg.txt', '0')

test_words_list = test_words_list1 + test_words_list2
test_labels = test_labels1 + test_labels2

train_comments_new = [deal_text(comment, "stopwords_cn.txt") for comment in train_words_list]
test_comments_new = [deal_text(comment, "stopwords_cn.txt") for comment in test_words_list]


stop_words = open('stopwords_cn.txt','r',encoding='utf-8').read()
stop_words = stop_words.encode('utf-8').decode('utf-8-sig') #列表头部\ufeff处理
stop_words = stop_words.split('\n') #根据分隔符分隔

#计算单词权重
tf = TfidfVectorizer(stop_words=stop_words,max_df=0.5)

train_features = tf.fit_transform(train_comments_new)
#上面fit过了,这里transform
test_features = tf.transform(test_comments_new)

#多项式贝叶斯分类器
clf = MultinomialNB(alpha=0.001).fit(train_features,train_labels)
predicted_labels = clf.predict(test_features)
#计算准确率
print('准确率：',accuracy_score(test_labels,predicted_labels))

