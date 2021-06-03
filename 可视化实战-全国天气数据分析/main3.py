import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

df = pd.read_csv('./csv_file/景点.csv',encoding='gbk').loc[:,['city','风力']]
df.dropna(axis=0,how='any',inplace=True)
df[df.isnull().T.any()]
list_city = []
for i in df['city']:
    i = str(i)
    i = i.replace('city:','').strip(' ')
    list_city.append(i)

list_fenli = []
for j in df['风力']:
    j = str(j)
    j = j.split(' ')
    j = j[1]
    j = j.replace('3-5级','4').replace('微风','2')
    list_fenli.append(j)

c = (
    Bar()
    .add_xaxis(list_city)
    .add_yaxis("风力", list_fenli)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="风力等级"),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
    )
    .render("bar_datazoom_both.html")
)
