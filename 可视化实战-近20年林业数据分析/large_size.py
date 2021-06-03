from pyecharts.charts import Page
from main_map import *
from main_line import *
from main_bar import *
from main_reversal import *


def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        main_bar(),
        main_line(),
        main_reveral(),
        time_map()


    )
    page.save_resize_html(cfg_file="./data/chart_config.json")
    # page.render()


if __name__ == '__main__':
    page_draggable_layout()