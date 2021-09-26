import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('电影数据.csv',encoding='gbk').loc[:,['年份','场次','人次']]
rc = df['人次']
cc = df['场次']
year = df['年份']

list_rc = []
list_cc = []
list_year = []

for j in range(len(year)):
    t = year[j]
    t = str(t)
    t = t.replace('[','').replace(']','').replace("'","").replace(' ','')
    t = t.split(',')
    for i in t:
        if '-' in i:
            list_year.append(i[0:4])
            list_rc.append(rc[j])
            list_cc.append(cc[j])


list1 = list(set(list_year))
list1.sort(key=lambda x:x,reverse=False)

cc_2011 = []
cc_2012 = []
cc_2013 = []
cc_2014 = []
cc_2015 = []
cc_2016 = []
cc_2017 = []
cc_2018 = []
cc_2019 = []

for k in range(len(list_year)):
    if list_year[k] == '2011':
        if '万' in list_cc[k]:
            cc_2011.append(float(list_cc[k][:-1]))
    if list_year[k] == '2012':
        if '万' in list_cc[k]:
            cc_2012.append(float(list_cc[k][:-1]))
    if list_year[k] == '2013':
        if '万' in list_cc[k]:
            cc_2013.append(float(list_cc[k][:-1]))
    if list_year[k] == '2014':
        if '万' in list_cc[k]:
            cc_2014.append(float(list_cc[k][:-1]))
    if list_year[k] == '2015':
        if '万' in list_cc[k]:
            cc_2015.append(float(list_cc[k][:-1]))
    if list_year[k] == '2016':
        if '万' in list_cc[k]:
            cc_2016.append(float(list_cc[k][:-1]))
    if list_year[k] == '2017':
        if '万' in list_cc[k]:
            cc_2017.append(float(list_cc[k][:-1]))
    if list_year[k] == '2018':
        if '万' in list_cc[k]:
            cc_2018.append(float(list_cc[k][:-1]))
    if list_year[k] == '2019':
        if '万' in list_cc[k]:
            cc_2019.append(float(list_cc[k][:-1]))


rc_2011 = []
rc_2012 = []
rc_2013 = []
rc_2014 = []
rc_2015 = []
rc_2016 = []
rc_2017 = []
rc_2018 = []
rc_2019 = []

for k in range(len(list_year)):
    if list_year[k] == '2011':
        if '万' in list_rc[k]:
            rc_2011.append(float(list_rc[k][:-1]))
    if list_year[k] == '2012':
        if '万' in list_rc[k]:
            rc_2012.append(float(list_rc[k][:-1]))
    if list_year[k] == '2013':
        if '万' in list_rc[k]:
            rc_2013.append(float(list_rc[k][:-1]))
    if list_year[k] == '2014':
        if '万' in list_rc[k]:
            rc_2014.append(float(list_rc[k][:-1]))
    if list_year[k] == '2015':
        if '万' in list_rc[k]:
            rc_2015.append(float(list_rc[k][:-1]))
    if list_year[k] == '2016':
        if '万' in list_rc[k]:
            rc_2016.append(float(list_rc[k][:-1]))
    if list_year[k] == '2017':
        if '万' in list_rc[k]:
            rc_2017.append(float(list_rc[k][:-1]))
    if list_year[k] == '2018':
        if '万' in list_rc[k]:
            rc_2018.append(float(list_rc[k][:-1]))
    if list_year[k] == '2019':
        if '万' in list_rc[k]:
            rc_2019.append(float(list_rc[k][:-1]))

cc_2011 = sum(cc_2011) / len(cc_2011)
cc_2012 = sum(cc_2012) / len(cc_2012)
cc_2013 = sum(cc_2013) / len(cc_2013)
cc_2014 = sum(cc_2014) / len(cc_2014)
cc_2015 = sum(cc_2015) / len(cc_2015)
cc_2016 = sum(cc_2016) / len(cc_2016)
cc_2017 = sum(cc_2017) / len(cc_2017)
cc_2018 = sum(cc_2018) / len(cc_2018)
cc_2019 = sum(cc_2019) / len(cc_2019)

rc_2011 = sum(rc_2011) / len(rc_2011)
rc_2012 = sum(rc_2012) / len(rc_2012)
rc_2013 = sum(rc_2013) / len(rc_2013)
rc_2014 = sum(rc_2014) / len(rc_2014)
rc_2015 = sum(rc_2015) / len(rc_2015)
rc_2016 = sum(rc_2016) / len(rc_2016)
rc_2017 = sum(rc_2017) / len(rc_2017)
rc_2018 = sum(rc_2018) / len(rc_2018)
rc_2019 = sum(rc_2019) / len(rc_2019)

sum_rc = [rc_2011,rc_2012,rc_2013,rc_2014,rc_2015,rc_2016,rc_2017,rc_2018,rc_2019]
sum_cc = [cc_2011,cc_2012,cc_2013,cc_2014,cc_2015,cc_2016,cc_2017,cc_2018,cc_2019]
plt.rcParams['font.sans-serif']=['SimHei']
fig = plt.figure(figsize=(20, 10), dpi=80)
# 利用画布对象，在上面放置三个坐标系
# 新建子图1
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(list1, sum_cc)
ax1.grid(color='b', linestyle='--', linewidth=1, alpha=0.3)
ax1.set_ylabel('单位(/万)')
ax1.set_title('每年总场次平均值变化')
# 新建子图2
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(list1, sum_rc)  # x的二次方，如果是x**3是x的三次方
ax2.grid(color='r', linestyle='--', linewidth=1, alpha=0.3)
ax2.set_ylabel('单位(/万)')
ax2.set_title('每年总人次平均值变化')
plt.savefig('rc_cc.jpg')
plt.show()