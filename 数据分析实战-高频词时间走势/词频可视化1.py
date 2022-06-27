import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('./output/聚类结果.csv')

def time_qx(x):
    x = str(x)
    x = x.split(" ")
    x = x[0].split("-")
    x = x[0] + "-" + x[1]
    return x


def comment_total(x):
    x = str(x).split(" ")
    return len(x)


df = df.dropna(subset=['comment'])
df['发文时间'] =  df['发文时间'].apply(time_qx)
df['长度'] = df['comment'].apply(comment_total)

def main1(number,color=None):
    df1 = df[df['聚类结果'] == number]
    new_df = df1.groupby('发文时间').agg('sum')
    x_data = [x for x in new_df.index]
    y_data = [y for y in new_df['长度']]

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(20,9),dpi=300)
    plt.plot(x_data, y_data,'*--',linewidth=5,color=color)
    plt.title('聚类{}频次走势'.format(number))
    plt.grid()
    plt.xticks(rotation=65)
    plt.savefig('./output/聚类{}频次走势.png'.format(number))
    plt.show()


if __name__ == '__main__':
    main1(0,color='#5DADE2')
    main1(1,color='#34495E')
    main1(2,color='#F7DC6F')
