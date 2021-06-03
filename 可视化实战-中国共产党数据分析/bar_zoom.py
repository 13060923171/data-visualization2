from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar,Timeline,Pie

year = [
    2000,
    2001,
    2002,
    2003,
    2004,
    2005,
    2006,
    2007,
    2008,
    2009,
    2010,
    2011,
    2012,
    2013,
    2014,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020
]
renkou=[
    3209,
    2927,
    2820,
    2900,
    2610,
    2365,
    2148,
    1479,
    4007,
    3597,
    16567,
    12238,
    9899,
    8249,
    7017,
    5575,
    4335,
    3046,
    1660,
    551,
    0]
y_data = [3.5,3.2,3.1,2.8,2.5,2.3,1.6,4.2,3.8,17.2,12.7,10.2,8.5,7.2,5.7,4.5,3.1,1.7,0.6]
def Bar_zoom():
    scatter1 = (
        Bar({"theme": ThemeType.INFOGRAPHIC})
        .add_xaxis(year)
        .add_yaxis("贫困人口(单位:人数)", renkou, yaxis_index=0)
        .extend_axis(yaxis=opts.AxisOpts())
        .set_global_opts(
            datazoom_opts=opts.DataZoomOpts(),
            title_opts=opts.TitleOpts(
                        title="中国人民的脱贫趋势",
                        pos_left="left",
                        pos_top="top",)
                         )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    )
    return scatter1