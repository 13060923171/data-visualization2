from pyecharts.charts import Page
from main_map import *
from main_word import *
from tree_man import *


def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        time_map(),
        wordcloud_hot(),
        main_tree()

    )
    page.save_resize_html(cfg_file="./data/chart_config.json")
    # page.render()


if __name__ == '__main__':
    page_draggable_layout()