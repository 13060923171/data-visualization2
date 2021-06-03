import pandas as pd

df = pd.read_excel('python_lagou.xlsx').loc[:,['city','salary']]

df['salary'] = df['salary'].apply(str)
df['city'] = df['city'].apply(str)

data = df.loc[df['city']=='西安']
list_float = []
for i in data['salary']:
    i = str(i)
    if 'k' not in i:
        list_float.append(i)


df2 = data[-data.salary.isin(list_float)]
list_salary = []
for s in df2['salary']:
    s = str(s)
    s = s.replace('k','000').split('-')
    s = s[1]
    list_salary.append(s)

sum = 0

for l in list_salary:
    try:
        l = int(l)
        sum += l
    except:
        pass
avg = sum/len(list_salary)
print('{:.1f}'.format(avg))
# df2 = df['salary']
# list_float = []
# try:
#     for i in df2:
#         i = str(i)
#         if 'k' not in i:
#             list_float.append(i)
# except:
#     pass
# df3 = df[-df.salary.isin(list_float)]
# df4 = df['city']
# list_city = []
# for j in df4:
#     j = str(j)
#     if len(j) >3:
#         list_city.append(j)
# # df5 = df3[-df3.salary.isin(list_city)]
# # data = df5['city'].value_counts()
# print(list_city)
# data_pair_1 = [(i, int(j)) for i, j in zip(data.index,data.values)]
# print(data_pair_1)

# del data_pair_1[('互联网行业', 1)]
# del data_pair_1[('每年涨薪制度',1)]
# del data_pair_1[('无办公室政治', 1)]
# del data_pair_1[('沟通能力好', 1)]
# del data_pair_1[('高提成', 1)]
# print(data_pair_1)

# list_city1 = []
# for c in df5['city']:
#     list_city1.append(c)
#
# list_salary = []
# for s in df5['salary']:
#     s = str(s)
#     s = s.replace('k','000').split('-')
#     s = s[0]
#     print(s)
#     list_salary.append(s)
# df5['salary'] = df5['salary'].str.split('-',expand=True)[0]
# df5['salary'] = df5['salary'].str.replace('k','000')
# df5['city'] = df5['city'].apply(str)
# df5 = df5.loc[df5['city'].str.contains('北京')]
# df6 = df5['salary']
#
# df6.mean(axis=0)
# print(df6)

# list_city = []
# df4 = df2['city']
# for j in df4:
#     j = str(j)
#     line = j.replace('沟通能力好', '').replace('沟通能力好', '').replace('无办公室政治', '').replace('1，负责课程咨询及招生工作，完', ''). \
#         replace('海外', '').replace('佛山', '广东').replace('茂名', '广东').replace('有挑战性', '').replace('东莞', '广东') \
#         .replace('中山', '广东').replace('每年涨薪制度', '').replace('高提成', '').replace('互联网行业', '').replace('上海市', '上海').replace(
#         '无办公室政治', '').replace('有挑战性', '').replace('互联网行业', '').replace('无办公室政治', '').
#     list_city.append(j)
# l2 = list(set(list_city))
# print(l2)
#
# data = [("江苏", 77), ("广东", 67), ("山东", 70), ("河南", 57), ("湖北", 68), ("四川", 52), ("湖南", 51), ("河北",
#     61), ("安徽", 46), ("辽宁", 64), ("浙江", 59), ("江西", 45), ("陕西", 57), ("北京", 68), ("福建", 39),
#     ("山西",33),("云南",32),("黑龙江",39),("广西",38),("贵州",29),("重庆",26),("上海",39),("吉林",37),
#     ("天津",30),("新疆",18),("内蒙古",17),("甘肃",22),("海南",8),("宁夏",8),("青海",4),("西藏",4)]
