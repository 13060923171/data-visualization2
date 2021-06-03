import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
df = pd.read_excel('商品属性.xls').loc[:,['价钱','评论']]

list_price = []
for i in df['价钱']:
    i = i.replace('"','').replace("{",'').replace('price','').replace(':','').replace(' ','')\
        .replace('.00','').replace('.01','').replace('.99','').replace('.80','').replace('.90','').replace('.88','').replace('.20','')
    i = float(i)
    list_price.append(i)

list_comment = []
for i in df['评论']:
    i = i.strip(' ').replace('"comment":','').replace('"','').strip(' ').replace('万','0000').replace('+','')
    i = float(i)
    list_comment.append(i)

df1 = pd.DataFrame({'price':list_price,
                    'comment':list_comment}
                   )

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置加载的字体名
plt.rcParams['axes.unicode_minus'] = False   # 解决保存图像是负号'-'显示为方块的问题
# fig,axes=plt.subplots(2,1,figsize=(12,12))
sns.regplot(x='comment',y='price',data=df1,color='r',marker='+')
plt.savefig('线性回归图.png')
plt.show()