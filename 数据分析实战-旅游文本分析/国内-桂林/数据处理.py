import jieba
import jieba.posseg as pseg
import pandas as pd
import stylecloud
from IPython.display import Image
import paddlehub as hub

#读取数据
df = pd.read_excel('携程游记.xlsx')
data = df['正文']
df1 = pd.read_excel('马蜂窝游记.xlsx')
data1 = df1['正文']
#把两个文档的数据合并
data2 = pd.concat([data1,data],axis=0)
#删除空值
new_data = data2.dropna(how='any')
#建立一个新的文档
new_data1 = pd.DataFrame(new_data)

#把不是中文的内容删除
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True


def get_cut_words(content_series):
    # 读入停用词表
    stop_words = []

    with open("stopwords_cn.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())

    # 分词
    word_num = jieba.lcut(content_series, cut_all=False)

    # 条件筛选，把没有用的词，无意义的词删除
    word_num_selected = [i for i in word_num if i not in stop_words and len(i) >= 2 and is_all_chinese(i) == True]
    word_num_selected = ' '.join(word_num_selected)
    return word_num_selected

#开始清洗工作
new_data1['清洗文本'] = new_data1['正文'].apply(get_cut_words)

#这里使用了百度开源的成熟NLP模型来预测情感倾向
senta = hub.Module(name="senta_bilstm")
texts = new_data1['清洗文本'].tolist()
input_data = {'text':texts}
#情感分析处理的步骤
res = senta.sentiment_classify(data=input_data)
new_data1['情感分值'] = [x['positive_probs'] for x in res]
#把处理好的分值用转化为小数类型
new_data1['情感分值'] = new_data1['情感分值'].astype(float)
#当分值小于0.45的时候定义为0，这里的0指的是负向
new_data1.loc[new_data1['情感分值'] <= 0.45, "情感分值"] = 0
#当分值大于0.55的时候定义为1，这里的0指的是正向
new_data1.loc[new_data1['情感分值'] >= 0.55, "情感分值"] = 1
#中间值为中立
new_data1.loc[(new_data1['情感分值'] > 0.45) & (new_data1['情感分值'] < 0.55), "情感分值"] = 2
#最后把文档保存起来
new_data1.to_csv('清洗好的文本内容.csv',encoding='utf-8-sig')
