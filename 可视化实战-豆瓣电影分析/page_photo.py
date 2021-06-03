from pyecharts.charts import Page
from main import bar_time,number_bar,type_pie,line_comment,word,map_country
def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        bar_time(),
        number_bar(),
        type_pie(),
        line_comment(),
        word(),
        map_country()

    )
    page.save_resize_html(cfg_file="chart_config.json")
    # page.render()


if __name__ == '__main__':
    page_draggable_layout()
