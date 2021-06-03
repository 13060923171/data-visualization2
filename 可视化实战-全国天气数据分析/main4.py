import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map

df = pd.read_csv('./csv_file/全国空气质量指数排行榜.csv',encoding='gbk').loc[:,['省份','AQI']]
df.dropna(axis=0,how='any',inplace=True)
df[df.isnull().T.any()]

list_city = []
for i in df['省份']:
    list_city.append(i)

list_aqi = []
for j in df['AQI']:
    list_aqi.append(j)


sum_beijing = []
sum_tianjin = []
sum_hebei = []
sum_shanxi = []
sum_liaoning = []
sum_shanghai = []
sum_jiangsu = []
sum_zhejiang = []
sum_anhui = []
sum_fujinag = []
sum_jiangxi = []
sum_shangdong = []
sum_henan = []
sum_hubei = []
sum_hunan = []
sum_guangdong = []
sum_guangxi = []
sum_chongqing = []
sum_sichuan = []
sum_guizhou = []
sum_shaanxi = []
sum_gansu = []
sum_list =[]
sum_yunnan = []
sum_xizan = []
sum_qinghai = []
sum_hainan = []
sum_xingjiang = []
sum_neimengku = []
sum_ningxia = []
sum_jiling = []
sum_heilongjian=[]
for l in range(len(list_city)):
    if '北京' in list_city[l]:
        sum_beijing.append(int(list_aqi[l]))
avg_beijing = sum(sum_beijing)/len(sum_beijing)
sum_list.append(int(avg_beijing))

for l in range(len(list_city)):
    if '天津' in list_city[l]:
        sum_tianjin.append(int(list_aqi[l]))
avg_tianjin = sum(sum_tianjin) / len(sum_tianjin)
sum_list.append(int(avg_tianjin))

for l in range(len(list_city)):
    if '河北' in list_city[l]:
        sum_hebei.append(int(list_aqi[l]))
avg_hebei = sum(sum_hebei) / len(sum_hebei)
sum_list.append(int(avg_hebei))

for l in range(len(list_city)):
    if '山西' in list_city[l]:
        sum_shanxi.append(int(list_aqi[l]))
avg_shanxi = sum(sum_shanxi) / len(sum_shanxi)
sum_list.append(int(avg_shanxi))

for l in range(len(list_city)):
    if '辽宁' in list_city[l]:
        sum_liaoning.append(int(list_aqi[l]))
avg_liaoning = sum(sum_liaoning) / len(sum_liaoning)
sum_list.append(int(avg_liaoning))

for l in range(len(list_city)):
    if '上海' in list_city[l]:
        sum_shanghai.append(int(list_aqi[l]))
avg_shanghai = sum(sum_shanghai) / len(sum_shanghai)
sum_list.append(int(avg_shanghai))

for l in range(len(list_city)):
    if '江苏' in list_city[l]:
        sum_jiangsu.append(int(list_aqi[l]))
avg_jiangsu = sum(sum_jiangsu) / len(sum_jiangsu)
sum_list.append(int(avg_jiangsu))

for l in range(len(list_city)):
    if '浙江' in list_city[l]:
        sum_zhejiang.append(int(list_aqi[l]))
avg_zhejiang = sum(sum_zhejiang) / len(sum_zhejiang)
sum_list.append(int(avg_zhejiang))

for l in range(len(list_city)):
    if '安徽' in list_city[l]:
        sum_anhui.append(int(list_aqi[l]))
avg_anhui = sum(sum_anhui) / len(sum_anhui)
sum_list.append(int(avg_anhui))

for l in range(len(list_city)):
    if '福建' in list_city[l]:
        sum_fujinag.append(int(list_aqi[l]))
avg_fujinag = sum(sum_fujinag) / len(sum_fujinag)
sum_list.append(int(avg_fujinag))

for l in range(len(list_city)):
    if '江西' in list_city[l]:
        sum_jiangxi.append(int(list_aqi[l]))
avg_jiangxi = sum(sum_jiangxi) / len(sum_jiangxi)
sum_list.append(int(avg_jiangxi))

for l in range(len(list_city)):
    if '山东' in list_city[l]:
        sum_shangdong.append(int(list_aqi[l]))
avg_shangdong = sum(sum_shangdong) / len(sum_shangdong)
sum_list.append(int(avg_shangdong))

for l in range(len(list_city)):
    if '河南' in list_city[l]:
        sum_henan.append(int(list_aqi[l]))
avg_henan = sum(sum_henan) / len(sum_henan)
sum_list.append(int(avg_henan))

for l in range(len(list_city)):
    if '湖北' in list_city[l]:
        sum_hubei.append(int(list_aqi[l]))
avg_hubei = sum(sum_hubei) / len(sum_hubei)
sum_list.append(int(avg_hubei))

for l in range(len(list_city)):
    if '湖南' in list_city[l]:
        sum_hunan.append(int(list_aqi[l]))
avg_hunan = sum(sum_hunan) / len(sum_hunan)
sum_list.append(int(avg_hunan))

for l in range(len(list_city)):
    if '广东' in list_city[l]:
        sum_guangdong.append(int(list_aqi[l]))
avg_guangdong = sum(sum_guangdong) / len(sum_guangdong)
sum_list.append(int(avg_guangdong))

for l in range(len(list_city)):
    if '广西' in list_city[l]:
        sum_guangxi.append(int(list_aqi[l]))
avg_guangxi = sum(sum_guangxi) / len(sum_guangxi)
sum_list.append(int(avg_guangxi))

for l in range(len(list_city)):
    if '重庆' in list_city[l]:
        sum_chongqing.append(int(list_aqi[l]))
avg_chongqing = sum(sum_chongqing) / len(sum_chongqing)
sum_list.append(int(avg_chongqing))

for l in range(len(list_city)):
    if '四川' in list_city[l]:
        sum_sichuan.append(int(list_aqi[l]))
avg_sichuan = sum(sum_sichuan) / len(sum_sichuan)
sum_list.append(int(avg_sichuan))

for l in range(len(list_city)):
    if '贵州' in list_city[l]:
        sum_guizhou.append(int(list_aqi[l]))
avg_guizhou = sum(sum_guizhou) / len(sum_guizhou)
sum_list.append(int(avg_guizhou))

for l in range(len(list_city)):
    if '陕西' in list_city[l]:
        sum_shaanxi.append(int(list_aqi[l]))
avg_shaanxi = sum(sum_shaanxi) / len(sum_shaanxi)
sum_list.append(int(avg_shaanxi))

for l in range(len(list_city)):
    if '甘肃' in list_city[l]:
        sum_gansu.append(int(list_aqi[l]))
avg_gansu = sum(sum_gansu) / len(sum_gansu)
sum_list.append(int(avg_gansu))

for l in range(len(list_city)):
    if '西藏' in list_city[l]:
        sum_xizan.append(int(list_aqi[l]))
avg_xizan = sum(sum_xizan) / len(sum_xizan)
sum_list.append(int(avg_xizan))

for l in range(len(list_city)):
    if '云南' in list_city[l]:
        sum_yunnan.append(int(list_aqi[l]))
avg_yunnan = sum(sum_yunnan) / len(sum_yunnan)
sum_list.append(int(avg_yunnan))

for l in range(len(list_city)):
    if '海南' in list_city[l]:
        sum_hainan.append(int(list_aqi[l]))
avg_hainan = sum(sum_hainan) / len(sum_hainan)
sum_list.append(int(avg_hainan))

for l in range(len(list_city)):
    if '青海' in list_city[l]:
        sum_qinghai.append(int(list_aqi[l]))
avg_qinghai = sum(sum_qinghai) / len(sum_qinghai)
sum_list.append(int(avg_qinghai))

for l in range(len(list_city)):
    if '新疆' in list_city[l]:
        sum_xingjiang.append(int(list_aqi[l]))
avg_xingjiang = sum(sum_xingjiang) / len(sum_xingjiang)
sum_list.append(int(avg_xingjiang))

for l in range(len(list_city)):
    if '内蒙古' in list_city[l]:
        sum_neimengku.append(int(list_aqi[l]))
avg_neimengku = sum(sum_neimengku) / len(sum_neimengku)
sum_list.append(int(avg_neimengku))

for l in range(len(list_city)):
    if '吉林' in list_city[l]:
        sum_jiling.append(int(list_aqi[l]))
avg_jiling = sum(sum_jiling) / len(sum_jiling)
sum_list.append(int(avg_jiling))


for l in range(len(list_city)):
    if '黑龙江' in list_city[l]:
        sum_heilongjian.append(int(list_aqi[l]))
avg_heilongjian = sum(sum_heilongjian) / len(sum_heilongjian)
sum_list.append(int(avg_heilongjian))

for l in range(len(list_city)):
    if '宁夏' in list_city[l]:
        sum_ningxia.append(int(list_aqi[l]))
avg_ningxia = sum(sum_ningxia) / len(sum_ningxia)

sum_list.append(int(avg_ningxia))


x_data = ['北京','天津','河北','山西','辽宁','上海','江苏','浙江',
          '安徽','福建','江西','山东','河南','湖北','湖南','广东',
          '广西','重庆','四川','贵州','陕西','甘肃','西藏','云南','海南','青海','新疆','内蒙古','吉林','黑龙江','宁夏']

data_pair = [(i, j) for i, j in zip(x_data,sum_list)]

c = (
    Map()
    .add("", data_pair, "china", is_map_symbol_show=False,)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国空气质量平均值"),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
    .render("map_world.html")
)





