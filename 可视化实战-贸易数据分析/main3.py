from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType



#进口
x_data1 = ['美国','英国','德国','加拿大','日本','中国','法国','意大利','印度','西班牙','其他国家']
y_data1 = [161994.20,733.55,4926.8,19195.35,226.4,13693,1483.2,1957.35,1122.25,1963.8,float(349021.65-207295.9)]
data_pair_1 = [(i,j) for i, j in zip(x_data1,y_data1)]

#出口
x_data2 = ['美国','英国','德国','加拿大','日本','中国','法国','意大利','印度','西班牙','其他国家']
y_data2 = [586.45,10288.35,304.75,11070.65,4317.6,23650.40,21893.5,1957.35,1076.3,5344.2,float(365692.1-80489.55)]

data_pair_2 = [(i,j) for i, j in zip(x_data2,y_data2)]


c = (
    Pie(init_opts=opts.InitOpts(width="1300px", height="600px",theme=ThemeType.MACARONS))
    .add(
        series_name="进口",
        data_pair=data_pair_1,
        radius=["50%", "70%"],
        center=["25%", "50%"],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .add(
        series_name="出口",
        data_pair=data_pair_2,
        radius=["50%", "70%"],
        center=["75%", "50%"],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="近20年以来的进出口贸易环状图"))
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {d}%"
        ),
    )
    .render("./data/pie_rosetype.html")
)




