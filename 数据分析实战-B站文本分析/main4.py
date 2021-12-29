# -*- coding: utf-8 -*-
# import jieba
import pandas as pd
import matplotlib.pyplot as plt

# jieba.load_userdict('过滤词.txt')
# 对原文本分词
def cut_words():
    # 获取当前文件路径
    df = pd.read_excel('bilibili主评.xlsx').loc[:,['评论内容']]
    df2 = pd.DataFrame()
    text1 = df.astype('str').values
    counts = {}
    for t in text1:
        text = jieba.lcut(t[0])
        for word in text:
            counts[word] = counts.get(word, 0) + 1
        lst = []
        for i in range(len(find)):
            try:
                df2['find'] = [find[i]]
                df2['counts'] = [counts[find[i]]]
                df2.to_csv('频次.csv',mode='a+',header=None,index=None,encoding='utf-8')
                print(find[i], counts[find[i]])
            except:
                lst.append(find[i])
        print('不存在的词:', lst)
    #     for i in text:
    #         content += i
    #         content += " "
    # return content

def cl_csv():
    df = pd.read_csv('频次.csv')
    df1 = df.groupby(['关键词']).sum()
    data_pair = [(i, int(j)) for i, j in zip(df1.index, df1['频次'].values)]
    data_pair.sort(key=lambda x:x[1],reverse=True)
    data_pair = data_pair[0:10]

    x_data = ['popularization\n of science','recommend','support','sprout','significance','look\nforward to','amount\nof play','amusing',
                                                                                         'major','great']
    y_data = [i[1] for i in data_pair]
    x_data.reverse()
    y_data.reverse()
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.figure(figsize=(14, 6),dpi=500)
    plt.barh(x_data, y_data)
    font1 = {
        'size': 16,
    }
    plt.tick_params(labelsize=16)
    plt.title("Top 10 hot words",font1)
    plt.xlabel("frequency",font1)
    # plt.xticks(rotation=45)
    plt.savefig('热词排行榜.jpg')
    plt.show()

if __name__ == '__main__':
    # need_words = open("过滤词.txt", encoding="utf-8").read()  # 这个是要查找的词的txt文件 每个词一行
    # find = need_words.split()
    # cut_words()
    cl_csv()
