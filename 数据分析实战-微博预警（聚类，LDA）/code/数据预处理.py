import pandas as pd
import datetime
import numpy as np
import paddlehub as hub
df = pd.read_csv('../data/疫情关键词实时舆论.csv')
df = df.drop(['f','spiderTime'],axis=1)

def time_chuli(x):
    x = str(x)
    if '今天' in x or '前' in x:
        return datetime.datetime.now().strftime('%m-%d')
    elif '月' in x:
        x = x.split('日')
        x = x[0]
        x = x.replace('月','-')
        return x
    else:
        return x


def content_chuli(x):
    x = str(x)
    x = x.replace('#', '').strip().replace("【", "").replace("】", "")
    if len(x) <=1:
        return np.NaN
    return x


def comment_chuli(x):
    x = str(x)
    if '评论' in x:
        x = x.replace('评论','0')
        return x
    else:
        return x


def praise_chuli(x):
    x = str(x)
    if '赞' in x:
        x = x.replace('赞','0')
        return x
    else:
        return x


def transmit_chuli(x):
    x = str(x)
    if '转发' in x:
        x = x.replace('转发','0')
        return x
    else:
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

df = df.dropna(how='any')
df['time'] = df['time'].apply(time_chuli)
df['content'] = df['content'].apply(content_chuli)
df['comment'] = df['comment'].apply(comment_chuli)
df['transmit'] = df['transmit'].apply(transmit_chuli)
df['praise'] = df['praise'].apply(praise_chuli)
df['comment'] = df['comment'].astype(int)
df['transmit'] = df['transmit'].astype(int)
df['praise'] = df['praise'].astype(int)
df = df.dropna(how='any')
df['content'] = df['content'].apply(yasuo)


#这里使用了百度开源的成熟NLP模型来预测情感倾向
senta = hub.Module(name="senta_bilstm")
texts = df['content'].tolist()
input_data = {'text':texts}
res = senta.sentiment_classify(data=input_data)
df['emotion_score'] = [x['positive_probs'] for x in res]
df = df.drop_duplicates(subset=None, keep='first')
df.to_csv('../data/疫情-处理好的文本.csv',encoding="utf-8-sig")