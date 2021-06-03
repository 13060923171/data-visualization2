import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}


def word_global():
    url = 'http://111.231.75.86:8000/api/statistics/latest'
    html = requests.get(url,headers=headers)
    content = html.json()
    #确诊人数
    confirmed = content['globalStatistics']['confirmedCount']
    #治愈人数
    cured = content['globalStatistics']['curedCount']
    return confirmed,cured


def countries_global():
    url = 'http://111.231.75.86:8000/api/countries/'
    html = requests.get(url, headers=headers)
    content = html.json()
    list_sum = []
    for i in range(215):
        current,name = content[i]['currentConfirmedCount'],content[i]['countryName']
        list_1 = [name,current]
        list_sum.append(list_1)
    list_sum.sort(key=lambda x:x[1],reverse=True)
    return list_sum[0:7]


def use_global():

    url1 = 'http://111.231.75.86:8000/api/provinces/USA/California/daily/'
    html1 = requests.get(url1, headers=headers)
    content1 = html1.json()
    list_sum1 = []
    for i in range(len(content1)):
        current1, name1 = content1[i]['currentConfirmedCount'], content1[i]['provinceName']
        list_1 = [name1, current1]
        list_sum1.append(list_1)
    list_sum1.sort(key=lambda x: x[1], reverse=True)

    url2 = 'http://111.231.75.86:8000/api/provinces/USA/NewYork/daily/'
    html2 = requests.get(url2, headers=headers)
    content2 = html2.json()
    list_sum2 = []
    for i in range(len(content2)):
        current2, name2 = content2[i]['currentConfirmedCount'], content2[i]['provinceName']
        list_2 = [name2, current2]
        list_sum2.append(list_2)
    list_sum2.sort(key=lambda x: x[1], reverse=True)

    url3 = 'http://111.231.75.86:8000/api/provinces/USA/Florida/daily/'
    html3 = requests.get(url3, headers=headers)
    content3 = html3.json()
    list_sum3 = []
    for i in range(len(content3)):
        current3, name3 = content3[i]['currentConfirmedCount'], content3[i]['provinceName']
        list_3 = [name3, current3]
        list_sum3.append(list_3)
    list_sum3.sort(key=lambda x: x[1], reverse=True)

    url4 = 'http://111.231.75.86:8000/api/provinces/USA/Illinois/daily/'
    html4 = requests.get(url4, headers=headers)
    content4 = html4.json()
    list_sum4 = []
    for i in range(len(content4)):
        current4, name4 = content4[i]['currentConfirmedCount'], content4[i]['provinceName']
        list_4 = [name4, current4]
        list_sum4.append(list_4)
    list_sum4.sort(key=lambda x: x[1], reverse=True)

    url5 = 'http://111.231.75.86:8000/api/provinces/USA/NorthCarolina/daily/'
    html5 = requests.get(url5, headers=headers)
    content5 = html5.json()
    list_sum5 = []
    for i in range(len(content5)):
        current5, name5 = content5[i]['currentConfirmedCount'], content5[i]['provinceName']
        list_5 = [name5, current5]
        list_sum5.append(list_5)
    list_sum5.sort(key=lambda x: x[1], reverse=True)

    url6 = 'http://111.231.75.86:8000/api/provinces/USA/Georgia/daily/'
    html6 = requests.get(url6, headers=headers)
    content6 = html6.json()
    list_sum6 = []
    for i in range(len(content6)):
        current6, name6 = content6[i]['currentConfirmedCount'], content6[i]['provinceName']
        list_6 = [name6, current6]
        list_sum6.append(list_6)
    list_sum6.sort(key=lambda x: x[1], reverse=True)

    url7 = 'http://111.231.75.86:8000/api/provinces/USA/Arizona/daily/'
    html7 = requests.get(url7, headers=headers)
    content7 = html7.json()
    list_sum7 = []
    for i in range(len(content7)):
        current7, name7 = content7[i]['currentConfirmedCount'], content7[i]['provinceName']
        list_7 = [name7, current7]
        list_sum7.append(list_7)
    list_sum7.sort(key=lambda x: x[1], reverse=True)

    return list_sum1[0],list_sum2[0],list_sum3[0],list_sum4[0],list_sum5[0],list_sum6[0],list_sum7[0],list_sum1[0]

def china_global():
    url = 'http://111.231.75.86:8000/api/provinces/CHN/'
    html = requests.get(url, headers=headers)
    content = html.json()
    list_sum = []
    for i in range(34):
        current, name = content[i]['currentConfirmedCount'], content[i]['provinceName']
        list_1 = [name, current]
        list_sum.append(list_1)
    list_sum.sort(key=lambda x: x[1], reverse=True)
    return list_sum[0:8]


def use_china_global():
    url = 'http://111.231.75.86:8000/api/countries/USA/daily/'
    html = requests.get(url, headers=headers)
    content = html.json()
    list_sum = []
    for i in range(len(content)):
        current = content[i]['confirmedCount']
        list_sum.append(current)
    list_sum.sort(key=lambda x: x, reverse=True)

    url1 = 'http://111.231.75.86:8000/api/countries/CHN/daily/'
    html1 = requests.get(url1, headers=headers)
    content1 = html1.json()
    list_sum1 = []
    for i in range(len(content1)):
        current1 = content1[i]['confirmedCount']
        list_sum1.append(current1)
    list_sum1.sort(key=lambda x: x, reverse=True)

    return list_sum[0:7],list_sum1[0:7]

def continents_global():
    url = 'http://111.231.75.86:8000/api/countries/?continents=北美洲'
    html = requests.get(url, headers=headers)
    content = html.json()
    list_sum = []
    for i in range(len(content)):
        current, name = content[i]['currentConfirmedCount'], content[i]['countryName']
        list_1 = [name, current]
        list_sum.append(list_1)
    list_sum.sort(key=lambda x: x[1], reverse=True)

    url1 = 'http://111.231.75.86:8000/api/countries/?continents=亚洲'
    html1 = requests.get(url1, headers=headers)
    content1 = html1.json()
    list_sum1 = []
    for i in range(len(content1)):
        current1, name1 = content1[i]['currentConfirmedCount'], content1[i]['countryName']
        list_2 = [name1, current1]
        list_sum1.append(list_2)
    list_sum1.sort(key=lambda x: x[1], reverse=True)

    url2 = 'http://111.231.75.86:8000/api/countries/?continents=欧洲'
    html2 = requests.get(url2, headers=headers)
    content2 = html2.json()
    list_sum2 = []
    for i in range(len(content2)):
        current2, name2 = content2[i]['currentConfirmedCount'], content2[i]['countryName']
        list_3 = [name2, current2]
        list_sum2.append(list_3)
    list_sum2.sort(key=lambda x: x[1], reverse=True)
    return list_sum[0:6],list_sum1[0:6],list_sum2[0:6]

def statistics_global():
    url = 'http://111.231.75.86:8000/api/statistics/latest'
    html = requests.get(url,headers=headers)
    content = html.json()
    global_statistics = content['globalStatistics']
    current = global_statistics['currentConfirmedCount']
    cure = global_statistics['curedCount']
    dead = global_statistics['deadCount']
    incr = global_statistics['currentConfirmedIncr']
    return current,cure,dead,incr

def map_chian():
    url = 'http://111.231.75.86:8000/api/provinces/CHN/'
    html = requests.get(url, headers=headers)
    content = html.json()
    data = []
    for i in range(len(content)):
        current, name = content[i]['confirmedCount'], content[i]['provinceName']
        datas = {
            'name':name,
            'value':current
        }
        data.append(datas)

    return data





if __name__ == '__main__':
    # global_word()
    # countries_global()
    # use_global()
    # china_global()
    # use_china_global()
    # continents_global()
    # statistics_global()
    map_chian()