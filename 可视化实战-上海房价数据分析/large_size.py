from pyecharts.charts import Page
from main_map import *
from main_geo import *
from main_scatter import *
from main_boxplot import *
from main_image_1 import *
from main_image_2 import *
from main_image_3 import *

def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        main_map(),
        main_geo(),
        main_scatter(),
        main_boxplot(),
        main_image_1(),
        main_image_2(),
        main_image_3()


    )
    page.save_resize_html(cfg_file="chart_config.json")
    # page.render()


if __name__ == '__main__':
    page_draggable_layout()