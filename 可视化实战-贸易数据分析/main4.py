import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import HeatMap

def new_round(_float, _len):
    if isinstance(_float, float):
        if str(_float)[::-1].find('.') <= _len:
            return (_float)
        if str(_float)[-1] == '5':
            return (round(float(str(_float)[:-1] + '6'), _len))
        else:
            return (round(_float, _len))
    else:
        return (round(_float, _len))

def ms_data():
    df = pd.read_csv('./data/前十国家商品出口总额.csv').loc[:,['Exporters','Exported value in average']]
    list_value = []
    for i in range(len(df['Exported value in average'])):
        value = df['Exported value in average'][i] / df['Exported value in average'][0]
        list_value.append(new_round(float(value), 4))
    del list_value[0]
    return list_value

def tc_data():
    df1 = pd.read_csv('./data/前十国家商品出口总额.csv').loc[:, ['Exporters', 'Exported value in average']]
    df = pd.read_csv('./data/前十国家商品进口总额.csv').loc[:, ['Importers', 'Imported value in average']]
    list_value = []
    for i in range(len(df['Imported value in average'])):
        value = (df1['Exported value in average'][i] - df['Imported value in average'][i]) / (df1['Exported value in average'][i] + df['Imported value in average'][i])
        list_value.append(new_round(float(value), 4))
    del list_value[0]
    return list_value

def rca_data():
    df = pd.read_csv('./data/前十国家商品进口总额.csv').loc[:, ['Imported value in average']]
    df1 = pd.read_csv('./data/前十国家商品出口总额.csv').loc[:, ['Exported value in average']]
    df2 = pd.read_csv('./data/前十国家电影出口总额.csv').loc[:, [ 'Exported value in average']]
    df3 = pd.read_csv('./data/前十国家电影进口总额.csv').loc[:, [ 'Imported value in average']]
    list_value = []
    for i in range(len(df['Imported value in average'])):
        value = (df2['Exported value in average'][i] / df1['Exported value in average'][i]) / (df2['Exported value in average'][0]/df1['Exported value in average'][0])
        list_value.append(new_round(float(value), 4))
    del list_value[0]
    return list_value

def caab_data():
    df = pd.read_csv('./data/前十国家商品进口总额.csv').loc[:, ['Imported value in average']]
    df1 = pd.read_csv('./data/前十国家商品出口总额.csv').loc[:, ['Exported value in average']]
    df2 = pd.read_csv('./data/前十国家电影出口总额.csv').loc[:, ['Exported value in average']]
    df3 = pd.read_csv('./data/前十国家电影进口总额.csv').loc[:, ['Imported value in average']]
    rcaab = rca_data()
    rcaab.insert(0,0)
    list_value = []
    for i in range(len(df['Imported value in average'])):
        value = rcaab[i] - ((df3['Imported value in average'][i] / df3['Imported value in average'][0]) / (df['Imported value in average'][i] / df['Imported value in average'][0]))
        list_value.append(new_round(float(value), 4))
    del list_value[0]
    return list_value


x_data = ['美国','中国','德国','日本','英国','法国','意大利','加拿大','印度','西班牙']
y_data = ['MS','TC','RCA','CAAB']
list_1 = ms_data()
list_2 = tc_data()
list_3 = rca_data()
list_4 = caab_data()

sum_list = []

for c in range(10):
    for a in range(1):
        data = [c,a,list_1[c]]
    sum_list.append(data)

for c in range(10):
    for a in range(1,2,1):
        data = [c,a,list_2[c]]
    sum_list.append(data)

for c in range(10):
    for a in range(2,3,1):
        data = [c,a,list_3[c]]
    sum_list.append(data)

for c in range(10):
    for a in range(3,4,1):
        data = [c,a,list_4[c]]
    sum_list.append(data)


c = (
    HeatMap()
    .add_xaxis(x_data)
    .add_yaxis(
        "",
        y_data,
        sum_list,
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全球近20年进出口贸易平均值指标"),
        visualmap_opts=opts.VisualMapOpts(
            min_=0,
            max_=20
        ),
    )
    .render("./data/heatmap_with_label_show.html")
)

