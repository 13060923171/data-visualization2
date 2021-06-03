from pyecharts.charts import Page
from bar_gdp import *
from bar_policy import *
from bar_zoom import *
from line_zoom import *
from map_people import *
from pie_zoom import *
from Wordcloud_Hot import *
from Develop_Gauge import *
from Timer_Shaft import *

def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        Bar_gdp(),
        Bar_zoom(),
        Map_people(),
        Pie_zoom(),
        Line_zoom(),
        wordcloud_hot(),
        develop_gauge(),
        timer_shaft()

    )
    page.save_resize_html(cfg_file="chart_config.json")
    # page.render()

if __name__ == '__main__':
    page_draggable_layout()