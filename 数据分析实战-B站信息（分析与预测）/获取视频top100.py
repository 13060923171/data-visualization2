import requests
from lxml import etree
import random
import re
import pandas as pd
import time
from tqdm import tqdm
import os


#构建请求头,反爬策略
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
    #随机请求反爬策略
    'user-agent': random.choice(user_agent),
    "referer": "https://www.bilibili.com/",
    # #到时候替换成你自己的
   "cookie": "_uuid=715101066C-FAA5-D175-EA51-51071BCDDFFB928793infoc; buvid3=0D1B00B3-6F3D-4B89-AFC7-DFE562DDF14F167614infoc; b_nut=1638068729; DedeUserID=35906556; DedeUserID__ckMd5=6bc77a6b9c4d788a; video_page_version=v_old_home; blackside_state=1; CURRENT_QUALITY=0; rpdid=|(umR~~|Ykmu0J'uYJ)JYY~R); i-wanna-go-back=-1; b_ut=5; LIVE_BUVID=AUTO1816398016892574; buvid4=C66AE545-82A9-EB40-B87C-DA9B90EDB50A31270-022013014-Vp25bGcbK8ZpT1kPMJFT9g%3D%3D; fingerprint=807b5f756ae9d19228302dac996d1efd; buvid_fp_plain=undefined; buvid_fp=f8287eb05aecbd49171ed08907b0b66d; SESSDATA=c7c7f7e4%2C1659262304%2C7c0f4%2A21; bili_jct=81d5eaa78413784a8cec20f7b076ab3c; sid=5g0611ll; nostalgia_conf=-1; PVID=1; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; bp_t_offset_35906556=639549840534011909; bp_video_offset_35906556=639705722063421474; innersign=0; b_lsid=984C574E_17FBAB0370E",
}

session = requests.session()
session.headers = headers

def get_parse(url):
    #请求网页
    html = session.get(url)
    # 请求网页查看是否为200，200说明网页正常，进行下去
    if html.status_code == 200:
        get_html(html)
    #否则返回状态码
    else:
        print(html.status_code)


def get_html(html):
    #获取数据源
    content = html.text
    #把数据源替换成xpath语法能读取到的数据
    soup = etree.HTML(content)
    #进行定位，定位到请求连接，后面要用到
    href = soup.xpath('//div[@class="info"]/a/@href')
    #进行定位，获取视频标题
    title = soup.xpath('//div[@class="info"]/a/text()')
    #进行定位，获取up主的名称
    name = soup.xpath('//div[@class="detail"]/a/span/text()')
    #循环获取到内容，zip是用于多个列表一起循环时使用的
    for h,n,t in tqdm(zip(href,name,title)):
        #构造视频主页面
        url1 = 'https:' + h
        #对名字进行清洗，删除多余字符
        n = str(n).strip('\n').strip(' ').replace('\n','')
        #传入到下一个函数里面
        xx_coment(url1,n,t)
        #停顿0.2秒
        time.sleep(0.2)


def xx_coment(url,name,title):
    #对上面获取到的URL进行请求
    html = session.get(url)
    #获取源码
    content = html.text
    # 把数据源替换成xpath语法能读取到的数据
    soup = etree.HTML(content)
    #加入防错机制，防止程序出错，导致停运
    try:
        #获取粉丝数
        number = soup.xpath('//div[@class="default-btn follow-btn btn-transition b-gz not-follow"]/span/span/text()')[0]
        number = str(number).strip('\n').strip(' ')
    except:
        #如果粉丝数获取不到，则返回空值
        number = ''
    try:
        fenlei = re.findall('name="keywords" content="(.*?)"><meta data-vue-meta',content)
        fenlei1 = str(fenlei[0]).split(',')
        fenlei2 = ' '.join(fenlei1[1:-4])
    except:
        fenlei2 = ''
    # 视频时长
    try:
        time_length = re.findall("\"timelength\":([0-9]*),", content)[0]
        time_length = (int(time_length) / 1000) / 60
        time_length = str(time_length).split('.')
        time_length = time_length[0] + ":" + time_length[1][:2]
    except:
        time_length = ''
    # 点赞，投币，收藏，转发
    video_message = soup.xpath('//div[@class="ops"]/span/text()')
    # 点赞
    message1 = str(video_message[0]).replace('\n', '').replace(' ', '')
    # 投币
    message2 = str(video_message[1]).replace('\n', '').replace(' ', '')
    # 收藏
    message3 = str(video_message[2]).replace('\n', '').replace(' ', '')
    # 转发
    message4 = str(video_message[3]).replace('\n', '').replace(' ', '')
    # 回复数量
    try:
        reply = re.findall("\"reply\":([0-9]*),", content)[0]
    except:
        reply = ''
    # 播放量
    try:
        view = re.findall("\"view\":([0-9]*),", content)[0]
    except:
        view = ''
    # 弹幕量
    try:
        danmaku = re.findall("\"danmaku\":([0-9]*),", content)[0]
    except:
        danmaku = ''

    #最后根据上面获取到的内容，保存到CSV文件里面
    df['标题'] = [title]
    df['时长'] = [time_length]
    df['up粉丝数'] = [number]
    df['分类'] = [fenlei2]
    df['点赞'] = [message1]
    df['投币'] = [message2]
    df['收藏'] = [message3]
    df['转发'] = [message4]
    df['播放量'] = [view]
    df['弹幕量'] = [danmaku]
    df['评论数'] = [reply]
    df.to_csv('top100.csv', mode='a+', encoding='utf-8', header=None,index=None)


if __name__ == '__main__':
    #top100的URL
    url = 'https://www.bilibili.com/v/popular/rank/all'
    #创建dataframe格式文件，用于保存数据
    df = pd.DataFrame()
    #构建请求头
    df['标题'] = ['标题']
    df['时长'] = ['时长']
    df['up粉丝数'] = ['up粉丝数']
    df['分类'] = ['分类']
    df['点赞'] = ['点赞']
    df['投币'] = ['投币']
    df['收藏'] = ['收藏']
    df['转发'] = ['转发']
    df['播放量'] = ['播放量']
    df['弹幕量'] = ['弹幕量']
    df['评论数'] = ['评论数']
    df.to_csv('top100.csv', mode='w', encoding='utf-8', header=None,index=None)
    get_parse(url)
    # #最后把获取好的数据，进行格式转换，把utf-8转换为gbk格式
    # df1 = pd.read_csv('top100.csv', encoding='utf-8')
    # df1.to_excel('top100.xlsx',index=None)
    # #删除多余数据
    # os.remove('top100.csv')