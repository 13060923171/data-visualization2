import json
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Tree
from pyecharts.charts import Timeline

name = ['陈桥兵变', '雍熙北伐', '庆历新政', '王安石变法', '靖康之变', '苗刘兵变', '绍兴和议', '隆兴和议', '襄阳之战', '崖山海战']


def main_tree():
    tl = Timeline(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
    for i in range(10):
        with open("./data/{}.json".format(name[i]), "r", encoding="utf-8") as f:
            j = json.load(f)
        c = (
            Tree()
            .add("", [j], collapse_interval=0, layout="radial", symbol_size=7,is_expand_and_collapse=False,initial_tree_depth=2)

        )
        tl.add(c, "{}".format(name[i]))
        tl.add_schema(
            # 播放速度
            play_interval=3000,
            # 是否显示timeline组件
            is_timeline_show=True,
            # 是否自动播放
            is_auto_play=True,
        )
    return tl

