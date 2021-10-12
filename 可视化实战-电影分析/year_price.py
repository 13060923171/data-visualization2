import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('电影数据.csv',encoding='gbk').loc[:,['年份','票价']]
year = df['年份']
price = df['票价']

list_year = []
list_price = []
for j in range(len(year)):
    t = year[j]
    t = str(t)
    t = t.replace('[','').replace(']','').replace("'","").replace(' ','')
    t = t.split(',')
    for i in t:
        if '-' in i:
            list_year.append(i[0:4])
            list_price.append(price[j])

list1 = list(set(list_year))
list1.sort(key=lambda x:x,reverse=False)

sum_2011 = []
sum_2012 = []
sum_2013 = []
sum_2014 = []
sum_2015 = []
sum_2016 = []
sum_2017 = []
sum_2018 = []
sum_2019 = []

for k in range(len(list_year)):
    if list_year[k] == '2011':
        sum_2011.append(float(list_price[k]))
    if list_year[k] == '2012':
        sum_2012.append(float(list_price[k]))
    if list_year[k] == '2013':
        sum_2013.append(float(list_price[k]))
    if list_year[k] == '2014':
        sum_2014.append(float(list_price[k]))
    if list_year[k] == '2015':
        sum_2015.append(float(list_price[k]))
    if list_year[k] == '2016':
        sum_2016.append(float(list_price[k]))
    if list_year[k] == '2017':
        sum_2017.append(float(list_price[k]))
    if list_year[k] == '2018':
        sum_2018.append(float(list_price[k]))
    if list_year[k] == '2019':
        sum_2019.append(float(list_price[k]))

sum_2012.remove(40150.5)
avg_2011 = sum(sum_2011) / len(sum_2011)
avg_2012 = sum(sum_2012) / len(sum_2012)
avg_2013 = sum(sum_2013) / len(sum_2013)
avg_2014 = sum(sum_2014) / len(sum_2014)
avg_2015 = sum(sum_2015) / len(sum_2015)
avg_2016 = sum(sum_2016) / len(sum_2016)
avg_2017 = sum(sum_2017) / len(sum_2017)
avg_2018 = sum(sum_2018) / len(sum_2018)
avg_2019 = sum(sum_2019) / len(sum_2019)


sum_avg = [avg_2011,avg_2012,avg_2013,avg_2014,avg_2015,avg_2016,avg_2017,avg_2018,avg_2019]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 使用两次 bar 函数画出两组条形图
plt.bar(list1, height=sum_avg, color='darkcyan')
# 坐标轴上移
ax = plt.subplot(111)
ax.spines['right'].set_color('none')     # 去掉右边的边框线
ax.spines['top'].set_color('none')

plt.ylabel('Price')  # 纵坐标轴标题
plt.title('年份与平均票价关系图')  # 图形标题
plt.savefig('year_price.jpg')
plt.show()