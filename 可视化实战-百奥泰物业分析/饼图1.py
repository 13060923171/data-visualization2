import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']

df = pd.read_excel('百奥泰-U.xlsx',sheet_name='百奥泰-U上市前股权结构').loc[:14,['百奥泰-U上市前股权结构','Unnamed: 1']]

x_data = []
y_data = []
for x in df['百奥泰-U上市前股权结构']:
    x_data.append(x)

for y in df['Unnamed: 1']:
    y_data.append(y)

plt.figure(figsize=(16,9)) #调节图形大小

colors = ['mediumspringgreen','mediumaquamarine','aquamarine','turquoise','lightseagreen','mediumturquoise','yellow','r','salmon','tomato','coral','lightsalmon','sandybrown','peru','darkgray'] #每块颜色定义
explode = (0,0,0.02,0,0,0,0,0,0,0,0,0,0,0,0) #将某一块分割出来，值越大分割出的间隙越大
patches,text1,text2 = plt.pie(y_data,
                      explode=explode,
                      labels=x_data,
                      colors=colors,
                      labeldistance = 3,#图例距圆心半径倍距离
                      autopct = '%3.2f%%', #数值保留固定小数位
                      shadow = False, #无阴影设置
                      startangle =90, #逆时针起始角度设置
                      pctdistance = 0.6) #数值距圆心半径倍数距离
#patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部文本
# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')
plt.legend()
plt.title('百奥泰-U上市前股权结构所在百分比图')
plt.savefig('图1.jpg')
plt.show()