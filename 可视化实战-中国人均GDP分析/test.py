from pyecharts import options as opts
from pyecharts.charts import Map, Page
from pyecharts.faker import Collector, Faker

C = Collector()

ENGLISH_PROVINCE_NAMES = {
        "广东": "guangdong",
        "安徽": "anhui",
        "福建": "fujian",
        "甘肃": "gansu",
        "广西": "guangxi",
        "贵州": "guizhou",
        "海南": "hainan",
        "河北": "hebei",
        "黑龙江": "heilongjiang",
        "河南": "henan",
        "湖北": "hubei",
        "湖南": "hunan",
        "江苏": "jiangsu",
        "江西": "jiangxi",
        "吉林": "jilin",
        "辽宁": "liaoning",
        "内蒙古": "neimenggu",
        "宁夏": "ningxia",
        "青海": "qinghai",
        "山东": "shandong",
        "山西": "shanxi",
        "陕西": "shanxi1",
        "四川": "sichuan",
        "台湾": "taiwan",
        "新疆": "xinjiang",
        "西藏": "xizang",
        "云南": "yunnan",
        "浙江": "zhejiang",
        "重庆": "Chong Qing",
        "香港": "Hong Kong",
        "澳门": "Macao",
        "南海诸岛": "South China Sea Islands",
        "北京": "Beijing",
        "天津": "Tianjin",
        "上海": "Shanghai"
    }

@C.funcs
def map_base() -> Map:
    c = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china", name_map=ENGLISH_PROVINCE_NAMES)
        .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
        .render()
    )

    return c
