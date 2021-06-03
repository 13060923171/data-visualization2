import pyecharts.options as opts
from pyecharts.charts import Bar, Line, Grid
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
import pandas as pd

df = pd.read_excel('中小学吸烟报告(数据来源：湖南学校数据).xls',sheet_name='吸烟的原因').loc[2:4,['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 6']]

x_data = ['尝试','时髦','享受','消遣','解除烦恼和压力','提神','社交']

y1_data = [21,16,6,12,36,3,5]



# 折线图对象
bar = Bar(opts.InitOpts(bg_color="#323a5e"))
# 设置图形的全局参数
(
    bar.set_global_opts(
        legend_opts=opts.LegendOpts(
            pos_top=12,
            pos_right=10,
            textstyle_opts=opts.TextStyleOpts(
                color='#fff'
            )
        ),
        title_opts=opts.TitleOpts(
            title="中学生吸烟的原因",
            subtitle="计算单位:(%)",
            title_textstyle_opts=opts.TextStyleOpts(
                color="#90979c",
                font_size="16"
            )
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis",
            axis_pointer_type="shadow",
            textstyle_opts=opts.TextStyleOpts(
                color="#fff"
            )
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color="white"
                )
            ),
            axislabel_opts=opts.LabelOpts(
            )
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            max_=100,
            axistick_opts=opts.AxisTickOpts(
                is_show=False
            ),
            splitline_opts=opts.SplitLineOpts(
                is_show=True,
                linestyle_opts=opts.LineStyleOpts(
                    color='rgba(255,255,255,0.3)'
                ),
            ),
            axisline_opts=opts.AxisLineOpts(
                is_show=False,
                linestyle_opts=opts.LineStyleOpts(
                    color="white"
                )
            ),
            axislabel_opts=opts.LabelOpts()
        ),
        # datazoom_opts=opts.DataZoomOpts(
        #     is_show=True,
        #     pos_bottom='2%',
        #     pos_top='94%'
        # )
    )
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y1_data,
        label_opts=opts.LabelOpts(
            is_show=False
        ),
        bar_width='15%',
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#fccb05'
                }, {
                    offset: 1,
                    color: '#f5804d'
                }])"""
                ),
                "barBorderRadius": 11,
            }
        }
    )
    ).render("gradient_bar.html")