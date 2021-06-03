import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Timeline, Bar
from pyecharts.globals import ThemeType
df = pd.read_excel('图1 数据.xls',sheet_name='Sheet1')
total_data = {}
name_list = []
list_2000 = []
list_2001 = []
list_2002 = []
list_2003 = []
list_2004 = []
list_2005 = []
list_2006 = []
list_2007 = []
list_2008 = []
list_2009 = []
list_2010 = []
list_2011 = []
list_2012 = []
list_2013 = []
list_2014 = []
list_2015 = []
list_2016 = []
list_2017 = []
list_2018 = []
list_2019 = []
for i in df['地区']:
    name_list.append(i)
for i in df['2000年']:
    list_2000.append(i)
for i in df['2001年']:
    list_2001.append(i)
for i in df['2002年']:
    list_2002.append(i)
for i in df['2003年']:
    list_2003.append(i)
for i in df['2004年']:
    list_2004.append(i)
for i in df['2005年']:
    list_2005.append(i)
for i in df['2006年']:
    list_2006.append(i)
for i in df['2007年']:
    list_2007.append(i)
for i in df['2008年']:
    list_2008.append(i)
for i in df['2009年']:
    list_2009.append(i)
for i in df['2010年']:
    list_2010.append(i)
for i in df['2011年']:
    list_2011.append(i)
for i in df['2012年']:
    list_2012.append(i)
for i in df['2013年']:
    list_2013.append(i)
for i in df['2014年']:
    list_2014.append(i)
for i in df['2015年']:
    list_2015.append(i)
for i in df['2016年']:
    list_2016.append(i)
for i in df['2017年']:
    list_2017.append(i)
for i in df['2018年']:
    list_2018.append(i)
for i in df['2019年']:
    list_2019.append(i)
data_gdp = {
    2000:list_2000,
    2001:list_2001,
    2002:list_2002,
    2003:list_2003,
    2004:list_2004,
    2005:list_2005,
    2006:list_2006,
    2007:list_2007,
    2008:list_2008,
    2009:list_2009,
    2010:list_2010,
    2011:list_2011,
    2012:list_2012,
    2013:list_2013,
    2014:list_2014,
    2015:list_2015,
    2016:list_2016,
    2017:list_2017,
    2018:list_2018,
    2019:list_2019,
}
def format_data(data: dict) -> dict:
    for year in range(2000, 2020):
        max_data, sum_data = 0, 0
        temp = data[year]
        max_data = max(temp)
        for i in range(len(temp)):
            sum_data += temp[i]
            data[year][i] = {"name": name_list[i], "value": temp[i]}
        data[str(year) + "max"] = int(max_data / 100) * 100
        data[str(year) + "sum"] = sum_data
    return data
# GDP
total_data["dataGDP"] = format_data(data=data_gdp)

#2000-2019年的数据
def get_year_overlap_chart(year: int) -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
        .add_xaxis(xaxis_data=name_list)
        .add_yaxis(
            series_name='GDP',
            y_axis=total_data["dataGDP"][year],
            # is_selected=False,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="GDP of provinces in {}".format(year),subtitle='Data Sources: State Statistical Bureau'
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True,trigger='axis',axis_pointer_type='shadow'),
        )
    )

    return bar

#生成时间轴的图
timeline = Timeline(init_opts=opts.InitOpts(width='1200px',height='600px'))
for y in range(2000,2020):
    timeline.add(get_year_overlap_chart(year=y),time_point=str(y))
timeline.add_schema(is_auto_play=True,play_interval=1000)
timeline.render('finance_indices.html')