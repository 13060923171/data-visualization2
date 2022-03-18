import random
import pandas as pd
import time
from tqdm import tqdm
import requests

df = pd.read_csv('非遗top100信息表.csv').loc[76:,['标题','评论数','评论oid']]

df['标题'] = df['标题'].replace(r'【.*?】',' ',regex=True).replace(r'《.*?》',' ',regex=True)
title = list(df['标题'])
print(title)
replay = list(df['评论数'])
oid = list(df['评论oid'])



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

#爬二级评论
def reply_clean(reply):
    level = reply['member']['level_info']['current_level']  # 等级
    content = reply['content']['message'].replace("\n", "")  # 评论内容
    t = reply['ctime']
    timeArray = time.localtime(t)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)  # 评论时间，时间戳转为标准时间格式
    return level,content,otherStyleTime,'回复'


#获取评论信息
def acquire_reply(oid,reply,title):
    page = int(int(reply) / 20) + 1
    for i in tqdm(range(1, int(page)+1)):
        try:
            url = 'https://api.bilibili.com/x/v2/reply/main?jsonp=jsonp&next={}&type=1&oid={}&mode=3&plat=1'.format(i,oid)
            html = requests.get(url, headers=headers)
            content = html.json()
            if content['message'] == '请求被拦截':
                print(content)
                time.sleep(1800)
                continue
            else:
                replies = content['data']['replies']
                for r in replies:
                    count = r['count']
                    content = r['content']['message'].replace("\n", "")
                    level = r['member']['level_info']['current_level']  # 等级
                    t = r['ctime']
                    timeArray = time.localtime(t)
                    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)  # 评论时间，时间戳转为标准时间格式

                    type1 = '评论'
                    df1['评论内容'] = [content]
                    df1['评论时间'] = [otherStyleTime]
                    df1['评论人等级'] = [level]
                    df1['评论类型'] = [type1]

                    df1.to_csv('./data/{}.csv'.format(title),mode='a+',index=None,header=None,encoding='utf-8')
                    if count >= 1:
                        replies1 = r['replies']
                        for r1 in replies1:
                            level,content,otherStyleTime,type2 = reply_clean(r1)
                            df1['评论内容'] = [content]
                            df1['评论时间'] = [otherStyleTime]
                            df1['评论人等级'] = [level]
                            df1['评论类型'] = [type2]
                            df1.to_csv('./data/{}.csv'.format(title), mode='a+', index=None, header=None, encoding='utf-8')
                    else:
                        pass
                    time.sleep(0.2)
        except:
            continue

if __name__ == '__main__':
    number = 0
    for t,r,o in zip(title,replay,oid):
        t = str(t).replace('|',' ')
        df1 = pd.DataFrame()
        df1['评论内容'] = ['评论内容']
        df1['评论时间'] = ['评论时间']
        df1['评论人等级'] = ['评论人等级']
        df1['评论类型'] = ['评论类型']
        df1.to_csv('./data/{}.csv'.format(t), index=None, mode='w', header=None, encoding='utf-8')
        acquire_reply(o,r,t)
