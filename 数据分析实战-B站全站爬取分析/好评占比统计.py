import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np


def sum_data(name1):
    df = pd.read_csv('./newdata/{}'.format(name1))
    emotion = list(df['情感分值'])
    return emotion

def main():
    sum_emotion = []
    files = os.listdir(r'newdata/')
    for f in files:
        emotion1 = sum_data(f)
        sum_emotion.append(emotion1)

    return sum_emotion


sum_emotion1 = main()
counts = {}
sum_shuzhi = []
for s in sum_emotion1:
    for word in s:
        sum_shuzhi.append(word)
df1 = pd.DataFrame()
df1['data'] = sum_shuzhi

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(12,6))
plt.hist(df1['data'], bins=np.arange(0, 1, 0.01), facecolor='#E74C3C')
plt.xlabel('情感数值')
plt.ylabel('数量')
plt.title('情感分析')
plt.savefig('./HTML文件储存/Analysis of Sentiments.jpg')
plt.show()