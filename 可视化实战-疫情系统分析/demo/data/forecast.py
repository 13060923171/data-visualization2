from datetime import time
from io import BytesIO

import numpy as np
import matplotlib.pyplot as plt
import math

import openpyxl
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import curve_fit
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def logistic_increase_function(t, K, P0, r):
    t0 = 20
    # r 中国0.25 美国0.05 英国0.08 意大利0.08 德国0.09 韩国0.11
    r = 0.05
    # t:time   t0:initial time    P0:initial_value    K:capacity  r:increase_rate
    exp_value = np.exp(r * (t - t0))
    return (K * exp_value * P0) / (K + (exp_value - 1) * P0)

def nihe():
    # 日期及感染人数
    '''
    1.11日41例
    1.18日45例
    1.19日62例
    1.20日291例
    1.21日440例
    1.22日571例
    1.23日830例
    1.24日1287例
    1.25日1975例
    1.26日2744例
    1.27日4515例
    '''

    #  日期及感染人数
    t = [11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    t = np.array(t)
    P = [41, 45, 62, 291, 440, 571, 830, 1287, 1975, 2744, 4515]
    P = np.array(P)

    # 用最小二乘法估计拟合
    # 现有数据曲线拟合检验
    popt1, pcov1 = curve_fit(logistic_increase_function, t, P)

    # 获取popt里面是拟合系数
    print("K:capacity  P0:initial_value   r:increase_rate   t:time")
    print(popt1)
    # 拟合后预测的P值

    P_predict = logistic_increase_function(t, popt1[0], popt1[1], popt1[2])
    # 未来预测
    future = [11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 41, 51, 61, 71, 81, 91, 101]
    future = np.array(future)
    future_predict = logistic_increase_function(future, popt1[0], popt1[1], popt1[2])

    # 近期情况预测
    tomorrow = [28, 29, 30, 32, 33, 35, 37, 40]
    tomorrow = np.array(tomorrow)
    tomorrow_predict = logistic_increase_function(tomorrow, popt1[0], popt1[1], popt1[2])
    # 绘图
    plot1 = plt.plot(t, P, 's', label="confimed infected people number")
    plot2 = plt.plot(t, P_predict, 'r', label='predict infected people number')
    plot3 = plt.plot(tomorrow, tomorrow_predict, 's', label='tomorrow predict infected people number')
    plt.xlabel('time')

    plt.ylabel('confimed infected people number')

    plt.legend(loc=0)  # 指定legend的位置右下角

    print(logistic_increase_function(np.array(28), popt1[0], popt1[1], popt1[2]))
    print(logistic_increase_function(np.array(29), popt1[0], popt1[1], popt1[2]))
    plt.show()

def chinaforcast():
    n = r"demo/data/国内历史疫情.xlsx"
    # data = pd.read_excel(n)
    # 修改国家可以得到不同的曲线拟合情况
    # data = data[data['countryName'] == '日本']
    wb = openpyxl.load_workbook(n)  # 获取已有的xlsx文件
    ws_data = wb['Sheet1']  # 获取文件中中国省份疫情数据表
    ws_data.delete_rows(1)  # 删除第一行
    date_list = []  # 时间
    confirm_list = []  # 累计确诊
    # 获取表数据
    for data in ws_data.values:
        date_list.append(data[4]+19)  #count+19 = 20 取日期还是编号无所谓
        confirm_list.append(data[0])
    # date_list = data['date']
    print(date_list)
    date_list = list(map(lambda x: str(x), date_list))  # lambda函数，将date_list对象转为字符串

    # confirm_list = data['confirm']
    print(confirm_list)
    #将数据转化为矩阵

    #time_array1 = np.array(date_list)

    time_array = np.array(range(20, len(date_list) + 20))
    long_time_array = np.array(range(20, len(date_list) + 200))
    confirm_array = np.array(confirm_list)
    #print(time_array)
    #print(long_time_array)
    #print(time_array1 )
    # 用最小二乘法估计拟合

    # 现有数据曲线拟合预测
    popt, pcov = curve_fit(logistic_increase_function, time_array, confirm_array)
    # popt, pcov = curve_fit(funl, x, y,bounds=(0, [80, 24., 0.2]))
    # 获取popt里面是拟合系数
    print("K:capacity  P0:initial_value   r:increase_rate   t:time")
    print(popt)
    # 拟合后预测的P值
    P_predict = logistic_increase_function(long_time_array, popt[0], popt[1], popt[2])

    # 未来预测

    # 近期情况预测

    # 绘图
    plot1 = plt.plot(time_array, confirm_array, 's', label="confimed infected people number")
    plot2 = plt.plot(long_time_array, P_predict, 'r', label='predict infected people number')
    plt.xlabel('time')
    plt.ylabel('confimed infected people number')

    plt.legend(loc=0)  # 指定legend的位置右下角

    print(logistic_increase_function(np.array(28), popt[0], popt[1], popt[2]))
    print(logistic_increase_function(np.array(29), popt[0], popt[1], popt[2]))

    #plt.show()
    return plt

if __name__ == "__main__":
    #测试
    #nihe ()
    chinaforcast().show()
