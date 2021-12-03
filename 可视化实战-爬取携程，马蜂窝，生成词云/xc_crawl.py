import requests
import time
import json
import pandas as pd
from tqdm import tqdm
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    'cookie': 'GUID=09031095410095346961; _RF1=61.140.95.235; _RGUID=d9bd0cfa-e53f-459a-a450-3f90e3f85ad5; _RDG=28b6fdb92f11fa2fbf342cdf27fa1f94f2; _RSG=QMqFbhF3zcDLh5.Z3vFGHA; MKT_CKID_LMT=1638443273985; MKT_CKID=1638443273985.hs37f.l4mb; MKT_Pagesource=PC; _ga=GA1.2.1722528149.1638443275; _gid=GA1.2.329090127.1638443275; _gcl_aw=GCL.1638443275.Cj0KCQiA-qGNBhD3ARIsAO_o7ymD0LqdZryfKMvu4emgbxFKA15Wyc5G9PQqhB-EmZi0IBiw9jDYGzQaAvTgEALw_wcB; _gcl_dc=GCL.1638443275.Cj0KCQiA-qGNBhD3ARIsAO_o7ymD0LqdZryfKMvu4emgbxFKA15Wyc5G9PQqhB-EmZi0IBiw9jDYGzQaAvTgEALw_wcB; _bfaStatusPVSend=1; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; nfes_isSupportWebP=1; login_uid=1CE2EC2E3B7D80C522BA26EAD67377A9; login_type=0; cticket=0D5C05792E30F37FE7636B48B0E77B4EF384D83B8490E8C7A7AD736B4867288A; AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0; DUID=u=1CE2EC2E3B7D80C522BA26EAD67377A9&v=0; IsNonUser=F; UUID=0F15D87682DE430D8A7991E88097708B; IsPersonalizedLogin=F; Union=OUID=&AllianceID=4899&SID=155989&SourceID=&createtime=1638443451&Expires=1639048251279; MKT_OrderClick=ASID=4899155989&AID=4899&CSID=155989&OUID=&CT=1638443451282&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155989%26allianceid%3D4899%26gclid%3DCj0KCQiA-qGNBhD3ARIsAO_o7yl4RF3SSMmuYCuVkaDLqpYUj3edNqY9oV31-1dw1GwvT3gRrLfqFRYaAm9pEALw_wcB%26gclsrc%3Daw.ds%26keywordid%3D489496324552-72670506432&VAL={"pc_vid":"1638443271139.2j5lzb"}; _gac_UA-3748357-1=1.1638443451.Cj0KCQiA-qGNBhD3ARIsAO_o7yl4RF3SSMmuYCuVkaDLqpYUj3edNqY9oV31-1dw1GwvT3gRrLfqFRYaAm9pEALw_wcB; _uetsid=95fecac0536011ec96f8cd5261a640b1; _uetvid=95ff65e0536011ec8d51e5126df7bb8d; _gcl_au=1.1.581028425.1638443484; appFloatCnt=2; librauuid=3hZ6uZpn0dLfu9XF; _bfa=1.1638443271139.2j5lzb.1.1638443271139.1638443271139.1.12; _bfs=1.12; _bfi=p1%3D290510%26p2%3D290510%26v1%3D12%26v2%3D11; _jzqco=%7C%7C%7C%7C%7C1.331680150.1638443273999.1638443541835.1638443550677.1638443541835.1638443550677.0.0.0.8.8; __zpspc=9.1.1638443273.1638443550.8%231%7Cgoogleppc%7Cgoogle%7Cpp%7C%7C%23; _bfaStatus=send',
    'cookieorigin': 'https://you.ctrip.com',
    'referer': 'https://you.ctrip.com/',
    'origin': 'https://you.ctrip.com',
    'Host':'m.ctrip.com',

}



def get_parse(url,i):
    data = {
        'arg': {
            'channelType': 2,
            'collapseType': 0,
            'commentTagId': 0,
            'pageIndex': i,
            'pageSize': 10,
            'poiId': 31677717,
            'sortType': 3,
            'sourceType': 1,
            'starType': 0,
        },
        'head': {
            'auth': "",
            'cid': "09031095410095346961",
            'ctok': "",
            'cver': "1.0",
            'extension': [],
            'lang': "01",
            'sid': "8888",
            'syscode': "09",
            'xsid': "",
        }
    }
    html = requests.post(url,headers=headers,data=json.dumps(data))
    if html.status_code == 200:
        get_html(html)
    else:
        print(html.status_code)

def get_html(html):
    content = html.json()
    result = content['result']['items']
    for r in result:
        df = pd.DataFrame()
        content1 = r['content']
        comment = r['publishTypeTag']
        df['评论'] = [content1]
        df['时间'] = [comment]
        df.to_csv('环球影城评论200.csv',mode='a+',header=None,index=None)
        time.sleep(0.1)



if __name__ == '__main__':
    url = 'https://m.ctrip.com/restapi/soa2/13444/json/getCommentCollapseList?_fxpcqlniredt=09031155210110660291&x-traceID=09031155210110660291-1638496160257-600129'
    for i in tqdm(range(1,41)):
        get_parse(url,i)