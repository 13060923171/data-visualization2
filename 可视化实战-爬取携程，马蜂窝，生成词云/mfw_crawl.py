import requests
import time
import json
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
import re

headers = {
    'referer': 'https://www.mafengwo.cn/poi/520.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'cookie': 'PHPSESSID=pc0bbmsthvilebht41c4g4tqq5; mfw_uuid=61a8bc36-da30-f58c-ab2a-2eb6ca467f66; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222021-12-02+20%3A29%3A42%22%3B%7D; uva=s%3A91%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1638448183%3Bs%3A10%3A%22last_refer%22%3Bs%3A23%3A%22http%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1638448183%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=61a8bc36-da30-f58c-ab2a-2eb6ca467f66; UM_distinctid=17d7b1f32b9a54-0b9227da65af35-978183a-e1000-17d7b1f32ba231; __mfwothchid=referrer%7Copen.weixin.qq.com; __omc_chl=; __mfwc=referrer%7Copen.weixin.qq.com; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1638448181,1638449074; login=mafengwo; mafengwo=41fa64e4d4b5ea047e4e552f481970de_86423828_61a8bfcfc03a77.78550349_61a8bfcfc03ad0.22245902; mfw_uid=86423828; __omc_r=; uol_throttle=86423828; __mfwa=1638448179871.19095.2.1638448179871.1638458154978; __mfwlv=1638458154; __mfwvn=2; __mfwb=6d21db14d61b.3.direct; __mfwlt=1638458170; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1638458171',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',

}


def get_parse(url):
    html = requests.get(url,headers=headers)
    if html.status_code == 200:
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):
    content = html.text
    content = re.sub('jQuery*\d+_*\d+','',content)
    content = content.replace('(', '').replace(');', '')
    content = json.loads(content)

    html1 = content['data']['html']
    soup = BeautifulSoup(html1,'lxml')
    content = soup.select('p.rev-txt')
    time1 = soup.select('div.info.clearfix span.time')
    for p in range(15):
        df = pd.DataFrame()
        c = str(content[p])
        t = str(time1[p])
        c = c.replace('<br/>','').replace('\n','').replace('class="rev-txt">','').replace('</p>','').replace('<p','').replace('～','')
        t = t.replace('<span class="time">','').replace('</span>','')
        df['时间'] = [t]
        df['内容'] = [c]
        df.to_csv('马蜂窝-迪士尼评论.csv',mode='a+',header=None,index=None,encoding='utf-8-sig')



if __name__ == '__main__':
    df1 = pd.DataFrame()
    df1['时间'] = ['时间']
    df1['内容'] = ['内容']
    df1.to_csv('马蜂窝-迪士尼评论.csv', mode='w', header=None, index=None, encoding='utf-8-sig')
    for i in tqdm(range(1,2)):
        url = 'https://pagelet.mafengwo.cn/poi/pagelet/poiCommentListApi?callback=jQuery18109039283409653498_1653125985557&params=%7B%22poi_id%22%3A%22520%22%2C%22page%22%3A{}%2C%22just_comment%22%3A1%7D&'.format(i)
        get_parse(url)
