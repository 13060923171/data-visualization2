from snownlp import SnowNLP
import pandas as pd
import codecs
import os
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_excel('豆瓣电影评分.xlsx')
sentimentslist = []
texts = df['内容'].tolist()
for i in texts:
    i = i.replace('"}','').replace('"内容":','').replace('"','').replace('... ','').strip('\n')
    s = SnowNLP(i)
    print(s.sentiments)
    sentimentslist.append(s.sentiments)

plt.hist(sentimentslist, bins = np.arange(0, 1, 0.01), facecolor = 'g')
plt.xlabel('Sentiments Probability')
plt.ylabel('Quantity')
plt.title('Analysis of Sentiments')
plt.show()

