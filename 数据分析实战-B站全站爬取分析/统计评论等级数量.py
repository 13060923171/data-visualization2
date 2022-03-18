import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType
import os



def sum_data(name1):
    df = pd.read_csv('./newdata/{}'.format(name1))
    level = list(df['评论人等级'])
    return level

def main():
    sum_level = []
    files = os.listdir(r'newdata/')
    for f in files:
        level1 = sum_data(f)
        sum_level.append(level1)

    return sum_level


sum_level1 = main()
counts = {}
for s in sum_level1:
    for word in s:
        counts[word] = counts.get(word,0) + 1
counts[1] = counts.pop(0)
ls = list(counts.items())
ls.sort(key=lambda x:x[0],reverse=True)

x_data = [str(i[0]) for i in ls]
y_data = [int(i[1]) for i in ls]

c = (
    Pie(init_opts=opts.InitOpts(width="1600px", height="800px",theme=ThemeType.DARK))
    .add(
        "",
        [list(z) for z in zip(x_data, y_data)],
        radius=["40%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="等级分布图"))
    .render("./HTML文件储存/等级分布图.html")
)

