import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

sum_zg = [len(zg_2011),len(zg_2012),len(zg_2013),len(zg_2014),len(zg_2015),len(zg_2016),len(zg_2017),len(zg_2018),len(zg_2019)]
sum_mg = [len(mg_2011),len(mg_2012),len(mg_2013),len(mg_2014),len(mg_2015),len(mg_2016),len(mg_2017),len(mg_2018),len(mg_2019)]
sum_yg = [len(yg_2011),len(yg_2012),len(yg_2013),len(yg_2014),len(yg_2015),len(yg_2016),len(yg_2017),len(yg_2018),len(yg_2019)]
sum_fg = [len(fg_2011),len(fg_2012),len(fg_2013),len(fg_2014),len(fg_2015),len(fg_2016),len(fg_2017),len(fg_2018),len(fg_2019)]
sum_rb = [len(rb_2011),len(rb_2012),len(rb_2013),len(rb_2014),len(rb_2015),len(rb_2016),len(rb_2017),len(rb_2018),len(rb_2019)]

plt.rcParams['font.sans-serif'] = ['SimHei']
bar_width = 0.15  # 条形宽度
index_zg = np.arange(len(sum_zg))
index_mg = index_zg + bar_width
index_yg = index_zg + bar_width + bar_width
index_fg = index_zg + bar_width + bar_width + bar_width
index_rb = index_zg + bar_width + bar_width + bar_width + bar_width
# 使用两次 bar 函数画出两组条形图
plt.bar(index_zg, height=sum_zg, width=bar_width, color='Chartreuse',label='中国')
plt.bar(index_mg, height=sum_mg, width=bar_width, color='MediumSpringGreen',label='美国')
plt.bar(index_yg, height=sum_mg, width=bar_width, color='DarkGreen',label='英国')
plt.bar(index_fg, height=sum_mg, width=bar_width, color='MediumAquamarine',label='法国')
plt.bar(index_rb, height=sum_mg, width=bar_width, color='Teal',label='日本')
# 坐标轴上移
ax = plt.subplot(111)
ax.spines['right'].set_color('none')     # 去掉右边的边框线
ax.spines['top'].set_color('none')
plt.legend()  # 显示图例
plt.xticks(index_zg + bar_width/2, list1,rotation=75)
plt.ylabel('number')  # 纵坐标轴标题
plt.title('每年各国电影数量对比')  # 图形标题
plt.savefig('year_city.jpg')
plt.show()