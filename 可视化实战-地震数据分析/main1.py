import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType

df = pd.read_excel('eqdata.xls').loc[:,['震级','经度','纬度','地点']]
data_pair = [(i, j) for i, j in zip(df['地点'],df['震级'])]


def geo_main():

    geo = (
        Geo()
        .add_schema(
            maptype="world",
            itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),)
        .add_coordinate_json(json_file='city.json')
        .add(
            '震级',
            data_pair,
            type_=ChartType.HEATMAP,
            effect_opts=opts.EffectOpts(symbol_size=0.1)
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(min_=0.0,max_=10.0),
            title_opts=opts.TitleOpts(title="世界地震热力地图"),
        )
    )

    return geo

