import requests
from lxml import etree
from urllib import parse
import json
import re
from tqdm import tqdm
import time
import random
import pandas as pd


headers = {

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'referer': 'https://www.jd.com/',
    'cookie': '__jdu=161827796288293166331; areaId=19; ipLoc-djd=19-1601-36953-0; PCSYCityID=CN_440000_440100_440113; shshshfpa=afbfb5a6-2b2f-2cd1-32c9-08f6cb7b5e62-1618277978; shshshfpb=bUxR1wpyM7eG3WPxMIY3taQ%3D%3D; qrsc=3; user-key=0cbfeba7-166d-499e-a7f4-43ad907e30d3; __jda=122270672.161827796288293166331.1618277963.1618536384.1618542302.4; __jdc=122270672; __jdv=122270672|google|AmericaBrandC01|cpc|not set|1618542349131; _gcl_aw=GCL.1618542349.Cj0KCQjwyN-DBhCDARIsAFOELTn8DTrHrG6Gol_MbEO9yT7os8LsXCR2JbYqFx5z3RXdiUkBk1L1MGAaAnpkEALw_wcB; shshshfp=a0a87c2b662f78b0c547093c74c8c74c; rkv=1.0; __jdb=122270672.12.161827796288293166331|4.1618542302; shshshsID=7274c87af36cb9c5681d983fe6bd027d_10_1618542650847; 3AB9D23F7A4B3C9B=VXCREJHRBERJFNRSY7JQ5GDZ3XXG3TDRDLBEPH5N3QML3Y3RHTZRTEUTUJ3EE3LZOZRXXFF2ZTMB7NKN2N7PBKKTUA',

}




def get_parse(url):
    html = requests.get(url, headers=headers)
    if html.status_code == 200:
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):
    content = html.text
    soup = etree.HTML(content)
    list_price = []
    list_comment = []
    list_icons =[]
    try:
        for i in range(0,25):
            href = soup.xpath("//div[@class='p-img']/a[@target='_blank']/@href")[i]
            href = 'https:' + href
            commit = re.compile('https://item.jd.com/(.*?).html',re.S|re.I)
            commits = commit.findall(href)
            #获取评论数量
            comment = get_number(commits[0])
            comment = comment.strip(' ').replace('"comment":', '').replace('"', '').strip(' ').replace('万', '0000').replace(
                '+', '')
            comment = int(comment)
            list_comment.append(comment)
            #获取价格
            price = soup.xpath("//div[@class='p-price']/strong/i/text()")[i]
            list_price.append(float(price))
            #自营店铺的数据
            icons = get_icons(href)
            list_icons.append(int(icons))
            #获取结果页数
            number = soup.xpath("//div[@id='J_topPage']/span/i/text()")[0]
            a = random.random()
            time.sleep(a)
        get_comment(list_price,list_comment,list_icons,number)
    except:
        pass


def get_number(commits):
    url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds={}&callback=jQuery4456228&_=1618542993463'.format(commits)
    headers = {
        'Cookie': '__jdu=161827796288293166331; areaId=19; ipLoc-djd=19-1601-36953-0; PCSYCityID=CN_440000_440100_440113; shshshfpa=afbfb5a6-2b2f-2cd1-32c9-08f6cb7b5e62-1618277978; shshshfpb=bUxR1wpyM7eG3WPxMIY3taQ%3D%3D; jwotest_product=99; user-key=0cbfeba7-166d-499e-a7f4-43ad907e30d3; __jda=122270672.161827796288293166331.1618277963.1618536384.1618542302.4; __jdc=122270672; __jdv=122270672|google|AmericaBrandC01|cpc|not set|1618542349131; _gcl_aw=GCL.1618542349.Cj0KCQjwyN-DBhCDARIsAFOELTn8DTrHrG6Gol_MbEO9yT7os8LsXCR2JbYqFx5z3RXdiUkBk1L1MGAaAnpkEALw_wcB; shshshfp=a0a87c2b662f78b0c547093c74c8c74c; __jdb=122270672.15.161827796288293166331|4.1618542302; shshshsID=7274c87af36cb9c5681d983fe6bd027d_13_1618542977410; 3AB9D23F7A4B3C9B=VXCREJHRBERJFNRSY7JQ5GDZ3XXG3TDRDLBEPH5N3QML3Y3RHTZRTEUTUJ3EE3LZOZRXXFF2ZTMB7NKN2N7PBKKTUA',
        'Host': 'club.jd.com',
        'Referer': 'https://search.jd.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    }
    html = requests.get(url,headers=headers)
    a = random.random()
    time.sleep(a)
    content = html.text
    try:
        comment = re.compile('"CommentCountStr":"(.*?)",', re.I | re.S)
        comments = comment.findall(content)
        return comments[0]
    except:
        pass

def get_icons(url):
    html = requests.get(url, headers=headers)
    a = random.random()
    time.sleep(a)
    content = html.text
    soup = etree.HTML(content)
    try:
        name = soup.xpath("//div[@class='name']/a/text()")[0]
        sum_name = 0
        if '自营' in name:
            sum_name += 1
        return sum_name
    except:
        pass

def get_comment(list_price,list_comment,list_icons,number):
    max_price = max(list_price)
    min_price = min(list_price)
    max_comment = max(list_comment)
    min_comment = min(list_comment)
    price_scope = '{}-{}'.format(min_price,max_price)
    comment_scope = '{}-{}'.format(min_comment,max_comment)

    list_price_scope = []
    list_comment_scope = []
    sum_icons =[]
    list_keyword = []
    list_number = []

    list_price_scope.append(price_scope)
    list_comment_scope.append(comment_scope)
    sum_icons.append(sum(list_icons))
    list_keyword.append(str(i))
    list_number.append(int(number))

    save_to_file(list_price_scope,list_comment_scope,sum_icons,list_keyword,list_number)


#写一个保存文件的函数
def save_to_file(list_price_scope,list_comment_scope,list_icons,list_keyword,list_number):
    df = pd.DataFrame()
    df['关键词'] = list_keyword
    df['结果页数'] = list_number
    df['自营数量'] = list_icons
    df['评论区间'] = list_comment_scope
    df['价格区间'] = list_price_scope
    try:
        df.to_csv("茶具.csv", mode="a+", header=None, index=None, encoding="gbk")
        print("写入成功")
    except:
        print("当页数据写入失败")

if __name__ == '__main__':
    df1 = pd.read_excel('京东关键词-茶具.xls').loc[:,['关键词']]
    for i in tqdm(df1['关键词']):
        url = 'https://search.jd.com/Search?keyword={}'.format(parse.quote(i))
        get_parse(url)






