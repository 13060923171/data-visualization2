# 数据整理
import numpy as np
import pandas as pd

# 可视化
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import init_notebook_mode, iplot, plot
from statsmodels.formula.api import ols


# init_notebook_mode(connected=True)
# plt.style.use('seaborn')
#导入csv文件
df_2015 = pd.read_csv('./data/2015.csv')
df_2016 = pd.read_csv('./data/2016.csv')
df_2017 = pd.read_csv('./data/2017.csv')
df_2018 = pd.read_csv('./data/2018.csv')
df_2019 = pd.read_csv('./data/2019.csv')
#并且添加多一列名为year
df_2015['year'] = str(2015)
df_2016['year'] = str(2016)
df_2017['year'] = str(2017)
df_2018['year'] = str(2018)
df_2019['year'] = str(2019)
#将所有CSV合并，不用按照从大到小
df_all = df_2015.append([df_2016,df_2017,df_2018,df_2019],sort=False)
df_all.drop('Unnamed: 0',axis=1,inplace=True)
df_all.head()
print(df_2015.shape,df_2016.shape,df_2017.shape,df_2018.shape,df_2019.shape)
df_all.info()
sel_cols = ['happiness','gdp_per_capita','healthy_life_expectancy','freedom_to_life_choise','corruption_perceptions','generosity']
#重置索引
df_model =df_all[sel_cols]
df_model.index = range(df_model.shape[0])
#删除空值
df_model = df_model.dropna()
df_model.head()
lm_m = ols(formula='happiness ~ gdp_per_capita + healthy_life_expectancy + freedom_to_life_choise + corruption_perceptions + generosity',
           data=df_model).fit()
lm_m.summary()

#生成全球地图
data = dict(type='choropleth',locations=df_2019['region'],locationmode='country names',
            colorscale='RdYlGn',z=df_2019['happiness'],text=df_2019['region'],colorbar={'title':'Happiness'})
layout = dict(title='Geographical Visualization of Happiness Score in 2019',
              geo=dict(showframe=True,projection={'type':'azimuthal equal area'}))
choromap3 = go.Figure(data = [data],layout = layout)
plot(choromap3,filename='./html/世界幸福地图.html')

#合并数据
rank_top10 = df_2019.head(10)[['rank','region','happiness']]
last_top10 = df_2019.tail(10)[['rank','region','happiness']]
rank_concat = pd.concat([rank_top10,last_top10])

#条形图
fig = px.bar(rank_concat,
             x="region",
             y="happiness",
             color="region",
             title="World's happiest and least happy countries in 2019")
plot(fig,filename='./html/2019世界幸福国家排行Top10和Last10.html')

# 散点图
fig = px.scatter(df_all, x='gdp_per_capita',
                 y='happiness',
                 facet_row='year',
                 color='year',
                 trendline='ols'
                )
fig.update_layout(height=800, title_text='GDP per capita and Happiness Score')
plot(fig, filename='./html/GDP和幸福得分.html')

# 散点图
fig = px.scatter(df_all, x='healthy_life_expectancy',
                 y='happiness',
                 facet_row='year',
                 color='year',
                 trendline='ols'
                )
fig.update_layout(height=800, title_text='Healthy Life Expecancy and Happiness Score')
plot(fig, filename='./html/健康预期寿命和幸福得分.html')

#动态图
fig = px.scatter(df_all,x='gdp_per_capita',y='happiness',animation_frame='year',
                 animation_group='region',size='rank',color='region',hover_name='region',trendline='ols')
fig.update_layout(title_text='Happiness Rank vs GDP per Capita')
plot(fig,filename='./html/GDP和幸福水平动态图展示.html')

