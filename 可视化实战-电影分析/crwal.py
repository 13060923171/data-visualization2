import requests
from lxml import etree
import pandas as pd
import time
headers = {
    "Cookie": "DIDA642a4585eb3d6e32fdaa37b44468fb6c=gq4ded9p1s8d4354i1ranl9420; Hm_lvt_e71d0b417f75981e161a94970becbb1b=1632273642; Hm_lpvt_e71d0b417f75981e161a94970becbb1b=1632273722",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
}

session = requests.session()
session.headers = headers

def get_parse(url):
    html = session.get(url,headers=headers)
    html.encoding = html.apparent_encoding
    if html.status_code == 200:
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):
    content = html.text
    soup = etree.HTML(content)
    odd = soup.xpath('//tr[@class="odd"]')
    even = soup.xpath('//tr[@class="even"]')
    list_mingci = []
    list_name = []
    list_href = []
    list_price = []
    list_cc = []
    list_rc = []
    list_piaojia = []
    for i in range(len(odd)):
        o = odd[i]
        e = even[i]
        mingci1 = o.xpath('./td[1]/text()')[0]
        list_mingci.append(mingci1)
        mingci2 = e.xpath('./td[1]/text()')[0]
        list_mingci.append(mingci2)
        name1 = o.xpath('./td[2]/a/text()')[0]
        list_name.append(name1)
        name2 = e.xpath('./td[2]/a/text()')[0]
        list_name.append(name2)
        href1 = o.xpath('./td[2]/a/@href')[0]
        list_href.append(href1)
        href2 = e.xpath('./td[2]/a/@href')[0]
        list_href.append(href2)
        # price1 = o.xpath('./td[3]/a/@href')[0]
        # list_price.append(price1)
        # price2 = e.xpath('./td[3]/a/@href')[0]
        # list_price.append(price2)
        cc1 = o.xpath('./td[4]/text()')[0]
        list_cc.append(cc1)
        cc2 = e.xpath('./td[4]/text()')[0]
        list_cc.append(cc2)
        rc1 = o.xpath('./td[5]/text()')[0]
        list_rc.append(rc1)
        rc2 = e.xpath('./td[5]/text()')[0]
        list_rc.append(rc2)
        piaojia1 = o.xpath('./td[6]/text()')[0]
        list_piaojia.append(piaojia1)
        piaojia2 = e.xpath('./td[6]/text()')[0]
        list_piaojia.append(piaojia2)

    list_city, list_leixing1,list_year = get_price(list_href)
    dowloands(list_mingci,list_name,list_cc,list_rc,list_piaojia,list_city, list_leixing1,list_year)

def get_price(urls):
    list_name = []
    list_leixing = []
    list_year = []
    for url in urls:
        url = "http://58921.com" + url
        html = session.get(url,headers=headers)
        html.encoding = html.apparent_encoding
        content = html.text
        soup = etree.HTML(content)
        name = soup.xpath('//div[@class="media-body"]/ul/li[6]/a/text()')
        list_name.append(name)
        leixing = soup.xpath('//div[@class="media-body"]/ul/li[7]/a/text()')
        list_leixing.append(leixing)
        year = soup.xpath('//div[@class="media-body"]/ul/li[4]/text()')
        list_year.append(year)
    return list_name,list_leixing,list_year

def dowloands(list_mingci,list_name,list_cc,list_rc,list_piaojia,list_city, list_leixing1,list_year):
    df = pd.DataFrame()
    df['名次'] = list_mingci
    df['名称'] = list_name
    df['场次'] = list_cc
    df['人次'] = list_rc
    df['票价'] = list_piaojia
    df['年份'] = list_year
    df['国家'] = list_city
    df['类型'] = list_leixing1

    try:
        df.to_csv("电影数据.csv", mode="a+",index=None,encoding="gbk")
        print("写入成功")
    except:
        print("当页数据写入失败")
    time.sleep(0.2)




if __name__ == '__main__':
    for i in range(0,10):
        url = 'http://58921.com/alltime/wangpiao?page={}'.format(i)
        get_parse(url)

