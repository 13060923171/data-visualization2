import json
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Graph
from pyecharts.charts import Timeline


def main_graph():
    time_list = ['陈桥兵变', '雍熙北伐', '庆历新政', '王安石变法', '靖康之变', '建炎南渡', '绍兴和议', '隆兴北伐', '襄樊之战', '崖山海战']

    tl = Timeline()
    for t in time_list:
        with open("./data/{}.json".format(t), "r", encoding="utf-8") as f:
            j = json.load(f)
            nodes = j["nodes"]
            links = j["links"]
            categories = j["categories"]
        c = (
            Graph(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
            .add(
                "",
                nodes=nodes,
                links=links,
                categories=categories,
                layout="circular",
                is_roam=True,
                is_focusnode=True,
                is_rotate_label=True,
                label_opts=opts.LabelOpts(position="right"),
                linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
            )
            .set_global_opts(
                legend_opts=opts.LegendOpts(is_show=False),
            )
        )
        tl.add(c, "{}".format(t))
        tl.add_schema(
            orient="vertical",
            is_auto_play=True,
            is_inverse=True,
            play_interval=3000,
            pos_left="null",
            pos_right="5",
            pos_top="20",
            pos_bottom="20",
            width="50",
            label_opts=opts.LabelOpts(is_show=True, color="#fff"),
        )
    return tl



