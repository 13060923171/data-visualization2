from snownlp import SnowNLP
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
def mechanical_compress():
    with open('(新)宝矿力微信评论信息.txt','r',encoding='utf-8')as f:
        content = f.readlines()

    filelist2 = []

    for a_string in content:
        temp1 = a_string.strip('\n')
        temp2 = temp1.lstrip('\ufeff')
        temp3 = temp2.strip('\r')
        char_list = list(temp3)  # 把字符串转化列表自动按单个字符分词了


        list1 = []
        list1.append(char_list[0])
        list2 = ['']

        # 记录要删除的索引
        del1 = []
        i = 0
        while (i < len(char_list)):
            i = i + 1
            # 这里是对后面没有词汇的时候对列表1和列表2判断一次重复
            if i == len(char_list):
                if list1 == list2:
                    m = len(list2)
                    for x in range(i - m, i):
                        del1.append(x)
            else:

                if char_list[i] == list1[0] and list2 == ['']:

                    list2[0] = char_list[i]  # 这里初始化用append会让lisr2初始化为['','**']
                elif char_list[i] != list1[0] and list2 == ['']:

                    list1.append(char_list[i])

                # 触发判断
                elif char_list[i] != list1[0] and list2 != ['']:
                    if list1 == list2 and len(list2) >= 2:

                        m = len(list2)
                        # 删除列表2里的内容，列表1本来的内容不用再去判断重复了
                        for x in range(i - m, i):
                            del1.append(x)
                        list1 = ['']
                        list2 = ['']
                        list1[0] = char_list[i]
                    else:

                        list2.append(char_list[i])

                # 触发判断
                elif char_list[i] == list1[0] and list2 != ['']:
                    if list1 == list2:

                        m = len(list2)
                        # 删除列表2里的内容，列表1需要再去和后面的词汇继续判断重复
                        for x in range(i - m, i):
                            del1.append(x)

                        list2 = ['']
                        list2[0] = char_list[i]
                    else:

                        # 逻辑对书本上进行了修改，书上是清空列表1和2，就是保留现在列表1和2内容不做删除，这里只保留1，列表2内容还需要做对比
                        list1 = list2
                        list2 = ['']
                        list2[0] = char_list[i]

        a = sorted(del1)  # 从数字更大的索引删起，这样就不用考虑元素删除后索引的变化问题
        t = len(a) - 1
        while (t >= 0):
            del char_list[a[t]]
            t = t - 1
        str1 = ''.join(char_list)
        str2 = str1.strip()
        filelist2.append(str2)

    return filelist2

def emotion_analyze():
    content = mechanical_compress()
    stop_words = []
    with open("stopwords_cn.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())

    sentimentslist = []
    for c in content:
        f = SnowNLP(c)
        print(str(f.sentiments)[0:3])
        sentimentslist.append(str(f.sentiments)[0:3])
    d = {}
    for l in sentimentslist:
        if float(l) <= 1:
            d[l] = d.get(l, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[0], reverse=False)
    x_data = []
    y_data = []
    for i in ls:
        x_data.append(i[0])
        y_data.append(i[1])

    plt.bar(x_data,y_data,facecolor='Crimson')
    plt.xlabel('Sentiments Probability')
    plt.ylabel('Quantity')
    plt.title('宝矿力情感趋势')
    plt.savefig('test2.jpg')
    plt.show()

if __name__ == '__main__':
    emotion_analyze()