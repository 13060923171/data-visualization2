# -*- coding: utf-8 -*-
import jieba
import sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud



# 结巴分词 cut_all=True 设置为精准模式
wordlist = jieba.cut(text, cut_all=False)

# 使用空格连接 进行中文分词
wl_space_split = " ".join(wordlist)
print(wl_space_split)

# 对分词后的文本生成词云
my_wordcloud = WordCloud().generate(wl_space_split)

# 显示词云图
plt.imshow(my_wordcloud)
# 是否显示x轴、y轴下标
plt.axis("off")
plt.show()