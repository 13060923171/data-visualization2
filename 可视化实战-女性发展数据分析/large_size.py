from pyecharts.charts import Page
from main1 import *
from main2 import *
from main3 import *
from main4 import *
from main5 import *
from main6 import *
from main7 import *
from main8 import *


def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        main_image(),
        main_bar(),
        main_liquid(),
        main_polar(),
        main_bar5(),
        main_line(),
        main_pie(),
        main_radar(),
    )
    page.save_resize_html(cfg_file="chart_config.json")
    # page.render()

if __name__ == '__main__':
    page_draggable_layout()