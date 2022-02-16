from pyecharts.charts import Page
from bayes_classification import get_pie
from time_emotion import get_line1
from time_trend import get_bar,get_line
from data_treating import get_word


def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        get_pie(),
        get_line1(),
        get_bar(),
        get_line(),
        get_word(),

    )
    page.save_resize_html(cfg_file="chart_config.json")
    # page.render()


if __name__ == '__main__':
    page_draggable_layout()