from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
x_data = ['否','取决于工作内容','能']
y_woman = [0.48,23.43,76.10]
y_man = [6.01,38.05,55.94]
sum_man = [2.71,29.32,67.98]

def main_bar5():
    c = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis("女人",y_woman,color="#B1F2F5")
        .add_yaxis("男人",y_man,color="#3399FF")
        .add_yaxis("总体",sum_man,color="#FF0066")
        .reversal_axis()
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c}%"
            ),
            label_opts=opts.LabelOpts(is_show=False)
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="女性能否胜任公司中高层"))
    )
    return c