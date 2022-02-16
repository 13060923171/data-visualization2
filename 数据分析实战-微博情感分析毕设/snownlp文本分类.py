from snownlp import SnowNLP
from snownlp import sentiment
from snownlp.sentiment import Sentiment
from snownlp import sentiment
from tqdm import tqdm
import re
import pandas as pd
import numpy as np
# 按文章的说法，初步筛选语料，大于0.8的归入积极，小于0.3的归入消极。
def train_model(texts):
    for comm in tqdm(texts):
        if comm != "":
            text = re.sub(r'(?:回复)?(?://)?@[\w\u2E80-\u9FFF]+:?|\[\w+\]', ',',comm)
            score = SnowNLP(text)
            if score.sentiments > 0.8:
                with open('train_pos.txt', mode='a', encoding='utf-8') as g:
                    g.writelines(comm +"\n")
            elif score.sentiments < 0.3:
                with open('train_neg.txt', mode='a', encoding='utf-8') as f:
                    f.writelines(comm + "\n")
            else:
                pass


def test_model(texts):
    for comm in tqdm(texts):
        if comm != "":
            text = re.sub(r'(?:回复)?(?://)?@[\w\u2E80-\u9FFF]+:?|\[\w+\]', ',',comm)
            score = SnowNLP(text)
            if score.sentiments > 0.8:
                with open('test_pos.txt', mode='a', encoding='utf-8') as g:
                    g.writelines(comm +"\n")
            elif score.sentiments < 0.3:
                with open('test_neg.txt', mode='a', encoding='utf-8') as f:
                    f.writelines(comm + "\n")
            else:
                pass

data1 = pd.read_excel('./data/数据(1).xlsx')
data2 = pd.read_excel('./data/数据(2).xlsx')
data3 = pd.read_excel('./data/数据(3).xlsx')
data4 = pd.read_excel('./data/数据(4).xlsx')
data5 = pd.read_excel('./data/数据(5).xlsx')
data6 = pd.read_excel('./data/数据(6).xlsx')
data7 = pd.read_excel('./data/数据(7).xlsx')
data8 = pd.read_excel('./data/数据(8).xlsx')
sum_data = pd.concat([data1,data2,data3,data4,data5,data6,data7,data8])

#删除空值和重复项
comment_text = sum_data['comment_text']
comment_text.dropna(how='any', inplace=True)
comment_text.drop_duplicates(keep='first', inplace=True)


#删除标点符号
def clear_characters(text):
    return re.sub('\W', '', text)


comment_text = comment_text.astype(str)
comment_text = comment_text.apply(clear_characters)


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


comment_text = comment_text.apply(yasuo)

comment_text = comment_text.astype(str)
train_model(comment_text[0:int(len(comment_text)*0.7)])
test_model(comment_text[int(len(comment_text)*0.7):len(comment_text)])