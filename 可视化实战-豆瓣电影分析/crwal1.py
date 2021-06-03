import requests
from lxml import etree
from test import Book,sess
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Cookie': 'll="118281"; bid=sAd7BF-d3uY; _vwo_uuid_v2=D274087811B7F516CB45E4815D8B53F66|91509fe710515c9438e8f8c3c8696306; push_noty_num=0; push_doumail_num=0; __utmv=30149280.21208; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1617105538%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1229770440.1616992757.1617095519.1617105543.8; __utmc=30149280; __utmz=30149280.1617105543.8.5.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1922743201.1616992757.1617095519.1617105543.8; __utmb=223695111.0.10.1617105543; __utmc=223695111; __utmz=223695111.1617105543.8.5.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; dbcl2="212088227:9hIhN/HTeB0"; ck=eGgh; __utmt_douban=1; __utmt=1; __utmb=30149280.16.10.1617105543; _pk_id.100001.4cf6=3904bfb29117c963.1616992757.8.1617109203.1617096614.'
}


countrys = ''

quotes = ''

titles = ''

times = ''

types = ''

numbers = ''

comments = ''

def get_parse(url):
    html = requests.get(url,headers=headers)
    if html.status_code == 200:
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):
    content = html.json()
    for i in range(len(content['subjects'])):
        url = content['subjects'][i]['url']
        get_content(url)

def get_content(url):
    html = requests.get(url,headers=headers)
    content = html.text
    soup = etree.HTML(content)
    get_content1(content)
    # items = soup.xpath("//div[@id='content']")
    # for i in items:
    #     title = i.xpath("./h1/span/text()")[0]
    #     time = i.xpath("./h1/span/text()")[1].replace('(','').replace(')','')
    #     type = i.xpath(".//span[@property='v:genre']/text()")
    #     number = i.xpath(".//strong[@class='ll rating_num']/text()")[0]
    #     comment = i.xpath(".//span[@property='v:votes']/text()")[0]
    #     connent_mysql(title,time,type,number,comment)

def get_content1(html):
    global countrys,quotes,titles,times,types,numbers,comments
    country = re.compile('<span class="pl">制片国家/地区:</span>(.*?)<br/>',re.S|re.I)
    countrys = country.findall(html)
    quote = re.compile('<span class="pl">又名:</span>(.*?)<br/>', re.S | re.I)
    quotes = quote.findall(html)
    title = re.compile('<input type="hidden" name="title" value="(.*?)">', re.S | re.I)
    titles = title.findall(html)
    time = re.compile(r'<span class="year">(.*?)</span>', re.S | re.I)
    times = time.findall(html)
    type = re.compile('<span property="v:genre">(.*?)</span>', re.S | re.I)
    types = type.findall(html)
    number = re.compile('<strong class="ll rating_num" property="v:average">(.*?)</strong>', re.S | re.I)
    numbers = number.findall(html)
    comment = re.compile('<span property="v:votes">(.*?)</span>人评价', re.S | re.I)
    comments = comment.findall(html)

    connent_mysql(titles,times,countrys,types,numbers,comments,quotes)



def connent_mysql(titles,times,countrys,types,numbers,comments,quotes):
    try:
        book_data = Book(
            title=titles,
            time=times,
            country=countrys,
            type=types,
            number=numbers,
            comment=comments,
            quote=quotes
        )
        sess.add(book_data)
        sess.commit()
    except Exception as e:
        print(e)
        # 如果出错了就回滚到原来的地方
        sess.rollback()


if __name__ == '__main__':
    for i in range(0,201,20):
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%88%B1%E6%83%85&sort=recommend&page_limit=20&page_start={}'.format(i)
        get_parse(url)