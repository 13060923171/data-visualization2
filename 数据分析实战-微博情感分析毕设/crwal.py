import requests
import time
import random
import re
import pandas as pd

#对应微博该条评论的id号
id1 = '4700724870775299'

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
    #在这里输入对应的cookie
    "Cookie": "xxx",
    'Sec-Fetch-Mode': 'cors',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': 'application/json, text/plain, */*',
    #这里也是填写你的个人token
    'X-XSRF-TOKEN': 'xxx',
}

commentLists = []

#把获取到的内容写入到csv文件中
def write_in(index: str):
    global commentLists
    df = pd.DataFrame()
    df['commentor_name'] = []
    df['comment_text'] = []
    df['create_time'] = []
    df['like_count'] = []
    df['reply_number'] = []
    df.to_csv('{}-{}.csv'.format(id1,index), encoding='utf-8',index=None)
    for obj in commentLists:
        df['commentor_name'] = [obj['commentor_name']]
        df['comment_text'] = [obj['comment_text']]
        df['create_time'] = [obj['create_time']]
        df['like_count'] = [obj['like_count']]
        df['reply_number'] = [obj['reply_number']]
        df.to_csv('{}-{}.csv'.format(id1,index),encoding='utf-8',mode='a+',header=None,index=None)


# 将中国标准时间(Sat Mar 16 12:12:03 +0800 2019)转换成年月日
def formatTime(time_string, from_format, to_format='%Y.%m.%d %H:%M:%S'):
    time_struct = time.strptime(time_string, from_format)
    times = time.strftime(to_format, time_struct)
    return times


def extract_data(comments_list):
    global commentLists
    for commment_item in comments_list:
        # 删除评论文本中的html格式表情符号
        pure_text = re.sub('<.*?>', '', commment_item['text'])
        #用字典把信息保存下来，再传入到列表信息里面
        Obj = {
            'commentor_id': commment_item['user']['id'],
            'commentor_name': commment_item['user']['screen_name'],
            'commentor_blog_url': commment_item['user']['profile_url'],
            'comment_id': commment_item['id'],
            'comment_text': pure_text,
            'create_time': formatTime(commment_item['created_at'], '%a %b %d %H:%M:%S +0800 %Y', '%Y-%m-%d %H:%M:%S'),
            'like_count': commment_item['like_count'],
            'reply_number': commment_item['total_number'],
        }
        commentLists.append(Obj)

#获取第一页评论的内容
def first_page_comment(url):
    try:
        html = requests.get(url, headers=headers, timeout=20)
        js_con = html.json()
        max_id = js_con['data']['max_id']  # 下一页的max_id
        max = js_con['data']['max']  # 获取最大页数
        comments_list = js_con['data']['data']  # 提取评论内容
        extract_data(comments_list)
        print("已获取第1页的评论")
        return max_id, max, commentLists
    except Exception as e:
        print("遇到异常")


# 爬取剩余页面的评论
def get_rest_comments(count, weibo_id, url, headers, max, urlNew):
    global commentLists
    last = count  # 记录写入磁盘的页数
    while count <= max:
        # 避免被反爬
        time.sleep(0.8+random.random())
        try:
            web_data = requests.get(
                url=urlNew, headers=headers, timeout=10)

            # get请求成功
            if web_data.status_code == 200:
                #把内容转化为json格式
                js_con = web_data.json()
                print(js_con)
                if js_con['ok'] == 1:

                    # 提取数据
                    max_id = js_con['data']['max_id']
                    comments_list = js_con['data']['data']
                    max_id_type = js_con['data']['max_id_type']
                    extract_data(comments_list)
                    print("已获取第" + str(count) + "页的评论。")
                    count += 1
                    # 得到下一页的url
                    urlNew = url + str(weibo_id) + '&mid=' + str(weibo_id) + \
                        '&max_id=' + str(max_id) + \
                        '&max_id_type=' + str(max_id_type)

            else:
                raise Exception('Request Error')

            # 每500页写入一下txt
            if count % 500 == 0:
                # 格式化txt文件名称：wlh_{起始页}-{终止页}.txt
                index = str(str(last) + '-' + str(count))
                last = count + 1
                write_in(index)
                # 清空前面的数据
                commentLists = []
                # 记录一下当前的url，以免出错后要从头开始爬
                with open('log.txt', 'a') as log:
                    msg = '\nMark\n' + urlNew + '\ncnt = ' + str(count) + '\n'
                    log.write(msg)

        except Exception as e:

            e_msg = e.__str__()

            # 出现异常时保存当前读到的页数和url
            with open('log.txt', 'a') as log:
                msg = 'Error\n' + urlNew+'\ncnt = ' + str(count) + '\n'
                log.write(msg)+'\n'
                log.write(e_msg+'\n')

            # 把截至当前页数的数据写入磁盘
            index = str(last) + '-' + str(count)
            write_in(index)

            if e_msg[:5] == 'HTTPS':
                continue
            break

if __name__ == '__main__':
    #原始URL
    url = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id_type=0'.format(id1,id1)
    max_id, max_page, output = first_page_comment(url)

    if len(output) > 0:
        url1 = "https://m.weibo.cn/comments/hotflow?id="
        # 如果结果不只一页，就继续爬
        if (max_page != 1):
            urlNew = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id={}&max_id_type=0'.format(id1,id1,max_id)

            get_rest_comments(2, id1,
                              url1, headers, max_page, urlNew)

        else:
            print('----------------该微博的评论只有1页-----------------')