import datetime
import sys
import time

import pandas as pd
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
### 储存信息
url = f"https://weibo.com/hot/weibo/102803"


def login():
    driver.get("https://s.weibo.com/weibo?q=%E7%96%AB%E6%83%85&Refer=realtime_weibo&page=1")
    input("请手动登录，登录后请回车")
    time.sleep(2)
    print("登录成功!")


def getData():
    driver.get(url)
    time.sleep(1)
    if url == f"https://weibo.com/hot/weibo/102803":
        input("搜索完毕请回车")
        time.sleep(1.5)
    for i in range(3000,300001,3000):
        driver.execute_script("window.scrollBy(0,{})".format(i))
        page = driver.page_source
        parse(page)
        time.sleep(1)
    driver.close()

def parse(page):
    item_list = []
    tree = etree.HTML(page)
    div_list = tree.xpath('//div[@class="detail_text_1U10O detail_ogText_2Z1Q8 wbpro-feed-ogText"]')
    for div in div_list:
        item = {}
        content = div.xpath('./div[@class="detail_wbtext_4CRf9"]/text()')
        data = []
        if len(content) != 0:
            for c in content:
                data.append(c)
        else:
            data = None
        comment = ' '.join(data)
        item['content'] = comment
        print(item)
        item_list.append(item)
    df = pd.DataFrame(item_list)
    df.to_csv(f"微博热门信息.csv",mode="a+",encoding="utf-8-sig",index=False,header=False)


if __name__ == '__main__':
    df = pd.DataFrame()
    df['comment'] = ['comment']
    df.to_csv(f"微博热门信息.csv", mode="w", encoding="utf-8-sig", index=False, header=False)
    login()
    getData()
    sys.exit()