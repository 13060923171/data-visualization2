import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel('bilibili主评.xlsx')
data = list(df.columns[0:10])
df1 = df[data]
df1 = df1.drop_duplicates(keep='first')
name = df1['视频标题']
print(name)
x_data = df1['发布时间'][:-1].values
y_data = df1['播放量'][:-1].values
x_data1 = []
for x in x_data:
    x = str(x)
    x = x.split(" ")
    x = x[0]
    x_data1.append(x)
y_data1 = []
for y in y_data:
    y = int(y)
    y_data1.append(y)

plt.figure(figsize=(12, 9),dpi=300)
font1 = {
        'style': 'normal',
        'size': 15,
    }
plt.plot(x_data1,y_data1,'o--',color='#b82410')
plt.tick_params(labelsize=15)
plt.title('Release time and number of views')
plt.xlabel('release time',font1)
plt.ylabel('amount of play',font1)
plt.grid()
plt.savefig('发布时间与播放量.jpg')
plt.show()