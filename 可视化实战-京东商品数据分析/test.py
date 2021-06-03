import pandas as pd
from urllib import parse
df1 = pd.read_excel('京东关键词-茶具.xlsx').loc[:,['关键词']]
for i in df1['关键词']:
    url = 'https://search.jd.com/Search?keyword={}'.format(parse.quote('{}'.format(i)))
    print(url)