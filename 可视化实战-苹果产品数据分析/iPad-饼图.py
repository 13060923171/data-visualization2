import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

#调用pandas库读取数据
df = pd.read_excel('ipad数据.xlsx').loc[:,['颜色']]
#这一块全是清洗数据
list1 = []
for d in df['颜色']:
    d = d.split('和')
    list1.append(d)
list2 = []
for l in list1:
    l = str(l)
    l = l.split('、')
    for i in l:
        i = i.replace("'","").replace('[','').replace(']','')
        i = i.split(',')
        for j in i:
            j = j.strip(" ")
            list2.append(j)
#创建一个字典，去查看这些内容出现的频次
d = {}
for c in list2:
    d[c] = d.get(c,0)+1
ls = list(d.items())
#将列表从高到低进行排序
ls.sort(key=lambda x:x[1],reverse=True)

#开始写饼图代码
c = (
    #这是是设置页面的大小和主题
    Pie(init_opts=opts.InitOpts(width="1300px", height="600px",theme=ThemeType.PURPLE_PASSION))
    .add(
        "",
        ls,
        #这个是饼图的参数
        radius=["40%", "55%"],
        center=['50%','50%'],
    #     #这个是饼图文字的一些基本配置，例如字体的颜色，大小，等等
    #     label_opts=opts.LabelOpts(
    #         position="outside",
    #         formatter="{b}: {d}%",
    #         background_color="#eee",
    #         border_color="#aaa",
    #         border_width=1,
    #         border_radius=4,
    #         rich={
    #             "a": {"color": "#999", "lineHeight": 22, "align": "center"},
    #             "abg": {
    #                 "backgroundColor": "#e3e3e3",
    #                 "width": "100%",
    #                 "align": "right",
    #                 "height": 0,
    #                 "borderRadius": [4, 4, 0, 0],
    #             },
    #             "hr": {
    #                 "borderColor": "#aaa",
    #                 "width": "100%",
    #                 "borderWidth": 0.5,
    #                 "height": 10,
    #             },
    #             "b": {"fontSize": 16, "lineHeight": 33},
    #             "per": {
    #                 "color": "#eee",
    #                 "backgroundColor": "#334455",
    #                 "padding": [2, 4],
    #                 "borderRadius": 2,
    #             },
    #         },
    #     ),
    )
    #设置标题
    .set_global_opts(title_opts=opts.TitleOpts(title="iPad-颜色"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    .render("iPad-pie.html")
)


