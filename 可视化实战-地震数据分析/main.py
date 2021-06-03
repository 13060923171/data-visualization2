from pyecharts.charts import Page
from main1 import geo_main
from main2 import table
from main3 import bar_timeline

def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        geo_main(),
        table(),
        bar_timeline(),
    )
    page.save_resize_html(cfg_file="chart_config.json")
    # page.render()

if __name__ == '__main__':
    page_draggable_layout()