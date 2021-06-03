import requests
from lxml import etree
import pandas as pd
import time
import json
from tqdm import tqdm
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'Host': 'movie.douban.com',
    'Cookie': 'bid=WFHJJrPnd5o; ll="118281"; _ga=GA1.2.1241817330.1603959717; _gid=GA1.2.1200895418.1603959717; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1603959741%2C%22https%3A%2F%2Fm.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1241817330.1603959717.1603959741.1603959741.1; __utmb=30149280.0.10.1603959741; __utmc=30149280; __utmz=30149280.1603959741.1.1.utmcsr=m.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1241817330.1603959717.1603959741.1603959741.1; __utmb=223695111.0.10.1603959741; __utmc=223695111; __utmz=223695111.1603959741.1.1.utmcsr=m.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=DB3931C1DD44AEA8ECD3066F9C0F19603|1263ebd7592d13cb5208ca48c4c25867; _pk_id.100001.4cf6=1b27861feaef5cc8.1603959741.1.1603959776.1603959741.'
}

def get_parse(url):
    html = requests.get(url,headers=headers)
    if html.status_code == 200:
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):
    content = html.text
    soup = etree.HTML(content)
    items = soup.xpath("//div[@class ='main review-item']")
    short_list = []
    time_list = []
    title_list = []
    useful_list =[]
    useless_list = []
    reply_list = []
    for item in items:
        time = item.xpath("./header/span/text()")[0]
        title = item.xpath("./header/span/@title")
        short_content = item.xpath("./div/div/div[@class = 'short-content']/text()")[0].replace("(","").strip("\n").strip(" ").replace("\n","")
        # short_list.append(short_content)
        useful = item.xpath("./div/div[@class='action']/a/span/text()")[0].strip('\n').strip(" ").replace("\n","")
        useless = item.xpath("./div/div[@class='action']/a/span/text()")[1].strip('\n').strip(" ").replace("\n","")
        reply = item.xpath("./div/div[@class='action']//a[@class = 'reply ']/text()")[0]
        downloads(time,title,useful,useless,reply,short_content)
        # time_list.append(time)
        # title_list.append(title)
        # useful_list.append(useful)
        # useless_list.append(useless)
        # reply_list.append(reply)
    # print(short_list)
    # short_content = item.xpath('//div[@class ="short-content"]/text()')
    # for short in short_content:

    # print(short_content)


def downloads(time,title,useful,useless,reply,short):
    content = {
        '时间':time,
        '评价':title,
        "赞同人数":useful,
        "否定人数":useless,
        '回应人数':reply,
        '内容':short,
    }
    with open('豆瓣评论信息.text','a+',encoding='utf-8')as f:
        f.write(json.dumps(content, ensure_ascii=False) + "\n")
        print("写入成功")


if __name__ == '__main__':
    for i in tqdm(range(0,401,20)):
        url = 'https://movie.douban.com/subject/26794435/reviews?start={}'.format(i)
        get_parse(url)