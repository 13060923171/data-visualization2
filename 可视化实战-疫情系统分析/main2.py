import openpyxl
import pandas as pd
from pyecharts.charts import Map
import pyecharts.options as opts

"""def alter_china_orther():
#将各国的中文名称转换成英文名称，使用pandas中的merge方法
#pd.merge( left, right, how=‘inner’, on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=(’_x’, ‘_y’), copy=True, indicator=False, validate=None,)
#how: One of ‘left’, ‘right’, ‘outer’, ‘inner’. 默认inner。inner是取交集，outer取并集
    word_data = pd.read_excel('国外疫情.xlsx')  # 获取国外疫情数据表
    world_name = pd.read_excel("国家中英文对照.xlsx")
    world_data_t = pd.merge(word_data,
                            world_name,
                            left_on="country",
                            right_on="中文",
                            how="inner")
    return world_data_t"""

def oversea_view():
    """国外疫情可视化"""
    #world_data_t = alter_china_orther()
    wb = openpyxl.load_workbook('demo/data/国外疫情.xlsx')  # 获取已有的xlsx文件
    ws_data = wb['Sheet1']  # 获取文件中中国省份疫情数据表
    ws_data.delete_rows(1)  # 删除第一行
    country = []  # 省份
    now_curconfirm = []  # 现确诊
    # 获取表数据
    for data in ws_data.values:
        country.append(data[0])
        now_curconfirm.append(data[1])
    # 国家名称中英文映射表
    name_map = {
        "Somalia": "索马里",
        "Liechtenstein": "列支敦士登",
        "Morocco": "摩洛哥",
        "W. Sahara": "西撒哈拉",
        "Serbia": "塞尔维亚",
        "Afghanistan": "阿富汗",
        "Angola": "安哥拉",
        "Albania": "阿尔巴尼亚",
        "Andorra": "安道尔共和国",
        "United Arab Emirates": "阿拉伯联合酋长国",
        "Argentina": "阿根廷",
        "Armenia": "亚美尼亚",
        "Australia": "澳大利亚",
        "Austria": "奥地利",
        "Azerbaijan": "阿塞拜疆",
        "Burundi": "布隆迪",
        "Belgium": "比利时",
        "Benin": "贝宁",
        "Burkina Faso": "布基纳法索",
        "Bangladesh": "孟加拉国",
        "Bulgaria": "保加利亚",
        "Bahrain": "巴林",
        "Bahamas": "巴哈马",
        "Bosnia and Herz.": "波斯尼亚和黑塞哥维那",
        "Belarus": "白俄罗斯",
        "Belize": "伯利兹",
        "Bermuda": "百慕大",
        "Bolivia": "玻利维亚",
        "Brazil": "巴西",
        "Barbados": "巴巴多斯",
        "Brunei": "文莱",
        "Bhutan": "不丹",
        "Botswana": "博茨瓦纳",
        "Central African Rep.": "中非共和国",
        "Canada": "加拿大",
        "Switzerland": "瑞士",
        "Chile": "智利",
        "China": "中国",
        "Côte d'Ivoire": "科特迪瓦",
        "Cameroon": "喀麦隆",
        "Dem. Rep. Congo": "刚果（布）",
        "Congo": "刚果（金）",
        "Colombia": "哥伦比亚",
        "Cape Verde": "佛得角",
        "Costa Rica": "哥斯达黎加",
        "Cuba": "古巴",
        "N. Cyprus": "北塞浦路斯",
        "Cyprus": "塞浦路斯",
        "Czech Rep.": "捷克",
        "Germany": "德国",
        "Djibouti": "吉布提",
        "Denmark": "丹麦",
        "Dominican Rep.": "多米尼加",
        "Algeria": "阿尔及利亚",
        "Ecuador": "厄瓜多尔",
        "Egypt": "埃及",
        "Eritrea": "厄立特里亚",
        "Spain": "西班牙",
        "Estonia": "爱沙尼亚",
        "Ethiopia": "埃塞俄比亚",
        "Finland": "芬兰",
        "Fiji": "斐济",
        "France": "法国",
        "Gabon": "加蓬",
        "United Kingdom": "英国",
        "Georgia": "格鲁吉亚",
        "Ghana": "加纳",
        "Guinea": "几内亚",
        "Gambia": "冈比亚",
        "Guinea-Bissau": "几内亚比绍",
        "Eq. Guinea": "赤道几内亚",
        "Greece": "希腊",
        "Grenada": "格林纳达",
        "Greenland": "格陵兰岛",
        "Guatemala": "危地马拉",
        "Guam": "关岛",
        "Guyana": "圭亚那合作共和国",
        "Honduras": "洪都拉斯",
        "Croatia": "克罗地亚",
        "Haiti": "海地",
        "Hungary": "匈牙利",
        "Indonesia": "印度尼西亚",
        "India": "印度",
        "Br. Indian Ocean Ter.": "英属印度洋领土",
        "Ireland": "爱尔兰",
        "Iran": "伊朗",
        "Iraq": "伊拉克",
        "Iceland": "冰岛",
        "Israel": "以色列",
        "Italy": "意大利",
        "Jamaica": "牙买加",
        "Jordan": "约旦",
        "Japan": "日本本土",
        "Siachen Glacier": "锡亚琴冰川",
        "Kazakhstan": "哈萨克斯坦",
        "Kenya": "肯尼亚",
        "Kyrgyzstan": "吉尔吉斯斯坦",
        "Cambodia": "柬埔寨",
        "Korea": "韩国",
        "Kuwait": "科威特",
        "Lao PDR": "老挝",
        "Lebanon": "黎巴嫩",
        "Liberia": "利比里亚",
        "Libya": "利比亚",
        "Sri Lanka": "斯里兰卡",
        "Lesotho": "莱索托",
        "Lithuania": "立陶宛",
        "Luxembourg": "卢森堡",
        "Latvia": "拉脱维亚",
        "Moldova": "摩尔多瓦",
        "Madagascar": "马达加斯加",
        "Mexico": "墨西哥",
        "Macedonia": "马其顿",
        "Mali": "马里",
        "Malta": "马耳他",
        "Myanmar": "缅甸",
        "Montenegro": "黑山",
        "Mongolia": "蒙古国",
        "Mozambique": "莫桑比克",
        "Mauritania": "毛里塔尼亚",
        "Mauritius": "毛里求斯",
        "Malawi": "马拉维",
        "Malaysia": "马来西亚",
        "Namibia": "纳米比亚",
        "New Caledonia": "新喀里多尼亚",
        "Niger": "尼日尔",
        "Nigeria": "尼日利亚",
        "Nicaragua": "尼加拉瓜",
        "Netherlands": "荷兰",
        "Norway": "挪威",
        "Nepal": "尼泊尔",
        "New Zealand": "新西兰",
        "Oman": "阿曼",
        "Pakistan": "巴基斯坦",
        "Panama": "巴拿马",
        "Peru": "秘鲁",
        "Philippines": "菲律宾",
        "Papua New Guinea": "巴布亚新几内亚",
        "Poland": "波兰",
        "Puerto Rico": "波多黎各",
        "Dem. Rep. Korea": "朝鲜",
        "Portugal": "葡萄牙",
        "Paraguay": "巴拉圭",
        "Palestine": "巴勒斯坦",
        "Qatar": "卡塔尔",
        "Romania": "罗马尼亚",
        "Russia": "俄罗斯",
        "Rwanda": "卢旺达",
        "Saudi Arabia": "沙特阿拉伯",
        "Sudan": "苏丹",
        "S. Sudan": "南苏丹",
        "Senegal": "塞内加尔",
        "Singapore": "新加坡",
        "Solomon Is.": "所罗门群岛",
        "Sierra Leone": "塞拉利昂",
        "El Salvador": "萨尔瓦多",
        "Suriname": "苏里南",
        "Slovakia": "斯洛伐克",
        "Slovenia": "斯洛文尼亚",
        "Sweden": "瑞典",
        "Swaziland": "斯威士兰",
        "Seychelles": "塞舌尔",
        "Syria": "叙利亚",
        "Chad": "乍得",
        "Togo": "多哥",
        "Thailand": "泰国",
        "Tajikistan": "塔吉克斯坦",
        "Turkmenistan": "土库曼斯坦",
        "Timor-Leste": "东帝汶",
        "Tonga": "汤加",
        "Trinidad and Tobago": "特立尼达和多巴哥",
        "Tunisia": "突尼斯",
        "Turkey": "土耳其",
        "Tanzania": "坦桑尼亚",
        "Uganda": "乌干达",
        "Ukraine": "乌克兰",
        "Uruguay": "乌拉圭",
        "United States": "美国",
        "Uzbekistan": "乌兹别克斯坦",
        "Venezuela": "委内瑞拉",
        "Vietnam": "越南",
        "Vanuatu": "瓦努阿图",
        "Yemen": "也门",
        "South Africa": "南非",
        "Zambia": "赞比亚",
        "Zimbabwe": "津巴布韦",
        "Aland": "奥兰群岛",
        "American Samoa": "美属萨摩亚",
        "Fr. S. Antarctic Lands": "南极洲",
        "Antigua and Barb.": "安提瓜和巴布达",
        "Comoros": "科摩罗",
        "Curaçao": "库拉索岛",
        "Cayman Is.": "开曼群岛",
        "Dominica": "多米尼加",
        "Falkland Is.": "福克兰群岛马尔维纳斯",
        "Faeroe Is.": "法罗群岛",
        "Micronesia": "密克罗尼西亚",
        "Heard I. and McDonald Is.": "赫德岛和麦克唐纳群岛",
        "Isle of Man": "曼岛",
        "Jersey": "泽西岛",
        "Kiribati": "基里巴斯",
        "Saint Lucia": "圣卢西亚",
        "N. Mariana Is.": "北马里亚纳群岛",
        "Montserrat": "蒙特塞拉特",
        "Niue": "纽埃",
        "Palau": "帕劳",
        "Fr. Polynesia": "法属波利尼西亚",
        "S. Geo. and S. Sandw. Is.": "南乔治亚岛和南桑威奇群岛",
        "Saint Helena": "圣赫勒拿",
        "St. Pierre and Miquelon": "圣皮埃尔和密克隆群岛",
        "São Tomé and Principe": "圣多美和普林西比",
        "Turks and Caicos Is.": "特克斯和凯科斯群岛",
        "St. Vin. and Gren.": "圣文森特和格林纳丁斯",
        "U.S. Virgin Is.": "美属维尔京群岛",
        "Samoa": "萨摩亚"
    }
    # 绘制地图
    m2 = Map()
    m2.add("各国现存确诊人数：", [
        list(z)
        for z in zip(country,now_curconfirm )
    ],
           maptype="world",
           name_map=name_map,
           is_map_symbol_show=False)
    m2.set_global_opts(title_opts=opts.TitleOpts(title="COVID-19世界各国现有确诊人数地图"),
                       visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                         pieces=[{
                                                             "min": 5000,
                                                             "label": '>5000',
                                                             "color": "#893448"
                                                         }, {
                                                             "min": 1000,
                                                             "max": 4999,
                                                             "label": '1000-4999',
                                                             "color": "#ff585e"
                                                         }, {
                                                             "min": 500,
                                                             "max": 999,
                                                             "label": '500-1000',
                                                             "color": "#fb8146"
                                                         }, {
                                                             "min": 101,
                                                             "max": 499,
                                                             "label": '101-499',
                                                             "color": "#ffA500"
                                                         }, {
                                                             "min": 10,
                                                             "max": 100,
                                                             "label": '10-100',
                                                             "color": "#ffb248"
                                                         }, {
                                                             "min": 0,
                                                             "max": 9,
                                                             "label": '0-9',
                                                             "color": "#fff2d1"
                                                         }]))
    """取消显示国家名称"""
    m2.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    print("国外疫情地图已生成")
    m2.render("demo/result/国家疫情地图.html") #render()函数输出为html文件，你可以在render()中传递输出地址参数，将html文件保存到自定义的位置。
    return m2
if __name__ == "__main__":
    oversea_view()
    #print(alter_china_orther())