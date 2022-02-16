import pandas as pd
import re
import jieba
#可视化库
import stylecloud
from IPython.display import Image
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType

import time
from collections import Counter

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


def get_cut_words(content_series):
    # 读入停用词表
    stop_words = []

    with open("stopwords_cn.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())

            # 分词
    word_num = jieba.lcut(content_series.str.cat(sep='。'), cut_all=False)

    # 条件筛选
    word_num_selected = [i for i in word_num if i not in stop_words and len(i) >= 2]
    return word_num_selected

text1 = get_cut_words(content_series=comment_text)

#分词，寻找高频词
ditc = {}
list_word = []
list_count = []
for t in text1:
    ditc[t] = ditc.get(t, 0) + 1
ls = list(ditc.items())
ls.sort(key=lambda x: x[1], reverse=True)
for i in range(len(ls)):
    word, count = ls[i]
    list_word.append(word)
    list_count.append(count)

df1 = pd.DataFrame()

df1['word'] = list_word
df1['count'] = list_count
df1.to_csv('高频词.csv',encoding='gbk')


x_data = list_word[0:100]
y_data = list_count[0:100]

data_pair = [(x,int(y)) for x,y in zip(x_data,y_data)]

def get_word():
    #词云图
    c = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
        .add("", data_pair, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
        .set_global_opts(title_opts=opts.TitleOpts(title="高频词-词云图"))

    )
    return c



# ------------------------------------中文分词------------------------------------
cut_words = ""
all_words = ""
f = open('fenci.txt', 'w', encoding='utf-8')

for line in comment_text:
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
    output = ""
    for (k, v) in c.most_common():
        # print("%s:%d"%(k,v))
        output += k + " "

    f.write(output + "\n")
else:
    f.close()