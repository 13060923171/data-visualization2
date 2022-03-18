import pandas as pd
import paddlehub as hub
import os
from tqdm import tqdm


def sum_data(name1):
    df = pd.read_csv('./data/{}'.format(name1))
    #定义机械压缩函数
    def yasuo(st):
        for i in range(1,int(len(st)/2)+1):
            for j in range(len(st)):
                if st[j:j+i] == st[j+i:j+2*i]:
                    k = j + i
                    while st[k:k+i] == st[k+i:k+2*i] and k<len(st):
                        k = k + i
                    st = st[:j] + st[k:]
        return st

    df['评论内容-新'] = df['评论内容'].astype(str)
    df['评论内容-新'] = df['评论内容-新'].apply(yasuo)
    df['评论内容-新'] = df['评论内容-新'].replace(r'[.*[.*?].*]','',regex=True)
    # df['评论内容-新'] = df['评论内容-新'].dropna(how='any')
    #这里使用了百度开源的成熟NLP模型来预测情感倾向
    senta = hub.Module(name="senta_bilstm")
    texts = df['评论内容-新'].tolist()
    input_data = {'text':texts}
    res = senta.sentiment_classify(data=input_data)
    df['情感分值'] = [x['positive_probs'] for x in res]
    df.to_csv("./newdata/{}".format(name1),index=False)

if __name__ == '__main__':
    files = os.listdir(r'data/')
    for f in tqdm(files[19:]):
        try:
            sum_data(f)
        except:
            pass
