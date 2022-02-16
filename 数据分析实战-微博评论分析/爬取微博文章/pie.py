import re
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']

def clearBlankLine():
    file1 = open('宝矿力微信评论信息.txt', 'r',encoding="utf-8",errors='ignore') # 要去掉空行的文件
    sum_list = []
    for line in file1.readlines():
        line = line.split(',')[0]
        sum_list.append(line)
    d = {}
    for s in sum_list:
        d[s] = d.get(s,0)+1
    x_data = ['男','女']
    y_data = [1386,3143]
    pie_main(x_data,y_data)

def pie_main(x_data,y_data):
    plt.figure(figsize=(6, 9))  # 调节图形大小
    labels = x_data  # 定义标签
    sizes = y_data  # 每块值
    colors = ['midnightblue', 'steelblue']  # 每块颜色定义
    explode = (0, 0.2)  # 将某一块分割出来，值越大分割出的间隙越大
    patches, text1, text2 = plt.pie(sizes,
                                    explode=explode,
                                    labels=labels,
                                    colors=colors,
                                    labeldistance=1.2,  # 图例距圆心半径倍距离
                                    autopct='%3.2f%%',  # 数值保留固定小数位
                                    shadow=False,  # 无阴影设置
                                    startangle=90,  # 逆时针起始角度设置
                                    pctdistance=0.6)  # 数值距圆心半径倍数距离
    # patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部文本
    # x，y轴刻度设置一致，保证饼图为圆形
    plt.axis('equal')
    plt.legend()
    plt.title('宝矿力-水特男女占比')
    plt.savefig('test1.jpg')
    plt.show()



if __name__ == '__main__':
    clearBlankLine()