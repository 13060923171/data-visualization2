import requests
from lxml import etree
import concurrent.futures
from urllib import parse
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
import re
import json

headers = {
    "cookie": "_T_WM=2c774653950bc1610df40eaec4c5e9c5; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5GwlB4mf13pUNVQ0MzU9ZV5NHD95Qfe024e0nXSK50Ws4Dqcj.i--ciKLhiKn4i--NiKyhi-8Fi--RiKnfi-iFi--fi-2ciK.c; WEIBOCN_WM=3349; H5_wentry=H5; backURL=https%3A%2F%2Fweibo.cn%2F; SUB=_2A25Nirk4DeRhGeNN6lsS-CrJyz-IHXVvdMdwrDV6PUJbktANLRbSkW1NSdnQVHEuwshZLN2PawhpMLZbaPK3GXkv; SSOLoginState=1619970408",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
}

keyword = parse.quote('宝矿力')
list = []
for i in range(1,101,1):
    url = "https://weibo.cn/search/mblog?hideSearchFrame=&keyword={}&advancedfilter=1&starttime=20190101&endtime=20200101&sort=time&page={}".format(keyword,i)
    list.append(url)

def get_statue(url):
    html = requests.get(url,headers= headers)
    if html.status_code ==200:
        print("页面正常")
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):
    content = html.text
    soups = BeautifulSoup(content,'lxml')
    comment = soups.select('div span.ctt')
    href = soups.select('div a.nk')
    try:
        for l in range(len(href)):
            sex = check_gender(href[l]['href'])
            coment = comment[l].text
            write_txt(sex,coment)
    except:
        pass



def write_txt(sex,comment):
    data = {
        '性别': sex,
        '内容': comment,
    }
    with open("宝矿力微信评论信息.txt","a+",encoding="utf-8")as f:
        f.write(json.dumps(data,ensure_ascii=False)+"\n")
        print("写入成功")


def check_gender(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'cookie': 'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5GwlB4mf13pUNVQ0MzU9ZV5NHD95Qfe024e0nXSK50Ws4Dqcj.i--ciKLhiKn4i--NiKyhi-8Fi--RiKnfi-iFi--fi-2ciK.c; SUB=_2A25Nirk4DeRhGeNN6lsS-CrJyz-IHXVvdMdwrDV6PUJbktANLRbSkW1NSdnQVHEuwshZLN2PawhpMLZbaPK3GXkv; _T_WM=c3ec4a110c670479787145eec3131279',
    }
    html = requests.get(url,headers=headers)
    content = html.text
    time.sleep(0.3)
    sex = re.compile('</a>&nbsp;(.*?)    &nbsp;')
    sexs = sex.findall(content)
    try:
        if '男' in sexs[0]:
            return '男'
        elif '女' in sexs[0]:
            return '女'
        else:
            return '未知'
    except:
        pass

if __name__ == '__main__':
    s = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2)as e:
        futures = [e.submit(get_statue,i) for i in list]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
    print(time.time()-s)
