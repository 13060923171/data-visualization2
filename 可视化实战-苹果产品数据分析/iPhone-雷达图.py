import pyecharts.options as opts
from pyecharts.charts import Radar
from pyecharts.globals import ThemeType

#这个是从表格中读取到的数据，进行雷达的数据集
v1 = [['160.8', '78.1', '7.4', '226']]
v2 = [['146.7', '71.5', '7.4', '187']]
v3 = [['146.7', '71.5', '7.4', '162']]
v4 = [['131.5', '64.2', '7.4', '133']]
v5 = [['158.0', '77.8', '8.1', '226']]
v6 = [['144.0', '71.4', '8.1', '188']]
v7 = [['150.9', '75.7', '8.3', '194']]
v8 = [['138.4', '67.3', '7.3', '148']]
v9 = [['157.5', '77.4', '7.7', '208']]
v10 = [['143.6', '70.9', '7.7','177']]
v11 = [['150.9', '75.7', '8.3','194']]
v12 = [['143.6', '70.9', '7.7','174']]
v13 = [['158.4', '78.1', '7.5','202']]
v14 = [['138.4', '67.3', '7.3','148']]
v15 = [['158.2', '77.9', '7.3','188']]
v16 = [['138.3', '67.1', '7.1','138']]
v17 = [['158.2', '77.9', '7.3','192']]
v18 = [['138.3', '67.1', '7.1','143']]
v19 = [['158.1', '77.8', '7.1','172']]
v20 = [['138.1', '67.0', '6.9','129']]
v21 = [['123.8', '58.6', '7.6','113']]


(
    #创建雷达图表，设置雷达的大小和主题
    Radar(init_opts=opts.InitOpts(width="1280px", height="620px", theme=ThemeType.ROMANTIC))
    .add_schema(
        #雷达每个角的大小和对应的内容
        schema=[
            opts.RadarIndicatorItem(name="高度（毫米）", max_=170.0),
            opts.RadarIndicatorItem(name="宽度（毫米）", max_=80.0),
            opts.RadarIndicatorItem(name="深度（毫米）", max_=10.0),
            opts.RadarIndicatorItem(name="重量（克）", max_=250),
        ],
        #雷达的形状
        shape="circle",
        #雷达的文字大小和颜色
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        textstyle_opts=opts.TextStyleOpts(color="#665706"),
    )
    #雷达的线
    .add(
        series_name="iPhone 12 Pro Max",
        data=v1,
        linestyle_opts=opts.LineStyleOpts(color="#DA4B1E"),
    )
    .add(
        series_name="iPhone 12 Pro",
        data=v2,
        linestyle_opts=opts.LineStyleOpts(color="#D5DA1E"),
    )
    .add(
            series_name="iPhone 12",
            data=v3,
            linestyle_opts=opts.LineStyleOpts(color="#41DA1E"),
        )
    .add(
            series_name="iPhone 12 mini",
            data=v4,
            linestyle_opts=opts.LineStyleOpts(color="#158847"),
        )
    .add(
            series_name="iPhone 11 Pro Max",
            data=v5,
            linestyle_opts=opts.LineStyleOpts(color="#13DADB"),
        )
    .add(
            series_name="iPhone 11 Pro",
            data=v6,
            linestyle_opts=opts.LineStyleOpts(color="#1376DB"),
        )
    .add(
            series_name="iPhone 11",
            data=v7,
            linestyle_opts=opts.LineStyleOpts(color="#7E13DB"),
        )
    .add(
        series_name="iPhone SE(第二代)",
        data=v8,
        linestyle_opts=opts.LineStyleOpts(color="#DB13DB"),
    )
.add(
        series_name="iPhone XS Max",
        data=v9,
        linestyle_opts=opts.LineStyleOpts(color="#DB133B"),
    )
    .add(
        series_name="iPhone XS",
        data=v10,
        linestyle_opts=opts.LineStyleOpts(color="#4D111D"),
    )
    .add(
            series_name="iPhone XR",
            data=v11,
            linestyle_opts=opts.LineStyleOpts(color="#221316"),
        )
    .add(
            series_name="iPhone X",
            data=v12,
            linestyle_opts=opts.LineStyleOpts(color="#C2ABAE"),
        )
    .add(
            series_name="iPhone 8 Plus",
            data=v13,
            linestyle_opts=opts.LineStyleOpts(color="#6C6D5B"),
        )
    .add(
            series_name="iPhone 8",
            data=v14,
            linestyle_opts=opts.LineStyleOpts(color="#4C271C"),
        )
    .add(
            series_name="iPhone 7 Plus",
            data=v15,
            linestyle_opts=opts.LineStyleOpts(color="#464C1C"),
        )
    .add(
        series_name="iPhone 7",
        data=v16,
        linestyle_opts=opts.LineStyleOpts(color="#1C2D4C"),
    )
.add(
        series_name="iPhone 6s Plus",
        data=v17,
        linestyle_opts=opts.LineStyleOpts(color="#5F6673"),
    )
    .add(
        series_name="iPhone 6s",
        data=v18,
        linestyle_opts=opts.LineStyleOpts(color="#25145C"),
    )
    .add(
            series_name="iPhone 6 Plus",
            data=v19,
            linestyle_opts=opts.LineStyleOpts(color="#574C7B"),
        )
    .add(
            series_name="iPhone 6",
            data=v20,
            linestyle_opts=opts.LineStyleOpts(color="#7B4C77"),
        )
    .add(
            series_name="iPhone SE(第一代)",
            data=v21,
            linestyle_opts=opts.LineStyleOpts(color="#4C7B5D"),
        )
    #雷达的标题
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    #雷达标题的位置
    .set_global_opts(
        title_opts=opts.TitleOpts(title="iPhone-尺寸与重量",pos_left="55%", pos_top="10%"), legend_opts=opts.LegendOpts()
    )
    .render("iPhone-尺寸与重量.html")
)

