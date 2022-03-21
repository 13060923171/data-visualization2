import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']


def pie1():
    df = pd.read_excel('行为消费数据.xlsx')
    content = df['3、你过去3个月是否曾经在网络上购买东西？'].value_counts()
    x_data = list(content.index)
    y_data = list(content.values)


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
    plt.title('在过去3个月是否曾经在网络上购买东西占比图')
    plt.savefig('3个月是否曾经在网络上购买东西占比图.jpg')
    plt.show()


def bar1():
    df = pd.read_excel('行为消费数据.xlsx')
    content = df['4、你选择网络购物的主要原因是？']
    def qg(x):
        x = str(x)
        x = x.split("┋")
        return x
    content = content.apply(qg)
    counts = {}
    for c in content:
        for i in c:
            counts[i] = counts.get(i, 0) + 1
    x_data = []
    y_data = []
    counts = list(counts.items())
    counts.sort(key=lambda x: x[1], reverse=True)

    for key, values in counts:
        x_data.append(key)
        y_data.append(values)

    plt.figure(figsize=(12, 9))
    plt.bar(x_data, y_data)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("网购的主要原因")
    plt.xticks(rotation=30)
    plt.savefig('网购的主要原因柱状图.jpg')
    plt.show()

def bar2():
    df = pd.read_excel('行为消费数据.xlsx')
    content = df['5、你在网上主要购买哪些东西？']

    def qg(x):
        x = str(x)
        x = x.split("┋")
        return x

    content = content.apply(qg)
    counts = {}
    for c in content:
        for i in c:
            counts[i] = counts.get(i, 0) + 1
    x_data = []
    y_data = []
    counts = list(counts.items())
    counts.sort(key=lambda x:x[1],reverse=True)

    for key, values in counts:
        x_data.append(key)
        y_data.append(values)

    x_data.reverse()
    y_data.reverse()
    plt.figure(figsize=(12, 9))
    plt.barh(x_data, y_data,color='#1ABC9C')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("主要购买物品")
    plt.xticks(rotation=30)
    plt.savefig('主要购买柱状图.jpg')
    plt.show()

def leida():
    df = pd.read_excel('行为消费数据.xlsx')
    content = df['11、网购在日常消费中占比大概多少'].value_counts()
    x_data = list(content.index)
    y_data = list(content.values)
    plt.figure(figsize=(12, 9))  # 调节图形大小
    labels = x_data  # 定义标签
    sizes = y_data  # 每块值
    colors = ['#17A589', '#16A085','#2ECC71']  # 每块颜色定义
    explode = (0, 0.1,0)  # 将某一块分割出来，值越大分割出的间隙越大
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
    plt.title('日常消费中占比图')
    plt.savefig('日常消费中占比.jpg')
    plt.show()


def line1():
    df = pd.read_excel('行为消费数据.xlsx')
    content = df['14、网购过程，你最担心的因素是？'].value_counts()
    x_data = list(content.index)
    y_data = list(content.values)
    x_data.reverse()
    y_data.reverse()
    plt.figure(figsize=(12, 9))
    plt.plot(x_data, y_data,linewidth=5)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("最担心的因素")
    plt.xticks(rotation=30)
    plt.savefig('最担心的因素.jpg')
    plt.show()


def line2():
    df = pd.read_excel('行为消费数据.xlsx')
    content = df['15、总体而言，你对网购是否满意？'].value_counts()
    x_data = list(content.index)
    y_data = list(content.values)
    x_data.reverse()
    y_data.reverse()
    plt.figure(figsize=(12, 9))
    plt.plot(x_data, y_data,color='#1ABC9C',linewidth=5)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("网购满意程度")
    plt.xticks(rotation=30)
    plt.savefig('网购满意程度.jpg')
    plt.show()

if __name__ == '__main__':
    pie1()
    bar1()
    bar2()
    leida()
    line1()
    line2()