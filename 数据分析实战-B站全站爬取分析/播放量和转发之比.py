import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
df = pd.read_csv('非遗top100信息表.csv')

def szth(x):
    if '万' in x:
        x = str(x).replace('万','')
        x = float(x) * 10000
        return x
    elif '分享' in x:
        return 0
    else:
        return x

title = list(df['标题'].replace(' ',''))
bfl = list(df['播放量'])
df['转发'] = df['转发'].apply(szth)
zf = list(df['转发'])


c = (
    Bar(init_opts=opts.InitOpts(width="1600px", height="800px",theme=ThemeType.DARK))
    .add_xaxis(title)
    .add_yaxis("播放量", bfl,label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis("转发", zf,label_opts=opts.LabelOpts(is_show=False))
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="播放量和转发之比"),
        # datazoom_opts=opts.DataZoomOpts(),
        datazoom_opts=opts.DataZoomOpts(orient="vertical"),
    )
    .render("./HTML文件储存/播放量和转发之比.html")
)

bfl_100 = []
bfl_200 = []
bfl_300 = []
bfl_400 = []
bfl_500 = []
bfl_600 = []
bfl_700 = []
zf_100 = []
zf_200 = []
zf_300 = []
zf_400 = []
zf_500 = []
zf_600 = []
zf_700 = []

for j,k in zip(bfl,zf):
    j = int(j)
    k = int(k)
    if j < 1000000:
        bfl_100.append(j)
        zf_100.append(k)
    elif 1000000 <= j < 2000000:
        bfl_200.append(j)
        zf_200.append(k)
    elif 2000000 <= j < 3000000:
        bfl_300.append(j)
        zf_300.append(k)
    elif 3000000 <= j < 4000000:
        bfl_400.append(j)
        zf_400.append(k)
    elif 4000000 <= j < 5000000:
        bfl_500.append(j)
        zf_500.append(k)
    elif 5000000 <= j < 6000000:
        bfl_600.append(j)
        zf_600.append(k)
    elif 6000000 <= j < 7000000:
        bfl_700.append(j)
        zf_700.append(k)

x_data = ['100万之内','100-200万之间','200-300万之间','300-400万之间','400-500万之间','500-600万之间','600-700万之间']
y_data = [sum(bfl_100),sum(bfl_200),sum(bfl_300),sum(bfl_400),sum(bfl_500),sum(bfl_600),sum(bfl_700)]
y_data1 = [sum(zf_100),sum(zf_200),sum(zf_300),sum(zf_400),sum(zf_500),sum(zf_600),sum(zf_700)]

c = (
    Bar(init_opts=opts.InitOpts(width="1600px", height="800px",theme=ThemeType.ESSOS))
    .add_xaxis(x_data)
    .add_yaxis("播放量", y_data,gap="0%")
    .add_yaxis("转发", y_data1,gap="0%")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="播放量和转发总量之比"),
    )
    .render("./HTML文件储存/播放量和转发总量之比.html")
)