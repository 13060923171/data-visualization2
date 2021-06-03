from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.commons.utils import JsCode

def main_liquid():
    c = (
        Liquid()
        .add("女性",
             [0.3762],
             color="#DB7093",
             background_color="#DB7093",
             label_opts=opts.LabelOpts(
                 font_size=50,
                 formatter=JsCode(
                     """function (param) {
                         return (Math.floor(param.value * 10000) / 100) + '%';
                     }"""
                 ),
                 position="inside",
                    ),
            is_outline_show=False
            )
        .set_global_opts(title_opts=opts.TitleOpts(title="女性媒体从业人员所在比重",pos_left="center",pos_top="top"))
    )
    return c