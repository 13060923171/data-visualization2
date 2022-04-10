import pandas as pd
import datetime
import numpy as np
import re
import jieba
import stylecloud
from IPython.display import Image


def content_chuli(x):
    x = str(x)
    x = x.replace('#', '').strip().replace("【", "").replace("】", "")
    if len(x) <=1:
        return np.NaN
    return x


def yasuo(st):
    for i in range(1, int(len(st) / 2) + 1):
        for j in range(len(st)):
            if st[j:j + i] == st[j + i:j + 2 * i]:
                k = j + i
                while st[k:k + i] == st[k + i:k + 2 * i] and k < len(st):
                    k = k + i
                st = st[:j] + st[k:]
    return st


def clear_characters(text):
    return re.sub('\W', '', text)


df = pd.read_csv('微博热门信息.csv')
df = df.dropna(how='any')
df = df.drop_duplicates(keep='first')
df['comment'] = df['comment'].astype(str)
df['comment'] = df['comment'].apply(content_chuli)
df = df.dropna(how='any')
df['comment'] = df['comment'].apply(yasuo)
df['comment'] = df['comment'].apply(clear_characters)
df = df.dropna(how='any')


def get_cut_words(content_series):
    # 读入停用词表
    stop_words = []

    with open("stopwords_cn.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())

    def is_all_chinese(strs):
        for _char in strs:
            if not '\u4e00' <= _char <= '\u9fa5':
                return False
        return True

    # 分词
    word_num = jieba.lcut(content_series.str.cat(sep='。'), cut_all=False)

    # 条件筛选
    word_num_selected = [i for i in word_num if i not in stop_words and len(i) >= 2 and is_all_chinese(i) == True]
    return word_num_selected


text1 = get_cut_words(content_series=df['comment'])
stylecloud.gen_stylecloud(text=','.join(text1), max_words=100,
                          collocations=False,
                          font_path='simhei.ttf',
                          icon_name='fas fa-circle',
                          size=500,
                          output_name='热词-云图.png')
Image(filename='热词-云图.png')

counts = {}
for t in text1:
    counts[t] = counts.get(t,0)+1

ls = list(counts.items())
ls.sort(key=lambda x:x[1],reverse=True)
x_data = []
y_data = []

for key,values in ls[:200]:
    x_data.append(key)
    y_data.append(values)

df1 = pd.DataFrame()
df1['word'] = x_data
df1['counts'] = y_data
df1.to_csv('高频词.csv',encoding="utf-8-sig")
df.to_csv('new-微博热门信息.csv',encoding="utf-8-sig",index=None)