# 导入词云制作库wordcloud和中文分词库jieba
import os
import time
from collections import Counter

import jieba
import wordcloud

# 导入imageio库中的imread函数，并用这个函数读取本地图片，作为词云形状图片
import imageio



def gen_word_cloud(img_path, txt_path):
    """结合图片和文本文档路径，生成词云图"""
    #首先我们读取停用词表的内容，设置为集合数据结构,添加停用词：stopwords.add('luopan')
    stopwords = set()
    content = [line.strip() for line in open('demo/data/中文停用词.txt', 'r', encoding='utf-8').readlines()]
    stopwords.update(content)

    # 读取本地的原始图片 chinamap.png （词云对象背景层）
    mk = imageio.imread(img_path)

    # 构建并配置词云对象w，注意要加scale参数，提高清晰度
    w = wordcloud.WordCloud(width=1000,  #词云对象生成的图片宽度，默认为400px
                            height=700,  #词云对象生成的图片高度，默认为200px
                            background_color='white',  #指定词云图片的背景颜色，默认为黑色
                            font_path='msyh.ttc',  #指定字体文件（otf或ttf格式后缀），默认字体为DroidSansMono，无法用于展示中文
                            mask=mk,  #定词云的形状，默认为长方形，通过imageio.imread方法手动指定
                            scale=15,  #定词云图的缩放倍数，默认为1，倍数越大图像越清晰，图像尺寸也会越大
                            stopwords=stopwords)

    # 对来自外部文件的文本进行中文分词，得到string
    print("正在对文本内容进行分词...")
    # jieba分词模块，首先需要读取新闻内容，作为接下来进行分词的对象
    with open(txt_path, encoding='utf-8') as f:
        txt = f.read()
    #获取到的新闻内容读取到名为txt的对象中
    #jieba.lcut方法，此方法会直接生成一个列表，列表中的每个元素对应分词后的每一个词。
    txtlist = jieba.lcut(txt)
    #分词后的列表，空格拼接成一个长字符串，这也是稍后生成词云图所需要的参数格式
    string = " ".join(txtlist)

    #分词后文本存储
    f = open('demo/data/新闻分词后.txt', 'w', encoding='utf-8')
    f.write(string)
    f.close()

    all_words = string.split()
    #print(all_words)
    # 词频统计
    c = Counter()
    for x in all_words:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    # 输出词频最高的前10个词
    print('\n词频统计结果：')
    for (k, v) in c.most_common(10):
        print("%s:%d" % (k, v))
    #存储高频词 CSV
    # name = time.strftime("%Y-%m-%d") + "-fc.csv"
    # fw = open(name, 'w', encoding='utf-8')
    # i = 1
    # for (k, v) in c.most_common(len(c)):
    #     fw.write(str(i) + ',' + str(k) + ',' + str(v) + '\n')
    #     i = i + 1
    # else:
    #     print("Over write file!")
    #     fw.close()

    # 将string变量传入w的generate()方法，给词云输入文字，此时，包含文本内容的词云对象
    w.generate(string)

    # 将词云图片导出到当前文件夹
    #本地的词云图文件并没有生成。想要将词云图生成到本地，
    # 需要执行词云对象的to_file方法，并指定词云图的输出路径
    export_pic = 'static/images/test1.png'
    print("正在生成词云图...")
    w.to_file(export_pic)

    print("词云图已成功生成！")
    return export_pic  #返回词云图的文件路径

if __name__ == "__main__":
    # 借助原始图像和新闻文档，执行生成词云图的操作
    export_pic = gen_word_cloud("demo/data/chinamap.png", "demo/data/top_news_content.txt")