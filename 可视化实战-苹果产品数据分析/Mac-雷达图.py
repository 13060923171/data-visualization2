import pyecharts.options as opts
from pyecharts.charts import Radar

#创建雷达图需要的数据集
v1 = [['1.61', '30.41', '21.24', '1.29']]
v2 = [['1.61', '30.41', '21.24', '1.29']]
v3 = [['1.7', '32.5', '22.7', '1.35']]
v4 = [['1.56', '30.41', '21.24', '1.4']]
v5 = [['1.56', '30.41', '21.24', '1.4']]
v6 = [['1.49', '30.41', '21.24', '1.4']]
v7 = [['1.56', '30.41', '21.24', '1.4']]
v8 = [['1.62', '35.79', '24.59', '2.0']]

(
    #创建雷达图，对雷达图进行设置大小和主题
    Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="#CCCCCC"))
    .add_schema(
        schema=[
            #雷达每个角对应的内容，和范围
            opts.RadarIndicatorItem(name="高度（厘米）", max_=2.0),
            opts.RadarIndicatorItem(name="宽度（厘米）", max_=40.0),
            opts.RadarIndicatorItem(name="深度（厘米）", max_=30.0),
            opts.RadarIndicatorItem(name="重量（千克）", max_=2.0),
        ],
        #雷达图的文字和颜色选择
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        textstyle_opts=opts.TextStyleOpts(color="#fff"),
    )
    #一个add对应一条雷达线
    .add(
        series_name="MacBook Air (M1，2020 年)",
        data=v1,
        linestyle_opts=opts.LineStyleOpts(color="#DA4B1E"),
    )
    .add(
        series_name="MacBook Air (视网膜显示屏，2020 年)",
        data=v2,
        linestyle_opts=opts.LineStyleOpts(color="#D5DA1E"),
    )
    .add(
            series_name="MacBook Air (2017 年)",
            data=v3,
            linestyle_opts=opts.LineStyleOpts(color="#41DA1E"),
        )
    .add(
            series_name="MacBook Pro 13 英寸 (M1，2020 年)",
            data=v4,
            linestyle_opts=opts.LineStyleOpts(color="#158847"),
        )
    .add(
            series_name="MacBook Pro 13 英寸 (两个雷雳 3 端口，2020 年)",
            data=v5,
            linestyle_opts=opts.LineStyleOpts(color="#13DADB"),
        )
    .add(
            series_name="MacBook Pro 13 英寸 (两个雷雳 3 端口，2016 年)",
            data=v6,
            linestyle_opts=opts.LineStyleOpts(color="#1376DB"),
        )
    .add(
            series_name="MacBook Pro 13 英寸 (四个雷雳 3 端口，2020 年)",
            data=v7,
            linestyle_opts=opts.LineStyleOpts(color="#7E13DB"),
        )
    .add(
        series_name="MacBook Pro 16 英寸",
        data=v8,
        linestyle_opts=opts.LineStyleOpts(color="#DB13DB"),
    )
    #设置雷达图的标题的大小和颜色以及位置
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Mac-尺寸与重量",pos_left="55%", pos_top="10%"), legend_opts=opts.LegendOpts()
    )
    .render("Mac-尺寸与重量.html")
)

