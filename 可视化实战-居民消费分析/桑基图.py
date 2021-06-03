from pyecharts import options as opts
from pyecharts.charts import Sankey
from pyecharts.globals import ThemeType

nodes = [
    {"name": "北京"},
    {"name": "上海"},
    {"name": "广东"},
    {"name": "重庆"},
    {"name": "浙江"},
    {"name": "湖南"},
    {"name": "湖北"},
]

links = [
    {"source": "北京", "target": "上海", "value": 102.09},
    {"source": "上海", "target": "广东", "value": 103.27},
    {"source": "广东", "target": "重庆", "value": 102.81},
    {"source": "重庆", "target": "浙江", "value": 102.62},
    {"source": "浙江", "target": "湖南", "value": 102.79},
    {"source": "湖南", "target": "湖北", "value": 103.30},
]
c = (
    Sankey(init_opts=opts.InitOpts(width="1300px", height="600px",theme=ThemeType.PURPLE_PASSION))
    .add(
        "桑基图",
        nodes,
        links,
        linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(position="right"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="热门省份-桑基图"))
    .render("sankey.html")
)

