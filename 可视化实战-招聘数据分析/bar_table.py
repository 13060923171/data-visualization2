import pandas as pd
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

#获取数据
df = pd.read_excel('数据.xls').loc[:,['薪水','工作地点']]
list_city = []
d = {}
#对数据进行筛选筛选好的数据添加到列表中
for c in df['工作地点']:
    c = str(c)
    c = c[0:2]
    c = c.replace('石家', '石家庄').replace('哈尔', '黑龙江').replace('广东', '广州')
    list_city.append(c)

#做数据累加，获取每个城市出现的次数
for c in list_city:
    d[c] = d.get(c,0) +1
list1 = list(d.items())
#让城市从大到小进行排序
list1.sort(key=lambda x:x[1],reverse=True)
#筛选前十的城市
list1 = list1[0:10]

#对数据清洗，求每一个的平均薪资
list_salary = []
for s in df['薪水']:
    s = str(s)
    if '万/月' in s:
        s = s.split('-')
        avg = float(float(s[0]) + float(s[1].replace('万/月',''))) / 2
        avg1 = round(float(avg) * 10000)
        list_salary.append(avg1)
    elif '千/月' in s:
        s = s.split('-')
        avg = float(float(s[0]) + float(s[1].replace('千/月',''))) / 2
        avg1 = round(float(avg) * 1000)
        list_salary.append(avg1)
    #不符合规范的数据清零去除，使得整体数据干净
    else:
        s = 0
        list_salary.append(s)

list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
list_6 = []
list_7 = []
list_8 = []
list_9 = []
list_10 = []

#根据关键词来获取该城市的总的平均工资
for i in range(len(list_city)):
    if '上海' in list_city[i]:
        list_1.append(list_salary[i])
    elif '深圳' in list_city[i]:
        list_2.append(list_salary[i])
    elif '广州' in list_city[i]:
        list_3.append(list_salary[i])
    elif '武汉' in list_city[i]:
        list_4.append(list_salary[i])
    elif '成都' in list_city[i]:
        list_5.append(list_salary[i])
    elif '北京' in list_city[i]:
        list_6.append(list_salary[i])
    elif '南京' in list_city[i]:
        list_7.append(list_salary[i])
    elif '杭州' in list_city[i]:
        list_8.append(list_salary[i])
    elif '苏州' in list_city[i]:
        list_9.append(list_salary[i])
    elif '西安' in list_city[i]:
        list_10.append(list_salary[i])

x_data = []
for i in list1:
    x_data.append(i[0])
#再对每个城市总的工资求其平均数，获取到每个城市薪资的平均数
y_data = []
sum_avg1 = int(sum(list_1) / len(list_1))
y_data.append(sum_avg1)
sum_avg2 = int(sum(list_2) / len(list_2))
y_data.append(sum_avg2)
sum_avg3 = int(sum(list_3) / len(list_3))
y_data.append(sum_avg3)
sum_avg4 = int(sum(list_4) / len(list_4))
y_data.append(sum_avg4)
sum_avg5 = int(sum(list_5) / len(list_5))
y_data.append(sum_avg5)
sum_avg6 = int(sum(list_6) / len(list_6))
y_data.append(sum_avg6)
sum_avg7 = int(sum(list_7) / len(list_7))
y_data.append(sum_avg7)
sum_avg8 = int(sum(list_8) / len(list_8))
y_data.append(sum_avg8)
sum_avg9 = int(sum(list_9) / len(list_9))
y_data.append(sum_avg9)
sum_avg10 = int(sum(list_10) / len(list_10))
y_data.append(sum_avg10)

#最后把整理好的数据生成柱状图
def get_bar():
    c = (
        #柱状图的主题
        Bar({"theme": ThemeType.MACARONS})
        #柱状图的X轴
            .add_xaxis(x_data)
        #柱状图的Y轴
            .add_yaxis("", y_data)
        #柱状图的标题
            .set_global_opts(
            title_opts={"text": "最热门的平均薪资"}
        )
    )
    return c


