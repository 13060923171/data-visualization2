import pandas as pd

try:
    df = pd.read_csv(r'清洗后城市二手房数据.csv', encoding='utf-8')
except:
    df = pd.read_csv(r'清洗后城市二手房数据.csv', encoding='gbk')
city_lst = ['北京', '上海', '广东', '深圳', '沈阳', '大连']  # 城市
city = []  # 城市
guige = []  # 规格
area = [] #面积
new_guige = [[[],[],[],[],[],[]] for i in range(6)]
new_area = [[[],[],[],[],[],[]] for i in range(6)]

for index in df['城市']:
    city.append(index)
for index in df['规格']:
    guige.append(index)
for index in df['面积']:
    area.append(index)
for index in range(len(city)):
    for num in range(len(city_lst)):
        if city[index] == city_lst[num]:
            if str(city[index]) == "北京":
                new_guige[num][0].append(guige[index])
                new_area[num][0].append(area[index])
            elif str(city[index]) == "上海":
                new_guige[num][1].append(guige[index])
                new_area[num][1].append(area[index])
            elif str(city[index]) == "广东":
                new_guige[num][2].append(guige[index])
                new_area[num][2].append(area[index])
            elif str(city[index]) == "深圳":
                new_guige[num][3].append(guige[index])
                new_area[num][3].append(area[index])
            elif str(city[index]) == "沈阳":
                new_guige[num][4].append(guige[index])
                new_area[num][4].append(area[index])
            elif str(city[index]) == "大连":
                new_guige[num][5].append(guige[index])
                new_area[num][5].append(area[index])

print(new_guige[1][1])