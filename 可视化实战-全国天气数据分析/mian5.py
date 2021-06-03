import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
from pylab import *
df = pd.read_csv('./csv_file/全国空气质量指数排行榜.csv',encoding='gbk').loc[:,['城市','AQI']]
df.dropna(axis=0,how='any',inplace=True)
df[df.isnull().T.any()]

list_city = []
for i in df['城市']:
    list_city.append(i)

list_aqi = []
for j in df['AQI']:
    list_aqi.append(j)

d = {}
for i in range(len((list_city))):
    d[list_city[i]] = list_aqi[i]

ls = list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)
top_10 = ls[0:10]
finally_10 = ls[-10:]

x_data = []
y_data = []

for f in finally_10:
    x = f[0]
    x_data.append(x)
    y = f[1]
    y_data.append(y)

x_data1 = []
y_data1 = []

for f in top_10:
    x = f[0]
    x_data1.append(x)
    y = f[1]
    y_data1.append(y)

plt.bar(x_data, y_data, facecolor='#9999ff', edgecolor='white',label='空气最好的城市')
plt.bar(x_data1, y_data1, facecolor='#ff9999', edgecolor='white',label='空气最差的城市')
plt.legend()  # 显示图例
plt.xticks(rotation=30)
plt.show()