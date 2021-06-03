import jieba
from wordcloud import WordCloud, STOPWORDS
from imageio import imread

with open("标题.txt", "r", encoding="utf8") as f:
    contents = f.read()
print("contents变量的类型：", type(contents))

# 使用jieba分词，获取词的列表
contents_cut = jieba.cut(contents)
print("contents_cut变量的类型：", type(contents_cut))
contents_list = " ".join(contents_cut)
print("contents_list变量的类型：", type(contents_list))

# 制作词云图，collocations避免词云图中词的重复，mask定义词云图的形状，图片要有背景色
wc = WordCloud(stopwords=STOPWORDS.add("一个"), collocations=False,
               background_color="white",
               font_path=r"C:\Windows\Fonts\simhei.ttf",
               width=1080, height=1920, random_state=42,
               mask=imread('sample.jpg', pilmode="RGB"))
wc.generate(contents_list)
# 要读取的形状的图片
wc.to_file("词云图.jpg")