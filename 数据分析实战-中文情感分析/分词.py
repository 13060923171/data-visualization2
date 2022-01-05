import jieba
import pandas as pd
import stylecloud
from IPython.display import Image 
comment = pd.read_excel('新浪微博评论采集.xlsx')


# 定义分词函数
def get_cut_words(content_series):
    # 读入停用词表
    stop_words = []

    with open("stopwords_cn.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())
    list_word = []
    # 分词
    word_num = jieba.lcut(content_series.str.cat(sep='。'), cut_all=False)

    # 条件筛选
    word_num_selected = [i for i in word_num if i not in stop_words and len(i) >= 2]
    return word_num_selected

def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

# 绘制词云图
text1 = get_cut_words(content_series=comment['评论内容'])
stylecloud.gen_stylecloud(text=' '.join(text1), max_words=100,
                          collocations=False,
                          font_path='simhei.ttf',
                          icon_name='fas fa-heart',
                          size=500,
                          #palette='matplotlib.Inferno_9',
                          output_name='热词-云图.png')
Image(filename='热词-云图.png')

# text1 = get_cut_words(content_series=comment['评论内容'])
#
# ditc = {}
# list_word = []
# list_count = []
# for t in text1:
#     ditc[t] = ditc.get(t, 0) + 1
# ls = list(ditc.items())
# ls.sort(key=lambda x: x[1], reverse=True)
# for i in range(len(ls)):
#     word, count = ls[i]
#     if is_all_chinese(word) == True:
#         list_word.append(word)
#         list_count.append(count)
#
#
# df1 = pd.DataFrame()
# df1['word'] = list_word
# df1['count'] = list_count
# df1.to_csv('高频词.csv',encoding='gbk')