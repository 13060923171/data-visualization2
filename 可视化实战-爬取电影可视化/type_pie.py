import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('电影数据.csv',encoding='gbk')
type = df['类型']

sum_type = []
for t in type:
    t = str(t)
    t = t.replace('[','').replace(']','').replace("'","").replace(' ','')
    t = t.split(',')
    for i in t:
        sum_type.append(i)

d = {}
for s in sum_type:
    d[s] = d.get(s,0)+1
list1 = list(d.items())
list1.sort(key= lambda x:x[1],reverse=True)
list1.remove(list1[4])

labels = []
sizes = []
for data in list1:
    labels.append(data[0])
    sizes.append(data[1])

plt.rcParams['font.sans-serif']=['SimHei']
#获取电影类型前10的类型
plt.figure(figsize=(12,9)) #调节图形大小
labels = labels[:10] #定义标签
sizes = sizes[:10] #每块值
colors = ['midnightblue','steelblue','palegreen','c','lightyellow','lightgreen','CadetBlue','LightBlue','MediumSlateBlue','Goldenrod'] #每块颜色定义
explode = (0,0,0.02,0,0,0,0,0,0,0) #将某一块分割出来，值越大分割出的间隙越大
patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      labeldistance = 0.8,#图例距圆心半径倍距离
                      autopct = '%3.2f%%', #数值保留固定小数位
                      shadow = False, #无阴影设置
                      startangle =90, #逆时针起始角度设置
                      pctdistance = 0.6) #数值距圆心半径倍数距离
#patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部文本
# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')
plt.legend()
plt.title('电影类型前10的类型')
plt.savefig('type_pie.jpg')
plt.show()


