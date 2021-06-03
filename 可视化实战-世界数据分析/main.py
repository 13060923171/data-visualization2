import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map,Page

df = pd.read_excel('汇总全球各国家每公顷粮食产量（千克_公顷）.xlsx')
a = df.iloc[[],2:78]

list1 = []
for i in a:
    i = i.split(":")
    list1.append(i[0])


with open('单词.txt','r',encoding='utf-8')as f:
    content = f.readlines()

list2 = []
for c in content:
    c = c.strip('\n')
    list2.append(c)

list3 = []
for i in range(len(list1)):
    l = list1[i]
    for j in range(len(list2)):
        k = list2[j]
        if l == k:
            list3.append(list2[j-2])

b = df.iloc[[0],2:78] #2017
c = df.iloc[[4],2:78] #2013
d = df.iloc[[8],2:78] #2009
e = df.iloc[[15],2:78] #2002

list_2017 = []
list_2013 = []
list_2009 = []
list_2002 = []

for i in range(len(b)):
    list_2017 = b.iloc[i].values.tolist()

for i in range(len(c)):
    list_2013 = c.iloc[i].values.tolist()

for i in range(len(d)):
    list_2009 = d.iloc[i].values.tolist()

for i in range(len(e)):
    list_2002 = e.iloc[i].values.tolist()

w = (
    Map()
    .add("2017", [list(z) for z in zip(list3,list_2017)], "world",label_opts=opts.LabelOpts(is_show=False),is_map_symbol_show=False,)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Grain production per hectare(A blank space is a lack of data)",pos_left="20%", pos_top="5%"),
        visualmap_opts=opts.VisualMapOpts(max_=10000),
    )
)

r = (
    Map()
    .add("2013", [list(z) for z in zip(list3,list_2013)], "world",label_opts=opts.LabelOpts(is_show=False),is_map_symbol_show=False,)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Grain production per hectare(A blank space is a lack of data)",pos_left="20%", pos_top="5%"),
        visualmap_opts=opts.VisualMapOpts(max_=10000),
    )
)

t = (
    Map()
    .add("2009", [list(z) for z in zip(list3,list_2009)], "world",label_opts=opts.LabelOpts(is_show=False),is_map_symbol_show=False,)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Grain production per hectare(A blank space is a lack of data)",pos_left="20%", pos_top="5%"),
        visualmap_opts=opts.VisualMapOpts(max_=10000),
    )
)

y = (
    Map()
    .add("2002", [list(z) for z in zip(list3,list_2002)], "world",label_opts=opts.LabelOpts(is_show=False),is_map_symbol_show=False,)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Grain production per hectare(A blank space is a lack of data)",pos_left="20%", pos_top="5%"),
        visualmap_opts=opts.VisualMapOpts(max_=10000),
    )
)

def page_default_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        w,
        r,
        t,
        y,
    )
    page.save_resize_html(cfg_file="chart_config.json")
    # page.render()

if __name__ == '__main__':
    page_default_layout()