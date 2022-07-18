import requests
import random
import pandas as pd
from tqdm import tqdm
from lxml import etree
import time
from urllib.parse import quote
import re
import numpy as np


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
       "cookie": "SUB=_2A25Pe67ODeRhGeNN6lsS-CrJyz-IHXVshzKGrDV6PUJbkdAKLVbikW1NSdnQVFU7UpTLiJJh65KaEIqfJf39SWj5; _T_WM=9457f97ee39f0dd0dbd852abd89e6e8e",
    }
    html = requests.get(i, headers=headers)
    while True:
        if html.status_code == 200:
            break
    content = html.text
    soup = etree.HTML(content.encode('utf-8'))
    ctt = soup.xpath('//div[@class="c"]/div')
    try:
        dianzan1 = re.compile('">赞\[(.*?)\]</a>&nbsp;')
        dianzan = dianzan1.findall(content)
        zhuanfa1 = re.compile('">转发\[(.*?)\]</a>&nbsp;')
        zhuanfa = zhuanfa1.findall(content)
        pinglun1 = re.compile('">评论\[(.*?)\]</a>&nbsp;')
        pinglun = pinglun1.findall(content)
        # comment1 = re.compile('<span class="ctt">(.*?)</span></div><div><a')
        # comment = comment1.findall(content)

        timedate1 = re.compile('<span class="ct">(.*?)&nbsp;')
        timedate = timedate1.findall(content)
        for c,t,d,z,p in zip(ctt,timedate,dianzan,zhuanfa,pinglun):
            try:
                try:
                    comtent = c.xpath('./span[@class="ctt"]/text()')
                    comment2 = ' '.join(comtent)
                    print(comment2)
                except:
                    comment2 = np.NaN
                try:
                    date = t
                except:
                    date = np.NaN
                try:
                    like = d
                except:
                    like = np.NaN
                try:
                    zf = z
                except:
                    zf = np.NaN
                try:
                    pl = p
                except:
                    pl = np.NaN
                df = pd.DataFrame()
                df['时间'] = [date]
                df['内容'] = [comment2]
                df['点赞'] = [like]
                df['转发'] = [zf]
                df['评论'] = [pl]
                df.to_csv('深圳卫健委.csv', index=None, header=None, mode='a+', encoding='utf-8-sig')
            except:
                break
        time.sleep(0.1)
    except:
        pass

if __name__ == '__main__':
    df = pd.DataFrame()
    df['时间'] = ['时间']
    df['内容'] = ['内容']
    df['点赞'] = ['点赞']
    df['转发'] = ['转发']
    df['评论'] = ['评论']
    df.to_csv('深圳卫健委.csv',index=None,header=None,mode='w',encoding='utf-8-sig')
    rng = pd.date_range(start='02/13/2022', end='04/01/2022',freq='W')
    list_time = []
    for r in rng:
        r = str(r).split(" ")
        list_time.append(r[0].replace('-',''))
    list_time.append('20220401')
    str_list = ['疫情通报','清零','疫情防控','密接','新闻发布会']
    for s in str_list:
        q = quote(s)
    for l in tqdm(range(len(list_time)-1)):
        for i in range(1,101,1):
            url = 'https://weibo.cn/2831150640/profile?keyword={}&hasori=0&haspic=0&starttime={}&endtime={}&advancedfilter=1&page={}'.format(q,list_time[l],list_time[l+1],i)
            main_ur(url)

