import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType

#获取数据
df = pd.read_excel('数据.xls').loc[:,['薪水','岗位名称']]
list_name = []
for n in df['岗位名称']:
    list_name.append(n)
#对数据清洗，求每一个的平均薪资
list_salary = []
for s in df['薪水']:
    s = str(s)
    if '万/月' in s:
        s = s.split('-')
        avg = float(float(s[0]) + float(s[1].replace('万/月',''))) / 2
        avg1 = round(float(avg) * 10000)
        list_salary.append(avg1)
    elif '千/月' in s:
        s = s.split('-')
        avg = float(float(s[0]) + float(s[1].replace('千/月',''))) / 2
        avg1 = round(float(avg) * 1000)
        list_salary.append(avg1)
        # 不符合规范的数据清零去除，使得整体数据干净
    else:
        s = 0
        list_salary.append(s)

list_iOS = []
list_android = []
list_web = []
list_python = []
list_java = []
list_php = []
list_network = []
list_analyst = []
list_database = []
list_cpp = []
#求包含工程师关键词的进行薪资提取，从而获取到每个工程师对应的平均薪资
for i in range(len(list_name)):
    if 'iOS' in list_name[i] or 'ios' in list_name[i]:
        list_iOS.append(list_salary[i])
    elif 'Android' in list_name[i] or 'android' in list_name[i]:
        list_android.append(list_salary[i])
    elif 'web' in list_name[i] or 'Web' in list_name[i] or '前端' in list_name[i]:
        list_web.append(list_salary[i])
    elif 'python' in list_name[i] or 'Python' in list_name[i] or 'PYTHON' in list_name[i]:
        list_python.append(list_salary[i])
    elif 'java' in list_name[i] or 'JAVA' in list_name[i] or 'Java' in list_name[i]:
        list_java.append(list_salary[i])
    elif 'php' in list_name[i] or 'PHP' in list_name[i]:
        list_php.append(list_salary[i])
    elif '网络' in list_name[i]:
        list_network.append(list_salary[i])
    elif '数据分析' in list_name[i] or '分析' in list_name[i] or '分析师' in list_name[i]:
        list_analyst.append(list_salary[i])
    elif '数据库' in list_name[i]:
        list_database.append(list_salary[i])
    elif 'c++' in list_name[i] or 'C++' in list_name[i] or 'C' in list_name[i] or 'C#' in list_name[i]:
        list_cpp.append(list_salary[i])

list_x = ['ios工程师','android工程师','web工程师','python工程师','Java工程师','PHP工程师','网络工程师','数据分析师','数据库工程师','C++工程师']
list_y = []
#对平均薪资进行总的添加再除，求得每个工程师总的平均薪资
sum_avg1 = int(sum(list_iOS) / len(list_iOS))
list_y.append(sum_avg1)
sum_avg2 = int(sum(list_android) / len(list_android))
list_y.append(sum_avg2)
sum_avg3 = int(sum(list_web) / len(list_web))
list_y.append(sum_avg3)
sum_avg4 = int(sum(list_python) / len(list_python))
list_y.append(sum_avg4)
sum_avg5 = int(sum(list_java) / len(list_java))
list_y.append(sum_avg5)
sum_avg6 = int(sum(list_php) / len(list_php))
list_y.append(sum_avg6)
sum_avg7 = int(sum(list_network) / len(list_network))
list_y.append(sum_avg7)
sum_avg8 = int(sum(list_analyst) / len(list_analyst))
list_y.append(sum_avg8)
sum_avg9 = int(sum(list_database) / len(list_database))
list_y.append(sum_avg9)
sum_avg10 = int(sum(list_cpp) / len(list_cpp))
list_y.append(sum_avg10)

#根据清洗好的数据生成折线图
def get_line():
    c = (
        #定义折线图的主题
        Line(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
        #折线图的X轴
            .add_xaxis(xaxis_data=list_x)
        #折线图的Y轴
            .add_yaxis(
            series_name="",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#ADFF2F",
            y_axis=list_y,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
        #折线图的标题
            .set_global_opts(
            title_opts=opts.TitleOpts(title="工程师的平均薪资"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,axisline_opts=opts.AxisLineOpts(
                is_on_zero=False,
                #对X轴进行角度旋转，使得全部显示出来
            ),axislabel_opts=opts.LabelOpts(rotate=30)),
        )
    )
    return c
