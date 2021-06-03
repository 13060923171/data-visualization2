import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd

try:
    df = pd.read_csv(r'清洗后城市二手房数据.csv', encoding='utf-8')
except:
    df = pd.read_csv(r'清洗后城市二手房数据.csv', encoding='gbk')
city_lst = ['北京', '上海', '广东', '深圳', '沈阳', '大连']  # 城市
city = []  # 城市
price = []  # 建房时期
new_buildTime = [[[], [],[],[],[],[]] for i in range(6)]
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
for index in df['城市']:
    city.append(index)
for index in df['总价']:
    price.append(index)
for index in range(len(city)):
    for num in range(len(city_lst)):
        if city[index] == city_lst[num]:
            if str(city[index]) == "北京":
                new_buildTime[num][0].append(price[index])
            elif str(city[index]) == "上海":
                new_buildTime[num][1].append(price[index])
            elif str(city[index]) == "广东":
                new_buildTime[num][2].append(price[index])
            elif str(city[index]) == "深圳":
                new_buildTime[num][3].append(price[index])
            elif str(city[index]) == "沈阳":
                new_buildTime[num][4].append(price[index])
            elif str(city[index]) == "大连":
                new_buildTime[num][5].append(price[index])


for g in range(len(new_buildTime)):
    data1.append(new_buildTime[g][0])
    data2.append(new_buildTime[g][1])
    data3.append(new_buildTime[g][2])
    data4.append(new_buildTime[g][3])
    data5.append(new_buildTime[g][4])
    data6.append(new_buildTime[g][5])

x_data = ["0-100", "100-200", "200-300", "300-400", "400-500", "500-600",'600-700','700-800','800-900','900-1000','1000-2000']

(
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="北京",
        stack="总量",
        y_axis=new_buildTime[0][0],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="上海",
        stack="总量",
        y_axis=new_buildTime[1][1],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="广东",
        stack="总量",
        y_axis=new_buildTime[2][2],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="深圳",
        stack="总量",
        y_axis=new_buildTime[3][3],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="沈阳",
        stack="总量",
        y_axis=new_buildTime[4][4],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
            series_name="大连",
            stack="总量",
            y_axis=new_buildTime[5][5],
            label_opts=opts.LabelOpts(is_show=False),
        )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="折线图堆叠"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("stacked_line_chart.html")
)