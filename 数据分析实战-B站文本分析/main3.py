import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']


df = pd.read_excel('bilibili主评.xlsx').loc[:,['用户等级']]
level = df.value_counts()
#构造data_pair
x_data = ['level5','level6','level4','level3','level2','level0']
y_data = [int(j) for j in level.values]


plt.figure(figsize=(12, 9))  # 调节图形大小
labels = x_data  # 定义标签
sizes = y_data  # 每块值
explode = (0, 0, 0, 0, 0, 0)  # 将某一块分割出来，值越大分割出的间隙越大
colors = ['Cyan','CadetBlue','SteelBlue','DeepSkyBlue','MediumSlateBlue','Navy']
patches, text1, text2 = plt.pie(sizes,
                                explode=explode,
                                labels=labels,
                                colors=colors,
                                labeldistance=1.1,  # 图例距圆心半径倍距离
                                autopct='%3.1f%%',  # 数值保留固定小数位
                                shadow=False,  # 无阴影设置
                                startangle=90,  # 逆时针起始角度设置
                                pctdistance=0.6)  # 数值距圆心半径倍数距离
# patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部文本
# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')
plt.legend()
plt.title('评论用户等级占比图')
plt.savefig('评论用户等级.jpg')
plt.show()