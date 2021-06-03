from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
import pandas as pd

try:
    df = pd.read_csv(r'清洗后城市二手房数据.csv', encoding='utf-8')
except:
    df = pd.read_csv(r'清洗后城市二手房数据.csv', encoding='gbk')
city_lst = ['北京', '上海', '广东', '深圳', '沈阳', '大连']  # 城市
city = []  # 城市
buildTime = []  # 建房时期
new_buildTime = [[[], []] for i in range(6)]
data1 = []
data2 = []
for index in df['城市']:
    city.append(index)
for index in df['建房时期']:
    buildTime.append(index)
for index in range(len(city)):
    for num in range(len(city_lst)):
        if city[index] == city_lst[num]:
            if int(buildTime[index]) >= 2000:
                new_buildTime[num][1].append(buildTime[index])
            else:
                new_buildTime[num][0].append(buildTime[index])
for g in range(len(new_buildTime)):
    value1 = len(new_buildTime[g][0])
    value2 = len(new_buildTime[g][1])
    result1 = {'value': value1, 'percent': '%.2f' % (value1/(value1+value2))}
    result2 = {'value': value2, 'percent': '%.2f' % (value2/(value1+value2))}
    data1.append(result1)
    data2.append(result2)
print(data1)
print(data2)

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(city_lst)
    .add_yaxis("2000年以前建房", data1, stack="stack1", category_gap="50%")
    .add_yaxis("2000年以后建房", data2, stack="stack1", category_gap="50%")
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            formatter=JsCode(
                "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
            ),
        )
    )
    .render("各城市建房时期.html")
)