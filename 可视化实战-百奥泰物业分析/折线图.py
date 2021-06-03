import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
#股票
def main1():
    time1 = ['2020.3','2020.6','2020.9']
    title1 = ['基本每股收益','每股净资产','每股资本公积','每股未分配利润']
    list1 = ['-0.28','-0.34','-0.28']
    list2 = ['5.83','5.49','5.21']
    list3 = ['7.38','7.38','7.38']
    list4 = ['-2.55','-2.88','-3.17']
    plt.title('每股指标')  # 折线图标题
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
    plt.xlabel('时间')  # x轴标题
    plt.ylabel('指标')  # y轴标题
    plt.plot(time1, list1,marker='o')  # 绘制折线图，添加数据点，设置点的大小
    plt.plot(time1, list2, marker='o', markersize=3)
    plt.plot(time1, list3, marker='o', markersize=3)
    plt.plot(time1, list4, marker='o', markersize=3)

    for a, b in zip(time1, list1):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  # 设置数据标签位置及大小
    for a, b in zip(time1,list2):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    for a, b in zip(time1, list3):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    for a, b in zip(time1, list4):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

    plt.legend(title1)  # 设置折线名称
    plt.title('每股指标-折线图')
    plt.savefig('折线1.jpg')
    plt.show()  # 显示折线图


#运营能力
def main2():
    time2 = ['2020.3','2020.6','2020.9']
    title2 = ['存货周转率','应收账款周转天数']
    list5 = ['1520.43','1253.09','1167.44']
    list6 = ['1447.83','1194.43','1092.23']

    plt.title('每股指标')  # 折线图标题
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
    plt.xlabel('时间')  # x轴标题
    plt.ylabel('指标')  # y轴标题
    plt.plot(time2, list5, marker='o', markersize=3)  # 绘制折线图，添加数据点，设置点的大小
    plt.plot(time2, list6, marker='o', markersize=3)

    for a, b in zip(time2, list5):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  # 设置数据标签位置及大小
    for a, b in zip(time2, list6):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

    plt.legend(title2)  # 设置折线名称
    plt.title('运营能力-折线图')
    plt.savefig('运营能力2.jpg')
    plt.show()  # 显示折线图


#偿债能力
def main3():
    time3 = ['2020.3', '2020.6', '2020.9']
    title3 = ['基本每股收益', '每股净资产', '每股资本公积', '每股未分配利润']
    list7 = ['5.62', '5.77', '6.92']
    list8 = ['5.16', '5.27', '6.18']
    list9 = ['5.16', '5.27', '6.18']
    list10 = ['0.14', '0.13', '0.1']

    plt.title('偿债能力')  # 折线图标题
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
    plt.xlabel('时间')  # x轴标题
    plt.ylabel('指标')  # y轴标题
    plt.plot(time3, list7, marker='o', markersize=3)  # 绘制折线图，添加数据点，设置点的大小
    plt.plot(time3, list8, marker='o', markersize=3)
    plt.plot(time3, list9, marker='o', markersize=3)
    plt.plot(time3, list10, marker='o', markersize=3)

    for a, b in zip(time3, list7):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  # 设置数据标签位置及大小
    for a, b in zip(time3, list8):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    for a, b in zip(time3, list9):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
    for a, b in zip(time3, list10):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

    plt.legend(title3)  # 设置折线名称
    plt.title('偿债能力-折线图')
    plt.savefig('偿债能力3.jpg')
    plt.show()  # 显示折线图

if __name__ == '__main__':
    main1()
    main2()
    main3()