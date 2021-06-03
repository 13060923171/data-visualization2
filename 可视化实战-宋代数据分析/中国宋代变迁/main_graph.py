import json
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Graph


with open("./data/陈桥兵变1.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes = j["nodes"]
    links = j["links"]
    categories = j["categories"]

c = (
    Graph(init_opts=opts.InitOpts(width="1000px", height="600px",theme=ThemeType.LIGHT))
    .add(
        "",
        nodes=nodes,
        links=links,
        categories=categories,
        layout="none",
        is_roam=True,
        is_focusnode=True,
        label_opts=opts.LabelOpts(is_show=True),
        linestyle_opts=opts.LineStyleOpts(width=0.5, curve=0.3, opacity=0.7),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Graph-Les Miserables"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
    )
    .render("graph_les_miserables.html")
)

