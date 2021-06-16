import pandas as pd
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Map

df = pd.read_excel('各区房价平均值.xlsx',sheet_name='Sheet2').loc[:,['地区','数值']]

x_data = []
for i in df['地区']:
    i = str(i)
    i = '{}区'.format(i)
    i = i.replace('浦东区','浦东新区').replace('静安+闸北区','静安区')
    x_data.append(i)

def main_map():
    map = (
            Map(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
                .add(
                "",
                [list(z) for z in zip(x_data, df['数值'])],
                "上海",
                label_opts=opts.LabelOpts(is_show=False),
                is_map_symbol_show=True,
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title=""),
                visualmap_opts=opts.VisualMapOpts(
                    is_calculable=True,
                    dimension=0,
                    pos_left="10",
                    pos_top="center",
                    range_text=["High", "Low"],
                    range_color=["lightskyblue", "yellow", "orangered"],
                    textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                    min_=0,
                    max_=200000,
                    is_show=True
                )
            )
    )
    return map
