from pyecharts.charts import Page
from bar_table import *
from china_map import *
from line_table import *
from pie_talbe import *

#生成大屏数据
def page_draggable_layout():
    #选择可以拖拽的类型
    page = Page(layout=Page.DraggablePageLayout)
    #导入函数，传入图表参数
    page.add(
        get_bar(),
        get_line(),
        main_pie(),
        get_city()


    )
    #根据定义好的json文件去固定位置
    page.save_resize_html(cfg_file="chart_config.json")
    #生成最新图表
    # page.render()


if __name__ == '__main__':
    page_draggable_layout()