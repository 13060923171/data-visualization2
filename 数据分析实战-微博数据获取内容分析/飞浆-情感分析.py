import paddlehub as hub
import pandas as pd

df = pd.read_csv('new_class.csv')

#这里使用了百度开源的成熟NLP模型来预测情感倾向
senta = hub.Module(name="senta_bilstm")
texts = df['内容'].tolist()
input_data = {'text':texts}
res = senta.sentiment_classify(data=input_data)
df['情感分值'] = [x['positive_probs'] for x in res]


def tihuan(x):
    x = float(x)
    if x <= 0.3:
        return '负面'
    else:
        return '非负'

df['情感分值'] = df['情感分值'].apply(tihuan)
df.to_csv('情感_离婚冷静期.csv',index=None,encoding='utf-8-sig')

