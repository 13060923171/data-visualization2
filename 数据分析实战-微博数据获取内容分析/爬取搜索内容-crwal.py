import requests
import random
import pandas as pd
from tqdm import tqdm
from lxml import etree
import time





def main_ur(i):
    user_agent = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    headers = {
        'user-agent': random.choice(user_agent),
        "cookie": "SINAGLOBAL=1903674588878.3147.1642225343191; ALF=1673761372; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5GwlB4mf13pUNVQ0MzU9ZV5NHD95Qfe024e0nXSK50Ws4Dqcj.i--ciKLhiKn4i--NiKyhi-8Fi--RiKnfi-iFi--fi-2ciK.c; UOR=www.google.com,weibo.com,link.csdn.net; SUB=_2A25Pe6j9DeRhGeNN6lsS-CrJyz-IHXVsh8i1rDV8PUJbkNAfLVf_kW1NSdnQVEaAEn69ELv0DGAlgpMkTeQUcxjL; _s_tentry=weibo.com; Apache=1249497319017.3186.1657283749089; ULV=1657283749366:4:1:1:1249497319017.3186.1657283749089:1649472629322",
}

    html = requests.get(i,headers=headers)
    content = html.text
    soup = etree.HTML(content)
    node = soup.xpath('//div[@class="card-feed"]')
    act = soup.xpath('//div[@class="card-act"]/ul')
    for n,a in zip(node,act):
        name = n.xpath('./div[@node-type="like"]/div/div[2]/a/@nick-name')
        try:
            title = n.xpath('./div[@class="avator"]/a/span/@title')
        except:
            title = '无'
        timedate = n.xpath('./div[@node-type="like"]/p[@class="from"]/a[1]/text()')
        comtent = n.xpath('./div[@node-type="like"]/p[@node-type="feed_list_content"]/text()')
        comtent1 = ' '.join(comtent)

        dianzan = a.xpath('./li[3]/a/button/span[2]/text()')
        zhuanfa = a.xpath('./li[1]/a/text()')
        pinglun = a.xpath('./li[2]/a/text()')

        df = pd.DataFrame()
        df['时间'] = [timedate]
        df['博主'] = [name]
        df['认证'] = [title]
        df['内容'] = [comtent1]
        df['点赞'] = [dianzan]
        df['转发'] = [zhuanfa]
        df['评论'] = [pinglun]
        df.to_csv('离婚冷静期.csv', index=None, header=None, mode='a+', encoding='utf-8-sig')
    time.sleep(0.1)

if __name__ == '__main__':
    df = pd.DataFrame()
    df['时间'] = ['时间']
    df['博主'] = ['博主']
    df['认证'] = ['认证']
    df['内容'] = ['内容']
    df['点赞'] = ['点赞']
    df['转发'] = ['转发']
    df['评论'] = ['评论']
    df.to_csv('离婚冷静期.csv',index=None,header=None,mode='w',encoding='utf-8-sig')
    rng = pd.date_range(start='11/1/2020', end='2/28/2021')
    list_time = []
    for r in rng:
        r = str(r).split(" ")
        list_time.append(r[0])
    for l in tqdm(range(len(list_time)-1)):
        for i in range(1,51,1):
            url = 'https://s.weibo.com/weibo?q=%23%E7%A6%BB%E5%A9%9A%E5%86%B7%E9%9D%99%E6%9C%9F%23&typeall=1&suball=1&timescope=custom:{}:{}&Refer=g&page={}'.format(list_time[l],list_time[l+1],i)
            main_ur(url)

