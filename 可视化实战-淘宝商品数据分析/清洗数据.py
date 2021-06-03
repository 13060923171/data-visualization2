import pandas as pd

df = pd.read_excel('商品的基本信息.xlsx')
title_list = []
for t in df['标题']:
    t = str(t)
    t = t.replace('(','').replace(')','').replace(',','').replace("'","")
    # title_list.append(t)
    with open('标题.txt','a+',encoding='utf-8')as f:
        f.write(t+'\n')

price_list = []
for p in df['价格']:
    p = str(p)
    p = p.replace('(','').replace(')','').replace(',','').replace("'","").replace('¥','')
    price_list.append(p)

deal_list = []
for d in df['付款人数']:
    d = str(d)
    d = d.replace('(','').replace(')','').replace(',','').replace("'","").\
        replace('人','').replace('付款','').replace('万','0000').replace('.0','').replace('+','').replace('1.50000','15000')
    d = d.replace('\n','0')
    # if d == '':
    #     d = 0
    #     deal_list.append(d)
    deal_list.append(d)


location_list = []
for l in df['发货地址']:
    l = str(l)
    l = l.replace('(','').replace(')','').replace(',','').replace("'","")
    l = l[0:2]
    location_list.append(l)

