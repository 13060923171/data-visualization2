import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import init_notebook_mode, iplot, plot
from statsmodels.formula.api import ols
import pandas as pd

df_x = pd.read_excel('图3数据.xlsx',sheet_name='x')
df_y = pd.read_excel('图3数据.xlsx',sheet_name='y')
df_2000 = pd.DataFrame()
list_2000 = []
for x in range(31):
    x = 2000
    list_2000.append(x)
df_2000['year'] = list_2000
df_2000['地区'] = df_x['地区']
df_2000['x'] = df_x[2000]
df_2000['y'] = df_y[2000]

df_2001 = pd.DataFrame()
list_2001 = []
for x in range(31):
    x = 2001
    list_2001.append(x)
df_2001['year'] = list_2001
df_2001['地区'] = df_x['地区']
df_2001['x'] = df_x[2001]
df_2001['y'] = df_y[2001]

df_2002 = pd.DataFrame()
list_2002 = []
for x in range(31):
    x = 2002
    list_2002.append(x)
df_2002['year'] = list_2002
df_2002['地区'] = df_x['地区']
df_2002['x'] = df_x[2002]
df_2002['y'] = df_y[2002]

df_2003 = pd.DataFrame()
list_2003 = []
for x in range(31):
    x = 2003
    list_2003.append(x)
df_2003['year'] = list_2003
df_2003['地区'] = df_x['地区']
df_2003['x'] = df_x[2003]
df_2003['y'] = df_y[2003]

df_2004 = pd.DataFrame()
list_2004 = []
for x in range(31):
    x = 2004
    list_2004.append(x)
df_2004['year'] = list_2004
df_2004['地区'] = df_x['地区']
df_2004['x'] = df_x[2004]
df_2004['y'] = df_y[2004]

df_2005 = pd.DataFrame()
list_2005 = []
for x in range(31):
    x = 2005
    list_2005.append(x)
df_2005['year'] = list_2005
df_2005['地区'] = df_x['地区']
df_2005['x'] = df_x[2005]
df_2005['y'] = df_y[2005]

df_2006 = pd.DataFrame()
list_2006 = []
for x in range(31):
    x = 2006
    list_2006.append(x)
df_2006['year'] = list_2006
df_2006['地区'] = df_x['地区']
df_2006['x'] = df_x[2006]
df_2006['y'] = df_y[2006]

df_2007 = pd.DataFrame()
list_2007 = []
for x in range(31):
    x = 2007
    list_2007.append(x)
df_2007['year'] = list_2007
df_2007['地区'] = df_x['地区']
df_2007['x'] = df_x[2007]
df_2007['y'] = df_y[2007]

df_2008 = pd.DataFrame()
list_2008 = []
for x in range(31):
    x = 2008
    list_2008.append(x)
df_2008['year'] = list_2008
df_2008['地区'] = df_x['地区']
df_2008['x'] = df_x[2008]
df_2008['y'] = df_y[2008]

df_2009 = pd.DataFrame()
list_2009 = []
for x in range(31):
    x = 2009
    list_2009.append(x)
df_2009['year'] = list_2009
df_2009['地区'] = df_x['地区']
df_2009['x'] = df_x[2009]
df_2009['y'] = df_y[2009]

df_2010 = pd.DataFrame()
list_2010 = []
for x in range(31):
    x = 2010
    list_2010.append(x)
df_2010['year'] = list_2010
df_2010['地区'] = df_x['地区']
df_2010['x'] = df_x[2010]
df_2010['y'] = df_y[2010]

df_2011 = pd.DataFrame()
list_2011 = []
for x in range(31):
    x = 2011
    list_2011.append(x)
df_2011['year'] = list_2011
df_2011['地区'] = df_x['地区']
df_2011['x'] = df_x[2011]
df_2011['y'] = df_y[2011]

df_2012 = pd.DataFrame()
list_2012 = []
for x in range(31):
    x = 2012
    list_2012.append(x)
df_2012['year'] = list_2012
df_2012['地区'] = df_x['地区']
df_2012['x'] = df_x[2012]
df_2012['y'] = df_y[2012]

df_2013 = pd.DataFrame()
list_2013 = []
for x in range(31):
    x = 2013
    list_2013.append(x)
df_2013['year'] = list_2013
df_2013['地区'] = df_x['地区']
df_2013['x'] = df_x[2013]

df_2014 = pd.DataFrame()
list_2014 = []
for x in range(31):
    x = 2014
    list_2014.append(x)
df_2014['year'] = list_2014
df_2014['地区'] = df_x['地区']
df_2014['x'] = df_x[2014]
df_2014['y'] = df_y[2014]

df_2015 = pd.DataFrame()
list_2015 = []
for x in range(31):
    x = 2015
    list_2015.append(x)
df_2015['year'] = list_2015
df_2015['地区'] = df_x['地区']
df_2015['x'] = df_x[2015]
df_2015['y'] = df_y[2015]

df_2016 = pd.DataFrame()
list_2016 = []
for x in range(31):
    x = 2016
    list_2016.append(x)
df_2016['year'] = list_2016
df_2016['地区'] = df_x['地区']
df_2016['x'] = df_x[2016]
df_2016['y'] = df_y[2016]

df_2017 = pd.DataFrame()
list_2017 = []
for x in range(31):
    x = 2017
    list_2017.append(x)
df_2017['year'] = list_2017
df_2017['地区'] = df_x['地区']
df_2017['x'] = df_x[2017]
df_2017['y'] = df_y[2017]

df_2018 = pd.DataFrame()
list_2018 = []
for x in range(31):
    x = 2018
    list_2018.append(x)
df_2018['year'] = list_2018
df_2018['地区'] = df_x['地区']
df_2018['x'] = df_x[2018]
df_2018['y'] = df_y[2018]

df_2019 = pd.DataFrame()
list_2019 = []
for x in range(31):
    x = 2019
    list_2019.append(x)
df_2019['year'] = list_2019
df_2019['地区'] = df_x['地区']
df_2019['x'] = df_x[2019]
df_2019['y'] = df_y[2019]

df_all = df_2000.append([df_2001,df_2002,df_2003,df_2004,df_2005,df_2006,df_2007,df_2008,df_2009,df_2010,df_2011,df_2012,df_2013,df_2014,df_2015,df_2016,df_2017,df_2018,df_2019],sort=False)
df_all.columns = ['year','diqu','population(thousands)','GDP（billion)']

fig = px.scatter(df_all,x='population(thousands)',y='GDP（billion)',animation_frame='year',
                 animation_group='diqu',size='population(thousands)',color='diqu',hover_name='diqu',trendline='ols')
fig.update_layout(title_text='the Relationship of GDP and Population')
plot(fig,filename='the Relationship of GDP and Population.html')