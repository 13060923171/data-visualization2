import requests
from lxml import etree
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Cookie': 'll="118281"; bid=sAd7BF-d3uY; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1616992757%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DjmHn2WxcAv4C38IXjJBGakERIme4mrA_tMpwuK1RRKttZiyD8V8frglgIpJcGhFX%26wd%3D%26eqid%3Df8e293c90006b57b00000006606159f0%22%5D; __utma=30149280.1229770440.1616992757.1616992757.1616992757.1; __utmc=30149280; __utmz=30149280.1616992757.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1922743201.1616992757.1616992757.1616992757.1; __utmc=223695111; __utmz=223695111.1616992757.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=D274087811B7F516CB45E4815D8B53F66|91509fe710515c9438e8f8c3c8696306; _pk_id.100001.4cf6=3904bfb29117c963.1616992757.1.1616992814.1616992757.',
}

def get_parse(url):
    html = requests.get(url,headers=headers)
    if html.status_code == 200:
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):
    content = html.text
    soup = etree.HTML(content)
    item = soup.xpath("//div[@class='item']")
    for i in item:
        try:
            title = i.xpath('./div/div/a/span/text()')[0]
            time = i.xpath("./div/div[@class='bd']/p/text()")[1].replace('\n','').replace(' ','').split('/')[0][0:4]
            country = i.xpath("./div/div[@class='bd']/p/text()")[1].split('/')[1]
            type = i.xpath("./div/div[@class='bd']/p/text()")[1].replace('\n','').split('/')[-1]
            number = i.xpath(".//div[@class='star']/span[@class='rating_num']/text()")[0]
            comment = i.xpath(".//div[@class='star']/span/text()")[1]
            quote = i.xpath("./div/div[@class='bd']/p[@class='quote']/span/text()")[0]
            df['title'] = [title]
            df['time'] = [time]
            df['country'] = [country]
            df['type'] = [type]
            df['comment'] = [comment]
            df['quote'] = [quote]
            df['number'] = [number]
            df.to_csv('电影.csv', mode='a+', encoding='utf-8', header=None, index=None)
        except:
            pass



if __name__ == '__main__':
    df = pd.DataFrame()
    df['title'] = ['title']
    df['time'] = ['time']
    df['country'] = ['country']
    df['type'] = ['type']
    df['comment'] = ['comment']
    df['quote'] = ['quote']
    df['number'] = ['number']
    df.to_csv('电影.csv',mode='a+',encoding='utf-8',header=None,index=None)
    for i in range(0,226,25):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
        get_parse(url)