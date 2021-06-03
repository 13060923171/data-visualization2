import pyecharts.options as opts
from pyecharts.charts import Radar
from pyecharts.globals import ThemeType

#这个是从表格中读取到的数据，进行雷达的数据集
v1 = [['62.02', '19.60', '13.82', '8.09','7.07','4.36','30.31']]

def main_radar():
    c = (
        #创建雷达图表，设置雷达的大小和主题
        Radar()
        .add_schema(
            #雷达每个角的大小和对应的内容
            schema=[
                opts.RadarIndicatorItem(name="产假/哺乳期等专属假期", max_=80.00),
                opts.RadarIndicatorItem(name="为女性提供弹性工作制", max_=80.00),
                opts.RadarIndicatorItem(name="提供母婴室、哺乳室等设施", max_=80.00),
                opts.RadarIndicatorItem(name="为女性员工规划职业发展", max_=80.00),
                opts.RadarIndicatorItem(name="提供女性专题培训课程", max_=80.00),
                opts.RadarIndicatorItem(name="成立女性领导力小组", max_=80.00),
                opts.RadarIndicatorItem(name="无", max_=80.00),

            ],
            #雷达的形状
            shape="circle",
            #雷达的文字大小和颜色
            splitarea_opt=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
            textstyle_opts=opts.TextStyleOpts(color="#EF5350"),
        )
        #雷达的线
        .add(
            series_name="支持力度(单位:%)",
            data=v1,
            linestyle_opts=opts.LineStyleOpts(color="#EF5350"),
        )
        #雷达的标题
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        #雷达标题的位置
        .set_global_opts(
            title_opts=opts.TitleOpts(title="社会及政策层面对于女性的支持程度和状况",pos_left="left"), legend_opts=opts.LegendOpts()
        )
    )
    return c

