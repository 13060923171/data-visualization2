import jieba
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
from pyecharts.charts import Map,Timeline

name = ['陈桥兵变', '雍熙北伐', '庆历新政', '王安石变法', '靖康之变', '建炎南渡', '绍兴和议', '隆兴北伐', '襄樊之战', '崖山海战']

def mechanical_compress():
    sum_list = []
    for n in name:
        with open('./data/{}.txt'.format(n),'r',encoding='utf-8')as f:
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
        sum_list.append(filelist2)

    return sum_list


def fenchi_test(s):
    d = {}
    stop_words = []
    with open("./data/stopwords_cn.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())
    word1 = ['960']
    stop_words.extend(word1)
    fenchi = jieba.lcut(s, cut_all=False)
    for f in fenchi:
        if f not in stop_words and len(f) >= 2:
            d[f] = d.get(f, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[1], reverse=True)
    ls = ls[:50]
    return ls

def data_cleansing():
    sum_list = mechanical_compress()
    total = []
    for sum in sum_list:
        s = " ".join(sum)
        ls = fenchi_test(s)
        total.append(ls)
    return total


def wordcloud_hot():
    total = data_cleansing()
    tl = Timeline()
    for i in range(10):
        c = (
                WordCloud(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
                .add(
                        "",
                        total[i],
                        word_size_range=[20, 100],
                        shape=SymbolType.DIAMOND,
                        textstyle_opts=opts.TextStyleOpts(font_family="cursive"), )
                .set_global_opts(title_opts=opts.TitleOpts(
                    pos_left="center",
                    pos_top="top"
                ))
            )
        tl.add(c, "{}".format(name[int(i)]))
        tl.add_schema(
            orient="vertical",
            is_auto_play=True,
            is_inverse=True,
            play_interval=3000,
            pos_left="5",
            pos_right="null",
            pos_top="20",
            pos_bottom="20",
            width="50",
            label_opts=opts.LabelOpts(is_show=True, color="#fff"),
        )
    return tl





