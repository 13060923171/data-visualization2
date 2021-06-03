from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

x_data = ['稍弱','无太大差异','更佳']
y_data = [11.50,49.76,38.74]
data_pair = [list(z) for z in zip(x_data,y_data)]

def main_pie():
    pie = (
                Pie(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
                .add(
                    "",
                    data_pair,
                    rosetype="radius",
                    radius=["30%", "55%"],

                )
                .set_colors(["#F44336", "#E91E63", "#9C27B0 "])
                .set_global_opts(title_opts=opts.TitleOpts("女性与同级别男性自身表现评价的比较",pos_left="center",pos_top="top"),legend_opts=opts.LegendOpts(is_show=False))
                .set_series_opts(
                    tooltip_opts=opts.TooltipOpts(
                        trigger="item", formatter="{b}: {c}%"
                    ),
                )
            )
    return pie