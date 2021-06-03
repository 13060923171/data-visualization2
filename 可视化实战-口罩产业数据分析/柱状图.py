import pandas as pd
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

df = pd.read_excel('口罩产业.xlsx',sheet_name='Sheet4').loc[1:30,['医用口罩产业链下游企业区域分布情况（单位：家）','Unnamed: 1']]
city = []
number = []

for c in df['医用口罩产业链下游企业区域分布情况（单位：家）']:
    city.append(c)

for n in df['Unnamed: 1']:
    n = int(n)
    number.append(n)


c = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(city)
    .add_yaxis("", number)
    .set_global_opts(
        title_opts={"text": "医用口罩产业链下游企业区域分布情况（单位：家）"}
    )
    .render("bar_base_dict_config.html")
)

