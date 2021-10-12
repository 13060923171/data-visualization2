import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('电影数据.csv',encoding='gbk').loc[:,['年份','国家']]
year = df['年份']
city = df['国家']

list_year = []
list_city = []
for j in range(len(year)):
    t = year[j]
    t = str(t)
    t = t.replace('[','').replace(']','').replace("'","").replace(' ','')
    t = t.split(',')
    for i in t:
        if '-' in i:
            list_year.append(i[0:4])
            list_city.append(city[j])


list1 = list(set(list_year))
list1.sort(key=lambda x:x,reverse=False)

zg_2011 = []
zg_2012 = []
zg_2013 = []
zg_2014 = []
zg_2015 = []
zg_2016 = []
zg_2017 = []
zg_2018 = []
zg_2019 = []

mg_2011 = []
mg_2012 = []
mg_2013 = []
mg_2014 = []
mg_2015 = []
mg_2016 = []
mg_2017 = []
mg_2018 = []
mg_2019 = []

yg_2011 = []
yg_2012 = []
yg_2013 = []
yg_2014 = []
yg_2015 = []
yg_2016 = []
yg_2017 = []
yg_2018 = []
yg_2019 = []

rb_2011 = []
rb_2012 = []
rb_2013 = []
rb_2014 = []
rb_2015 = []
rb_2016 = []
rb_2017 = []
rb_2018 = []
rb_2019 = []

fg_2011 = []
fg_2012 = []
fg_2013 = []
fg_2014 = []
fg_2015 = []
fg_2016 = []
fg_2017 = []
fg_2018 = []
fg_2019 = []


for k in range(len(list_year)):
    if list_year[k] == '2011':
        if '中国' in list_city[k]:
            zg_2011.append(list_year[k])
        if '美国' in list_city[k]:
            mg_2011.append(list_year[k])
        if '英国' in list_city[k]:
            yg_2011.append(list_year[k])
        if '法国' in list_city[k]:
            fg_2011.append(list_year[k])
        if '日本' in list_city[k]:
            rb_2011.append(list_year[k])
    if list_year[k] == '2012':
        if '中国' in list_city[k]:
            zg_2012.append(list_year[k])
        if '美国' in list_city[k]:
            mg_2012.append(list_year[k])
        if '英国' in list_city[k]:
            yg_2012.append(list_year[k])
        if '法国' in list_city[k]:
            fg_2012.append(list_year[k])
        if '日本' in list_city[k]:
            rb_2012.append(list_year[k])
    if list_year[k] == '2013':
        if '中国' in list_city[k]:
            zg_2013.append(list_year[k])
        if '美国' in list_city[k]:
            mg_2013.append(list_year[k])
        if '英国' in list_city[k]:
            yg_2013.append(list_year[k])
        if '法国' in list_city[k]:
            fg_2013.append(list_year[k])
        if '日本' in list_city[k]:
            rb_2013.append(list_year[k])
    if list_year[k] == '2014':
        if '中国' in list_city[k]:
            zg_2014.append(list_year[k])
        if '美国' in list_city[k]:
            mg_2014.append(list_year[k])
        if '英国' in list_city[k]:
            yg_2014.append(list_year[k])
        if '法国' in list_city[k]:
            fg_2014.append(list_year[k])
        if '日本' in list_city[k]:
            rb_2014.append(list_year[k])
    if list_year[k] == '2015':
        if '中国' in list_city[k]:
            zg_2015.append(list_year[k])
        if '美国' in list_city[k]:
            mg_2015.append(list_year[k])
        if '英国' in list_city[k]:
            yg_2015.append(list_year[k])
        if '法国' in list_city[k]:
            fg_2015.append(list_year[k])
        if '日本' in list_city[k]:
            rb_2015.append(list_year[k])
    if list_year[k] == '2016':
        if '中国' in list_city[k]:
            zg_2016.append(list_year[k])
        if '美国' in list_city[k]:
            mg_2016.append(list_year[k])
        if '英国' in list_city[k]:
            yg_2016.append(list_year[k])
        if '法国' in list_city[k]:
            fg_2016.append(list_year[k])
        if '日本' in list_city[k]:
            rb_2016.append(list_year[k])
    if list_year[k] == '2017':
        if '中国' in list_city[k]:
            zg_2017.append(list_year[k])
        if '美国' in list_city[k]:
            mg_2017.append(list_year[k])
        if '英国' in list_city[k]:
            yg_2017.append(list_year[k])
        if '法国' in list_city[k]:
            fg_2017.append(list_year[k])
        if '日本' in list_city[k]:
            rb_2017.append(list_year[k])
    if list_year[k] == '2018':
        if '中国' in list_city[k]:
            zg_2018.append(list_year[k])
        if '美国' in list_city[k]:
            mg_2018.append(list_year[k])
        if '英国' in list_city[k]:
            yg_2018.append(list_year[k])
        if '法国' in list_city[k]:
            fg_2018.append(list_year[k])
        if '日本' in list_city[k]:
            rb_2018.append(list_year[k])
    if list_year[k] == '2019':
        if '中国' in list_city[k]:
            zg_2019.append(list_year[k])
        if '美国' in list_city[k]:
            mg_2019.append(list_year[k])
        if '英国' in list_city[k]:
            yg_2019.append(list_year[k])
        if '法国' in list_city[k]:
            fg_2019.append(list_year[k])
        if '日本' in list_city[k]:
            rb_2019.append(list_year[k])

# sum_2012.remove(40150.5)
# number_2011 =len(sum_2011)
# number_2012 =len(sum_2012)
# number_2013 =len(sum_2013)
# number_2014 =len(sum_2014)
# number_2015 =len(sum_2015)
# number_2016 =len(sum_2016)
# number_2017 =len(sum_2017)
# number_2018 =len(sum_2018)
# number_2019 =len(sum_2019)
#
#
# sum_avg = [avg_2011,avg_2012,avg_2013,avg_2014,avg_2015,avg_2016,avg_2017,avg_2018,avg_2019]
#
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# # 使用两次 bar 函数画出两组条形图
# plt.bar(list1, height=sum_avg, color='darkcyan')
# # 坐标轴上移
# ax = plt.subplot(111)
# ax.spines['right'].set_color('none')     # 去掉右边的边框线
# ax.spines['top'].set_color('none')
#
# plt.ylabel('Price')  # 纵坐标轴标题
# plt.title('年份与平均票价关系图')  # 图形标题
# plt.savefig('year_price.jpg')
# plt.show()