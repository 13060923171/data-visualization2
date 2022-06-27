import pandas as pd
from tqdm import tqdm
import numpy as np
import nltk
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
df = pd.read_csv('./output/sum_comment.csv')

list_dz = []
for j,k in zip(df['点赞数'],df['转发数']):
    number = int(j) + int(k)
    list_dz.append(number)

df['权重系数'] = list_dz

def cxfp(x):
    if int(x) < 500:
        return x
    elif 500 <= int(x) <= 1000:
        return int(500)
    elif 1000 <= int(x) <= 2500:
        return int(750)
    elif 2500 <= int(x) <= 5000:
        return int(1000)
    else:
        return int(1500)


df['权重系数'] = df['权重系数'].apply(cxfp)

list_new_comment = []
for j,k in tqdm(zip(df['comment'],df['权重系数'])):
    if 'nan' not in str(j):
        if int(k) >= 2:
            j = str(j + " ") * int(k)
            list_new_comment.append(j)
        else:
            list_new_comment.append(j)

f = open('./output/C-class-fenci.txt', 'w', encoding='utf-8')
for line in tqdm(list_new_comment):
    tokens = nltk.word_tokenize(line)
    # 计算关键词
    all_words = tokens
    c = Counter()
    for x in all_words:
        if len(x) > 1 and x != '\r\n' and x != '\n':
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