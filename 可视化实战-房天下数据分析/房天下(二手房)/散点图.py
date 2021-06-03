from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
import pandas as pd
import pyecharts as pyec
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
y_data = ["1室1厅", "1室0厅", "1室2厅", "1室3厅", "1室4厅", "2室0厅",'2室1厅','2室2厅','2室3厅','2室4厅',
          "3室0厅",'3室1厅','3室2厅','3室3厅','3室4厅',"4室0厅",'4室1厅','4室2厅','4室3厅','4室4厅',
          "5室0厅",'5室1厅','5室2厅','5室3厅','5室4厅',"6室0厅",'6室1厅','6室2厅','6室3厅','6室4厅']
x_data = ['0-50','50-100','100-150','150-200','200-250','250-300','300-350','350-400','4000-450','450-500','500-550','550-600']

c = (
    Scatter()
        .add_xaxis(x_data)
        .add_yaxis(
        "北京",
        [list(z) for z in zip(new_area[0][0],new_guige[0][0])],
        # 标记的大小
        symbol_size=20,
        #标签配置项
        label_opts=opts.LabelOpts(
            formatter=JsCode(
                # 构造回调函数
                "function(params){return params.value[1] +' : '+ params.value[2];}"
            )  #params.value[1]对应y轴Faker.values() :  params.value[2]对应y轴Faker.choose()
        ),
    )
        .add_yaxis(
        "上海",
        [list(z) for z in zip(new_area[1][1],new_guige[1][1])],
        # 标记的大小
        symbol_size=20,
        #标签配置项
        label_opts=opts.LabelOpts(
            formatter=JsCode(
                # 构造回调函数
                "function(params){return params.value[1] +' : '+ params.value[2];}"
            )  #params.value[1]对应y轴Faker.values() :  params.value[2]对应y轴Faker.choose()
        ),
    )
        .add_yaxis(
        "广东",
        [list(z) for z in zip(new_area[2][2],new_guige[2][2])],
        # 标记的大小
        symbol_size=20,
        #标签配置项
        label_opts=opts.LabelOpts(
            formatter=JsCode(
                # 构造回调函数
                "function(params){return params.value[1] +' : '+ params.value[2];}"
            )  #params.value[1]对应y轴Faker.values() :  params.value[2]对应y轴Faker.choose()
        ),
    )
        .add_yaxis(
        "深圳",
        [list(z) for z in zip(new_area[3][3],new_guige[3][3])],
        # 标记的大小
        symbol_size=20,
        #标签配置项
        label_opts=opts.LabelOpts(
            formatter=JsCode(
                # 构造回调函数
                "function(params){return params.value[1] +' : '+ params.value[2];}"
            )  #params.value[1]对应y轴Faker.values() :  params.value[2]对应y轴Faker.choose()
        ),
    )
        .add_yaxis(
        "沈阳",
        [list(z) for z in zip(new_area[4][4],new_guige[4][4])],
        # 标记的大小
        symbol_size=20,
        #标签配置项
        label_opts=opts.LabelOpts(
            formatter=JsCode(
                # 构造回调函数
                "function(params){return params.value[1] +' : '+ params.value[2];}"
            )  #params.value[1]对应y轴Faker.values() :  params.value[2]对应y轴Faker.choose()
        ),
    )
        .add_yaxis(
        "大连",
        [list(z) for z in zip(new_area[5][5],new_guige[5][5])],
        # 标记的大小
        symbol_size=20,
        #标签配置项
        label_opts=opts.LabelOpts(
            formatter=JsCode(
                # 构造回调函数
                "function(params){return params.value[1] +' : '+ params.value[2];}"
            )  #params.value[1]对应y轴Faker.values() :  params.value[2]对应y轴Faker.choose()
        ),
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="Scatter-多维度数据"),
        # 提示框配置项
        tooltip_opts=opts.TooltipOpts(
            formatter=JsCode(
                # 构造回调函数
                "function (params) {return params.name + ' : ' + params.value[2];}"
            )  #params.name对应x轴的Faker.choose() : params.value[2]对应y轴Faker.choose()
        ),
        # 视觉映射配置项
        visualmap_opts=opts.VisualMapOpts(
            #颜色映射
            type_="color",
            max_=150,
            min_=20,
            dimension=1  ## 组件映射维度
        ),
    )
    .render("scatter_multi_dimension.html")
)
