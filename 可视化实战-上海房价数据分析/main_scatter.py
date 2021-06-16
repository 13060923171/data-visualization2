import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Scatter
from pyecharts.globals import ThemeType


df = pd.read_excel('各区房价平均值.xlsx',sheet_name='Sheet3').loc[:,['面积','价格（W）']]

x_data = []
y_data = []

for x in df['面积']:
    x = float(x)
    x_data.append(x)

for y in df['价格（W）']:
    y = float(y)
    y_data.append(y)

def main_scatter():
    scatter = (
            Scatter(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
                .add_xaxis(xaxis_data=x_data)
                .add_yaxis(
                series_name="",
                y_axis=y_data,
                symbol_size=20,
                label_opts=opts.LabelOpts(is_show=False),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="各小区面积与价格之比"),
                xaxis_opts=opts.AxisOpts(
                    type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    axistick_opts=opts.AxisTickOpts(is_show=True),
                    splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
                tooltip_opts=opts.TooltipOpts(is_show=True),
                visualmap_opts=opts.VisualMapOpts(
                    type_="color", max_=2000, min_=0, dimension=1
            ),
            )
        )
    return scatter


