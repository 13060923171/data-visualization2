import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

#获取数据
df = pd.read_excel('数据.xls').loc[:,['工作类型']]
list_type = {}
#对数据进行清洗
for c in df['工作类型']:
    c = str(c)
    c = c.split('/')
    for j in c:
        #删除一些无效数据
        j = j.replace('(系统、数据服务、维修)','').replace('(食品、饮料、化妆品)','').replace('(咨询、人力资源、财会)','').replace('、增值服务','')
        #对清洗好的数据进行计算，获取到每个类型的总数
        list_type[j] = list_type.get(j,0) + 1
#对清洗好的数据，进行从小到大的排序
list1 = list(list_type.items())
list1.sort(key=lambda x:x[1],reverse=True)
#选出前10的数据
list1 = list1[0:10]
#生成饼图
def main_pie():
    c = (
        #生成饼图的主题
        Pie(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
            .add(
            "",
            list1,
            #饼图的具体位置
            center=['50%','50%'],
            label_opts=opts.LabelOpts(is_show=True)
        )
            #饼图的颜色范围
            .set_colors(['SteelBlue','DarkCyan','DarkOrange','Salmon'])
        #饼图的标题
            .set_global_opts(title_opts=opts.TitleOpts(title="最热门的前十大职业",pos_left="center",
                                                       pos_top="top",),legend_opts=opts.LegendOpts(is_show=False))
        #饼图显示内容的设置
            .set_series_opts(tooltip_opts=opts.TooltipOpts(trigger='item',formatter="{a} <br/>{b}:{d}%"))
    )
    return c

