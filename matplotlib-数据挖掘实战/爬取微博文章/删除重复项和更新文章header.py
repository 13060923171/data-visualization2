import re


def clearBlankLine():
    # 读入停用词表
    stop_words = []
    with open("stopwords_cn.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip())
    my_stop_words = ['#', ':', '@', '[超话]', '“', '”','"','{','}','性别','内容']
    stop_words.extend(my_stop_words)
    word1 = []
    for i in range(0, 10000):
        i = str(i)
        word1.append(i)
    stop_words.extend(word1)
    lines_seen = set()
    file1 = open('宝矿力微信评论信息.txt', 'r',encoding="utf-8",errors='ignore') # 要去掉空行的文件
    file2 = open('(新)宝矿力微信评论信息.txt', 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            l = re.compile('#(.*?)#')
            lines = l.findall(line)
            for i in lines:
                line = line.replace(i,'')
            k = re.compile('[(.*?)]')
            lines = k.findall(line)
            for i in lines:
                line = line.replace(i, '')
            j = re.compile('【(.*?)】')
            lines = j.findall(line)
            for i in lines:
                line = line.replace(i, '')
            # for s in stop_words:
            #     line = line.replace(s,'')
            line = line.split(',')[-1]
            line = line.replace(':','').replace('#','').strip(" ").replace('{','').replace('}','').replace('】','').replace('【','')\
                .replace('"','').replace('性别','').replace('内容','').replace(' ','')
            line = line.strip("\n")
            if line not in lines_seen and '宝矿力' in line:
                file2.write(line+"\n")
                lines_seen.add(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine()