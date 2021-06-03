from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode


x_data = ['普通员工/职员','基层管理人员','中层管理人员','高层管理人员','初级技术人员','中级技术人员','高级技术人员']
y_woman = [46.3,21.2,21.4,5.0,2.6,2.7,0.7]
y_man = [31.0,25.6,22.1,9.0,5.1,5.3,2.0]

def main_bar():
    c = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis("女人", y_woman,color="#3498DB")
        .add_yaxis("男人", y_man,color="#F1948A")
        .set_global_opts(
            title_opts={"text": "男女职场人在各职级占比"}
        )
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c}%"
            ),
            label_opts=opts.LabelOpts(is_show=False)
        )
    )
    return c