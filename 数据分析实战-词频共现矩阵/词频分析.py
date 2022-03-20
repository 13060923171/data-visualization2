# coding=utf-8
import jieba
import re
import time
from collections import Counter
from snownlp import SnowNLP
import pandas as pd
import jieba.posseg as pseg


def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True


def n_word():
    stop_words = []
    with open("stopwords_cn.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())
    counts = {}
    f = open('评价要素.txt', 'w', encoding='utf-8')
    df = pd.read_excel('携程酒店评价.xlsx')
    content = df['评价内容']

    for line in content:
        line = line.strip('\n')
        # 停用词过滤
        line = re.sub('[0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", line)
        words = pseg.cut("{}".format(line))
        c = Counter()

        for word, flag in words:
            if word not in stop_words and len(word) >= 1 and word != '\r\n':
                if is_all_chinese(word) == True:
                    if 'n' == flag:
                        print(word,flag)
                        c[word] += 1
                        counts[word] = counts.get(word, 0) + 1

        # Top50
        output = ""
        # print('\n词频统计结果：')
        for (k, v) in c.items():
            # print("%s:%d"%(k,v))
            output += k + " "

        f.write(output + "\n")
    else:
        f.close()

    df1 = pd.DataFrame()
    list_word = []
    list_count = []
    ls = list(counts.items())
    ls.sort(key=lambda x: x[1], reverse=True)
    for i in ls[:100]:
        word = i[0]
        count = i[1]
        list_word.append(word)
        list_count.append(count)

    df1['word'] = list_word
    df1['count'] = list_count
    df1.to_csv('评论要素词频统计top100.csv',encoding='gbk')


def a_word():
    stop_words = []
    with open("stopwords_cn.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())
    counts = {}
    f = open('情感倾向.txt', 'w', encoding='utf-8')
    df = pd.read_excel('携程酒店评价.xlsx')
    content = df['评价内容']

    for line in content:
        line = line.strip('\n')
        # 停用词过滤
        line = re.sub('[0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", line)
        words = pseg.cut("{}".format(line))
        c = Counter()

        for word, flag in words:
            if word not in stop_words and len(word) >= 1 and word != '\r\n':
                if is_all_chinese(word) == True:
                    if 'a' in flag or 'A' in flag:
                        c[word] += 1
                        counts[word] = counts.get(word, 0) + 1

        # Top50
        output = ""
        # print('\n词频统计结果：')
        for (k, v) in c.items():
            # print("%s:%d"%(k,v))
            output += k + " "

        f.write(output + "\n")
    else:
        f.close()

    df1 = pd.DataFrame()
    list_word = []
    list_count = []
    ls = list(counts.items())
    ls.sort(key=lambda x: x[1], reverse=True)
    for i in ls[:100]:
        word = i[0]
        count = i[1]
        list_word.append(word)
        list_count.append(count)

    df1['word'] = list_word
    df1['count'] = list_count
    df1.to_csv('情感倾向词频统计top100.csv',encoding='gbk')


if __name__ == '__main__':
    n_word()
    a_word()
