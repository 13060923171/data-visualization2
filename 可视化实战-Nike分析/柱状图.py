import pandas as pd
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar
import pyecharts.options as opts


df = pd.read_csv('NIKE 510.csv').loc[:,['价格','评价人数']]




list_500 = []
list_1000 = []
list_1500 = []
list_2000 = []
list_2500 = []
list_3000 = []
for i in range(len(df['价格'])):
    if int(df['价格'][i]) <= int(500):
        list_500.append(df['评价人数'][i])
    if int(500) < int(df['价格'][i]) <= int(1000):
        list_1000.append(df['评价人数'][i])
    if int(1000) < int(df['价格'][i]) <= int(1500):
        list_1500.append(df['评价人数'][i])
    if int(1500) < int(df['价格'][i]) <= int(2000):
        list_2000.append(df['评价人数'][i])
    if int(2000) < int(df['价格'][i]) <= int(2500):
        list_2500.append(df['评价人数'][i])
    if int(df['价格'][i]) > int(2500):
        list_3000.append(df['评价人数'][i])

sum1 = 0
for l1 in list_500:
    l1 = l1.replace('.1万+','1000').replace('.2万+','2000').replace('.3万+','3000').replace('.4万+','4000').replace('.5万+','5000')\
        .replace('.6万+','6000').replace('.7万+','7000').replace('.8万+','8000')\
        .replace('.9万+','9000').replace('万+','0000').replace('+','')
    sum1 += int(l1)

sum2 = 0
for l1 in list_1000:
    l1 = l1.replace('.1万+','1000').replace('.2万+','2000').replace('.3万+','3000').replace('.4万+','4000').replace('.5万+','5000')\
        .replace('.6万+','6000').replace('.7万+','7000').replace('.8万+','8000')\
        .replace('.9万+','9000').replace('万+','0000').replace('+','')
    sum2 += int(l1)

sum3 = 0
for l1 in list_1500:
    l1 = l1.replace('.1万+','1000').replace('.2万+','2000').replace('.3万+','3000').replace('.4万+','4000').replace('.5万+','5000')\
        .replace('.6万+','6000').replace('.7万+','7000').replace('.8万+','8000')\
        .replace('.9万+','9000').replace('万+','0000').replace('+','')
    sum3 += int(l1)

sum4 = 0
for l1 in list_2000:
    l1 = l1.replace('.1万+','1000').replace('.2万+','2000').replace('.3万+','3000').replace('.4万+','4000').replace('.5万+','5000')\
        .replace('.6万+','6000').replace('.7万+','7000').replace('.8万+','8000')\
        .replace('.9万+','9000').replace('万+','0000').replace('+','')
    sum4 += int(l1)

sum5 = 0
for l1 in list_2500:
    l1 = l1.replace('.1万+','1000').replace('.2万+','2000').replace('.3万+','3000').replace('.4万+','4000').replace('.5万+','5000')\
        .replace('.6万+','6000').replace('.7万+','7000').replace('.8万+','8000')\
        .replace('.9万+','9000').replace('万+','0000').replace('+','')
    sum5 += int(l1)

sum6 = 0
for l1 in list_3000:
    l1 = l1.replace('.1万+','1000').replace('.2万+','2000').replace('.3万+','3000').replace('.4万+','4000').replace('.5万+','5000')\
        .replace('.6万+','6000').replace('.7万+','7000').replace('.8万+','8000')\
        .replace('.9万+','9000').replace('万+','0000').replace('+','')
    sum6 += int(l1)


x_data = ['0-500','500-1000','1000-1500','1500-2000','2000-2500','2500以上']
y_data = []
y_data.append(sum1)
y_data.append(sum2)
y_data.append(sum3)
y_data.append(sum4)
y_data.append(sum5)
y_data.append(sum6)

c = (
    Bar(init_opts=opts.InitOpts(width="1300px", height="600px",theme=ThemeType.MACARONS))
    .add_xaxis(x_data)
    .add_yaxis("评论数量", y_data,label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts={"text": "不同价位的评论数量"}
    )
    .render("bar.html")
)
