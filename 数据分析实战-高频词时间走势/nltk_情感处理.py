import pandas as pd
import nltk
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer

df = pd.read_csv('./output/聚类结果.csv',encoding="utf-8-sig")
df = df.dropna(subset=['comment'])
sid = SentimentIntensityAnalyzer()


def emotional_judgment(x):
    neg = x['neg']
    neu = x['neu']
    pos = x['pos']
    compound = x['compound']
    if compound == 0 and neg == 0 and pos == 0 and neu == 1:
        return 'neu'
    elif compound == 0 and neg < neu and pos < neu:
        return 'neu'
    if compound > 0:
        if pos > neg:
            return 'pos'
        else:
            return 'neg'
    elif compound < 0:
        if pos < neg:
            return 'neg'
        else:
            return 'pos'


df['scores'] = df['comment'].apply(lambda commentText: sid.polarity_scores(commentText))
df['compound'] = df['scores'].apply(lambda score_dict: score_dict['compound'])
df['Negtive'] = df['scores'].apply(lambda score_dict: score_dict['neg'])
df['Postive'] = df['scores'].apply(lambda score_dict: score_dict['pos'])
df['Neutral'] = df['scores'].apply(lambda score_dict: score_dict['neu'])
df['comp_score'] = df['scores'].apply(emotional_judgment)
df = df.drop(['Unnamed: 0','Unnamed: 0.1','Unnamed: 0.1.1'],axis=1)
df.to_csv('./output/情感分布计算.csv',encoding="utf-8-sig",index=None)



