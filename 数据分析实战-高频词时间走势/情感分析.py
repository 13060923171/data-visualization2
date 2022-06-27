import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df = pd.read_csv('./output/情感分布计算.csv')


def time_qx(x):
    x = str(x)
    x = x.split(" ")
    x = x[0].split("-")
    x = x[0] + "-" + x[1]
    return x


df['发文时间'] =  df['发文时间'].apply(time_qx)


def main1(number):
    df1 = df[df['聚类结果'] == number]
    def score_total(x):
        df = x
        df1 = df['comp_score'].value_counts()
        data = [(j,int(k)) for j,k in zip(df1.index,df1.values)]
        if len(data) == 3:
            data.sort(key=lambda x:x[0],reverse=True)
            return data
        else:
            return np.NaN
    new_df = df1.groupby('发文时间').apply(score_total)
    new_df = new_df.dropna(how='any',axis=0)

    x_data = [x for x in new_df.index]
    y_data1 = [y for y in new_df.values]
    pos_list = []
    neu_list = []
    neg_list = []
    for y in y_data1:
        pos_list.append(y[0][1])
        neu_list.append(y[1][1])
        neg_list.append(y[2][1])

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(20,9),dpi=300)
    plt.plot(x_data, pos_list, '*--',color='#E74C3C', label='积极')
    plt.plot(x_data, neu_list, '^--',color='#F1C40F', label='中立')
    plt.plot(x_data, neg_list, 'o--',color='#34495E', label='消极')
    plt.legend()
    plt.title('聚类{}情感走势'.format(number))
    plt.grid()
    plt.xticks(rotation=65)
    plt.savefig('./output/聚类{}情感走势.png'.format(number))
    plt.show()


if __name__ == '__main__':
    main1(0)
    main1(1)
    main1(2)