import requests
from lxml import etree
import random
import pandas as pd
import time
from tqdm import tqdm
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
    "cookie": "QN1=00009080306c4af5c9b0a8a2; QN300=www.google.com.hk; QN99=7926; QunarGlobal=10.67.197.57_-315863c_18548f11cc9_-4a4f|1671967543072; qunar-assist={%22version%22:%2220211215173359.925%22%2C%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false%2C%22theme%22:%22default%22}; QN205=s%3Dgoogle; QN277=s%3Dgoogle; QN601=52ed6c78bda27f30424909f0bdc748d3; QN269=DEA7F602844611EDAA9CFA163EFD983B; QN48=tc_4197b381eecb606d_18549081408_ac5a; QN163=0; fid=6cf106da-0cc6-43b4-ae38-9655b986322c; QN57=16719675543300.9857808169377869; QN58=1671967554327%7C1671967554327%7C1; Hm_lvt_c56a2b5278263aa647778d304009eafc=1671967594; viewpoi=26559258|7564992; uld=1-299878-2-1671967637; SECKEY_ABVK=HjuvmltQG7MkdU3DV+H4Fqeee71A2ljxO9wnuA7bYks%3D; BMAP_SECKEY=UeNJDpcv_O8nEpaFwL_bvKlqIM6CPaCe-x265Q3vkT9hxB39egPF9HAuvS4H9z76nbJG7J2JxKhRP-62hz0mYS4lTdjNhJPU9d8BXTCH_x42MZG8OAPprtvIEBPDVFimX1_rFRnfDyUzAVGPOsReWuTajZSQbGEaCzgcdYdFTc-BvuUSjvClzxZ0SRtS3xzK; ariaDefaultTheme=null; ctt_june=1654604625968##iK3wasg%3DWhPwawPwas0DaSv8XsvsXs2wE2DNaRXmEPP8X%3D3sESkGXKD%2BaPDsiK3siK3saKj%2BaK2%2BWK38WstOahPwaUvt; ctf_june=1654604625968##iK3waKDNWwPwawPwa%3DiTXPj%2BXPGGaRgAWS3%2BVRoDasTTVRtNERWhERg8ERDNiK3siK3saKj%2BaK2%2BWK38WstNaUPwaUvt; cs_june=9ed622132a2f300ebeac80b1c6a4943e8593406d61ce2babc489026303d496c984ad2f4e65ceadf4b3e36144526642bcc2092281736ff84495fc296e15859557b17c80df7eee7c02a9c1a6a5b97c11795e05c2a9c0aaa7f4d0f5f74252188f955a737ae180251ef5be23400b098dd8ca; QN271AC=register_pc; QN271SL=7cfa905b12748e9081ae171a16f023ff; QN271RC=7cfa905b12748e9081ae171a16f023ff; _q=U.cewnhbd2932; csrfToken=xVudpiP0ngjdxaygxwvBvxNyOKhob0tp; _s=s_B44D2ATJV4B57H7UW2DRDPY6A4; _t=27975693; _v=yLiYlWVjpSQOAgF3Sgk2gnjqhys9d7k8DtLWNXCFZIGGm0kanmC-3Er4eYmtcmA1JMIyaTsuKqaQjuSCiQSMmhQyNhpbLDxBw6ly9gqlXX3SnhcsiNofYDAxIbToB3qsqpeFfEznF5ArXbESrsyYxLt0XSyvBuzKTwGyVcAI4UV5; QN43=""; QN42=%E5%8E%BB%E5%93%AA%E5%84%BF%E7%94%A8%E6%88%B7; QN44=cewnhbd2932; _i=DFiEuY3z1wiwA_-wtBs0ByjdGNtw; _vi=uAECyopqZJxa6g8niYTw5H6X6mibDwrCL0Aapy_5N-EoLwBOgdzwaWoSV-gZbBrWbGTsnrwOsUFwWs9Js6BGcYNOgBt8XnmBgpnmoTpQeh-bxSykEbqZN3rCAGE9jPxlG3Xvy9pTnsJoa3AUFUHu3Bvge2o9T1BLh1gpSXIFqNy9; JSESSIONID=894E0C04F218CF9DEE87025D90563C97; QN267=1280119873fa32cb89; Hm_lpvt_c56a2b5278263aa647778d304009eafc=1671975371; QN271=7c463729-16a6-4a6c-b1d9-7f0b37f942b6",
    'user-agent': random.choice(user_agent),
    "referer": "https://travel.qunar.com/travelbook/list.htm?page=3&order=hot_heat",
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
}


def get_status(url):
    html = requests.get(url,headers=headers)
    content = html.text
    soup = etree.HTML(content)
    item = soup.xpath('//li[@class="list_item "]')
    for i in item:
        #标题
        try:
            title = i.xpath('./h2/a/text()')[0]
        except:
            title = ' '
        #出发时间
        try:
            date = i.xpath('./p/span/span[@class="date"]/text()')[0]
        except:
            date = ' '
        #停留时间
        try:
            days = i.xpath('./p/span/span[@class="days"]/text()')[0]
        except:
            days = ' '
        #游玩方式
        try:
            trip = i.xpath('./p/span/span[@class="trip"]/text()')[0]
        except:
            trip = ' '
        #费用
        try:
            fee = i.xpath('./p/span/span[@class="fee"]/text()')[0]
        except:
            fee = ' '
        #游玩人数
        try:
            people = i.xpath('./p/span/span[@class="people"]/text()')[0]
        except:
            people = ' '
        #途径与行程
        try:
            tujin = i.xpath('./p[@class="places"]/text()')
            tujin1 = ' '.join(tujin)
            tujin2 = tujin1.split('行程：')
            tujin3 = tujin2[0]
        except:
            tujin3 = ' '
        try:
            xinchen = "行程："+ str(tujin2[1])
        except:
            xinchen = ' '


        #观看量
        try:
            guankan = i.xpath('./p/span[@class="nums"]/span[1]/span/text()')[0]
        except:
            guankan = ' '

        df = pd.DataFrame()
        df['标题'] = [title]
        df['出发时间'] = [date]
        df['逗留时间'] = [days]
        df['费用'] = [fee]
        df['游玩人数'] = [people]
        df['游玩方式'] = [trip]
        df['观看量'] = [guankan]
        df['途径'] = [tujin3]
        df['行程'] = [xinchen]
        df.to_csv('data.csv', encoding='utf-8-sig', header=False, index=False, mode='a+')


if __name__ == '__main__':
    df = pd.DataFrame()
    df['标题'] = ['标题']
    df['出发时间'] = ['出发时间']
    df['逗留时间'] = ['逗留时间']
    df['费用'] = ['费用']
    df['游玩人数'] = ['游玩人数']
    df['游玩方式'] = ['游玩方式']
    df['观看量'] = ['观看量']
    df['途径'] = ['途径']
    df['行程'] = ['行程']
    df.to_csv('data.csv',encoding='utf-8-sig',header=False,index=False,mode='w')
    for i in tqdm(range(1,201)):
        url = 'https://travel.qunar.com/travelbook/list.htm?page={}&order=hot_heat'.format(i)
        get_status(url)
        time.sleep(1)