import requests
from lxml import etree
import random
import re
import pandas as pd
import time
from tqdm import tqdm
import os

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
    "origin": "https://search.bilibili.com",
   "cookie": "_uuid=715101066C-FAA5-D175-EA51-51071BCDDFFB928793infoc; buvid3=0D1B00B3-6F3D-4B89-AFC7-DFE562DDF14F167614infoc; b_nut=1638068729; DedeUserID=35906556; DedeUserID__ckMd5=6bc77a6b9c4d788a; video_page_version=v_old_home; blackside_state=1; CURRENT_QUALITY=0; rpdid=|(umR~~|Ykmu0J'uYJ)JYY~R); i-wanna-go-back=-1; b_ut=5; LIVE_BUVID=AUTO1816398016892574; buvid4=C66AE545-82A9-EB40-B87C-DA9B90EDB50A31270-022013014-Vp25bGcbK8ZpT1kPMJFT9g%3D%3D; fingerprint=807b5f756ae9d19228302dac996d1efd; buvid_fp_plain=undefined; buvid_fp=f8287eb05aecbd49171ed08907b0b66d; SESSDATA=c7c7f7e4%2C1659262304%2C7c0f4%2A21; bili_jct=81d5eaa78413784a8cec20f7b076ab3c; sid=5g0611ll; bp_t_offset_35906556=629159455574008408; bp_video_offset_35906556=631834442866884617; CURRENT_BLACKGAP=0; innersign=0; b_lsid=EDFE95D7_17F55230D71; nostalgia_conf=-1; CURRENT_FNVAL=80; PVID=1",
}

#????????????????????????
def get_parse(url,data):
    html = requests.get(url,headers=headers,params=data)
    if html.status_code == 200:
        return 200,html
    else:
        return html.status_code,html

#????????????????????????
def video_number():
    data = {
        "__refresh__": "true",
        "_extra":None,
        "context":None,
        "page": 1,
        "page_size": 42,
        "from_source": None,
        "from_spmid": 333.337,
        "platform": "pc",
        "highlight": 1,
        "single_column": 0,
        "keyword": keyword,
        "category_id":None,
        "search_type": "video",
        "dynamic_offset": 30,
        "preload": "true",
        "com2co": "true",
    }
    url = "https://api.bilibili.com/x/web-interface/search/type?"
    status,html = get_parse(url,data)
    if status == 200:
        content = html.json()
        #????????????
        numPages = content['data']['numPages']
        video_content(numPages)
    else:
        return '??????????????????????????????'


#?????????????????????????????????
def video_content(numPages):
    count = 0
    for n in tqdm(range(1,int(numPages)+1)):
        data = {
            "__refresh__": "true",
            "_extra": None,
            "context": None,
            "page": n,
            "page_size": 42,
            "from_source": None,
            "from_spmid": 333.337,
            "platform": "pc",
            "highlight": 1,
            "single_column": 0,
            "keyword": '??????',
            "category_id": None,
            "search_type": "video",
            "dynamic_offset": 30,
            "preload": "true",
            "com2co": "true",
        }
        url = "https://api.bilibili.com/x/web-interface/search/type?"
        status, html = get_parse(url,data=data)
        if status == 200:
            content = html.json()
            # ????????????
            result = content['data']['result']
            for r in result:
                try:
                    #bvid
                    bvid = r['bvid']
                    xx_coment(bvid)
                    count += 1
                    if count > 100:
                        break
                    time.sleep(0.1)
                except Exception as e:
                    pass
        else:
            return '??????????????????????????????'
        if count > 100:
            break


def xx_coment(bvid):
    url = 'https://www.bilibili.com/video/{}?from=search&seid=9220732790560164695&spm_id_from=333.337.0.0'.format(bvid)
    status, html = get_parse(url, data=None)
    if status == 200:
        #????????????
        content = html.text
        # ?????????????????????xpath???????????????????????????
        soup = etree.HTML(content)
        #????????????
        try:
            time_length = re.findall("\"timelength\":([0-9]*),", content)[0]
            time_length = (int(time_length) / 1000) / 60
            time_length = str(time_length).split('.')
            time_length = time_length[0] + ":" + time_length[1][:2]
        except:
            time_length = ''
        #?????????????????????????????????
        video_message = soup.xpath('//div[@class="ops"]/span/text()')
        #??????
        message1 = str(video_message[0]).replace('\n','').replace(' ','')
        #??????
        message2 = str(video_message[1]).replace('\n','').replace(' ','')
        #??????
        message3 = str(video_message[2]).replace('\n','').replace(' ','')
        #??????
        message4 = str(video_message[3]).replace('\n','').replace(' ','')
        #????????????
        title = soup.xpath('//div[@id="viewbox_report"]/h1/span/text()')[0]
        #??????oid
        try:
            oid = re.findall("\"aid\":([0-9]*),", content)[0]
        except:
            oid = ''
        #????????????
        try:
            reply = re.findall("\"reply\":([0-9]*),", content)[0]
        except:
            reply = ''
        #?????????
        try:
            view = re.findall("\"view\":([0-9]*),", content)[0]
        except:
            view = ''
        # ?????????
        try:
            danmaku = re.findall("\"danmaku\":([0-9]*),", content)[0]
        except:
            danmaku = ''
        df['??????'] = [title]
        df['??????'] = [time_length]
        df['??????'] = [message1]
        df['??????'] = [message2]
        df['??????'] = [message3]
        df['??????'] = [message4]
        df['?????????'] = [view]
        df['?????????'] = [danmaku]
        df['?????????'] = [reply]
        df['??????oid'] = [oid]
        try:
            df.to_csv('??????top100?????????.csv', mode='a+', header=None, index=None, encoding='utf-8')
            print('success write')
        except:
            print('????????????')




if __name__ == '__main__':
    str1 = '??????'
    keyword = str1
    df = pd.DataFrame()
    df['??????'] = ['??????']
    df['??????'] = ['??????']
    df['??????'] = ['??????']
    df['??????'] = ['??????']
    df['??????'] = ['??????']
    df['??????'] = ['??????']
    df['?????????'] = ['?????????']
    df['?????????'] = ['?????????']
    df['?????????'] = ['?????????']
    df['??????oid'] = ['??????oid']
    df.to_csv('??????top100?????????.csv',mode='w',header=None,index=None,encoding='utf-8')
    video_number()

