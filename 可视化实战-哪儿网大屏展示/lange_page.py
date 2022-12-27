
from pyecharts.charts import Page
from bar import *
from funnel import *
from line import *
from word import *
from pie import *
from barh import *
from scatter import *

def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        main_bar(),
        main_line(),
        main_word(),
        main_funnel(),
        main_pie(),
        main_barh(),
        main_scatter(),



    )
    page.save_resize_html(cfg_file="chart_config.json")
    # page.render()


if __name__ == '__main__':
    page_draggable_layout()