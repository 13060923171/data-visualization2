import pandas as pd
import numpy as np

df = pd.read_csv('#西安疫情#.csv')
print(df)

def main1(x):
    x1 = str(x)
    x1 = x1.replace("'","").replace("[","").replace("]","").replace(" ","").replace("\n","")
    x1 = str(x1)
    x2 = x1.split('\\n')
    return x2[1]

def main2(x):
    x1 = str(x)
    x1 = x1.replace("'","").replace("[","").replace("]","").replace(" ","").replace("\n","")
    x1 = str(x1)
    x2 = x1.split('\\n')
    return x2[0]

def main3(x):
    x1 = str(x)
    x1 = x1.replace("'","").replace("[","").replace("]","").replace(" ","").replace("\n","")
    x1 = str(x1)
    x2 = x1.split('\\n')

    try:
        x2 = x2[0]
    except:
        x2 = '无'
    return x2

def main4(x):
    x1 = str(x)
    x1 = x1.replace("'","").replace("[","").replace("]","").replace(" ","").replace("\n","").replace("\u200b","")
    x1 = str(x1)
    x2 = x1.split('\\n')
    return x2[0]

def main5(x):
    x1 = str(x)
    x1 = x1.replace("'","").replace("[","").replace("]","").replace(" ","").replace("\n","").replace("\u200b","")
    if x1 == '赞':
        return 0
    else:
        return x1

def main6(x):
    x1 = str(x)
    x1 = x1.replace("'","").replace("[","").replace("]","").replace(" ","").replace("\n","").replace("\u200b","").replace(",","")
    if x1 == '转发':
        return 0
    else:
        return x1

def main7(x):
    x1 = str(x)
    x1 = x1.replace("'","").replace("[","").replace("]","").replace(" ","").replace("\n","").replace("\u200b","").replace(",","")
    if x1 == '评论':
        return 0
    else:
        return x1

df['时间'] = df['时间'].apply(main1)
df['博主'] = df['博主'].apply(main2)
df['认证'] = df['认证'].apply(main3)
df['内容'] = df['内容'].apply(main4)
df['点赞'] = df['点赞'].apply(main5)
df['转发'] = df['转发'].apply(main6)
df['评论'] = df['评论'].apply(main7)
df = df.drop_duplicates(subset=['内容'],keep='first')
print(df)


def main8(x):
    x1 = str(x)
    if '01月' in x1:
        x1 = '2022年' + x1
    if '12月' in x1:
        return x1
    elif '01月' in x1:
        return x1
    else:
        return np.NaN


df['时间'] = df['时间'].apply(main8)
df1 = df.dropna(how='any',axis=0)
# df1['时间'] = df1['时间'].apply(main9)
df1.to_csv('new_西安疫情.csv',encoding='utf-8-sig',index=None)