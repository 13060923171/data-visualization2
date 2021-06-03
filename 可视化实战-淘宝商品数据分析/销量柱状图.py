import pandas as pd
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar
import pyecharts.options as opts

df = pd.read_excel('商品的基本信息.xlsx')

price_list = []
for p in df['价格']:
    p = str(p)
    p = p.replace('(','').replace(')','').replace(',','').replace("'","").replace('¥','')\
        .replace('.00','').replace('.10','').replace('.20','').replace('.30','').replace('.40','')\
        .replace('.50','').replace('.60','').replace('.70','').replace('.80','').replace('.90','').replace('.99','')\
        .replace('.55','').replace('.05','')

    price_list.append(p)

deal_list = []
for d in df['付款人数']:
    d = str(d)
    d = d.replace('(','').replace(')','').replace(',','').replace("'","").\
        replace('人','').replace('付款','').replace('万','0000').replace('.0','').replace('+','').replace('1.50000','15000')
    d = d.replace('\n','0')
    deal_list.append(d)

list_50 = []
list_100 = []
list_150 = []
list_200 = []
list_250 = []
list_300 = []
list_350 = []
list_400 = []

for p in range(len(price_list)):
    price = int(price_list[p])
    if price<50:
        list_50.append(int(deal_list[p]))
    if 50 <= price <= 100:
        list_100.append(deal_list[p])
    if 100 < price <= 150:
        list_150.append(int(deal_list[p]))
    if 150 < price <= 200:
        list_200.append(deal_list[p])
    if 200 < price <= 250:
        list_250.append(deal_list[p])
    if 250 < price <= 300:
        list_300.append(deal_list[p])
    if 300 < price <= 350:
        list_350.append(int(deal_list[p]))
    if price > 350:
        list_400.append(deal_list[p])

x_data = ['0-50','50-100','100-150','150-200','200-250','250-300','300-350','350以上']
#0-50
list_50_sum = sum(list_50)


#50-100
for p in list_100:
    p = str(p)
    if p == '':
        list_100.remove('')
    if p ==  '':
        list_100.remove( '')

list_100_sum = 0
for i in list_100:
    i = int(i)
    list_100_sum += i


#100-150
list_150_sum = sum(list_150)

#150-200
for p in list_200:
    p = str(p)
    if p == '':
        list_200.remove('')
    if p ==  '':
        list_200.remove( '')

list_200_sum = 0
for i in list_200:
    i = int(i)
    list_200_sum += i

#200-250
for p in list_250:
    p = str(p)
    if p == '':
        list_250.remove('')



list_250_sum = 0
for i in list_250[:-1]:
    i = int(i)
    list_250_sum += i

#250-300
for p in list_300:
    p = str(p)
    if p == '':
        list_300.remove('')
    if p ==  '':
        list_300.remove( '')

list_300_sum = 0
for i in list_300:
    i = int(i)
    list_300_sum += i

#300-350
list_350_sum = sum(list_350)

#350以上
for p in list_400:
    p = str(p)
    if p == '':
        list_400.remove('')


list_400_sum = 0
for i in list_400[:-1]:
    i = int(i)
    list_400_sum += i

y_data = []
y_data.append(list_50_sum)
y_data.append(list_100_sum)
y_data.append(list_150_sum)
y_data.append(list_200_sum)
y_data.append(list_250_sum)
y_data.append(list_300_sum)
y_data.append(list_350_sum)
y_data.append(list_400_sum)
print(y_data)

c = (
    Bar(init_opts=opts.InitOpts(width="1300px", height="600px",theme=ThemeType.MACARONS))
    .add_xaxis(x_data)
    .add_yaxis("销量", y_data,label_opts=opts.LabelOpts(is_show=False))

    .set_global_opts(
        title_opts={"text": "各个价位卫衣销售量"}
    )
    .render("bar.html")
)