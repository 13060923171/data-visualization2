import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('new_深圳疫情.csv')
df1 = df1.drop(['博主','认证'],axis=1)
df2 = pd.read_csv('深圳微博发布厅.csv')
df3 = pd.read_csv('深圳卫健委.csv')

data = pd.concat([df1,df2,df3],axis=0)

data['数量'] = 1

def time1(x):
    x = str(x)
    x1 = str(x).split('日')
    x1 = '2022年' + x1[0] + '日'
    return x1

data['时间'] = data['时间'].apply(time1)
data['时间'] = pd.to_datetime(data['时间'],format='%Y年%m月%d日')
data.index = data['时间']

#时间趋势
def main1():
    new_df = data['数量'].resample('D').sum()
    x_data = [str(n).split(" ")[0] for n in new_df.index]
    y_data = list(new_df.values)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(16, 9),dpi=300)
    plt.plot(x_data,y_data,linewidth=3,color='#EC7063')
    plt.title("时间热度趋势")
    plt.xlabel("时间")
    plt.ylabel("发帖数量")
    plt.xticks(rotation=65)
    plt.savefig('./深圳数据可视化/发帖热度时间趋势图.png')
    plt.show()


#点赞趋势
def main2():
    new_df = data['点赞'].resample('D').sum()
    x_data = [str(n).split(" ")[0] for n in new_df.index]
    y_data = list(new_df.values)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(16, 9),dpi=300)
    plt.bar(x_data,y_data,color='#b82410')
    plt.title("点赞热度趋势")
    plt.xlabel("时间")
    plt.ylabel("点赞数量")
    plt.xticks(rotation=65)
    plt.savefig('./深圳数据可视化/点赞热度时间趋势图.png')
    plt.show()

#评论趋势
def main3():
    new_df = data['评论'].resample('D').sum()
    x_data = [str(n).split(" ")[0] for n in new_df.index]
    y_data = list(new_df.values)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(16, 9),dpi=300)
    plt.barh(x_data,y_data,color='#3498DB')
    plt.title("评论热度趋势")
    plt.xlabel("评论数量")
    plt.ylabel("时间")
    # plt.xticks(rotation=65)
    plt.savefig('./深圳数据可视化/评论热度时间趋势图.png')
    plt.show()

#转发趋势
def main4():
    new_df = data['转发'].resample('D').sum()
    x_data = [str(n).split(" ")[0] for n in new_df.index]
    y_data = list(new_df.values)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(16, 9),dpi=300)
    plt.plot(x_data,y_data, linewidth=3,color='#DAF7A6')
    plt.title("转发热度趋势")
    plt.xlabel("时间")
    plt.ylabel("转发数量")
    plt.xticks(rotation=65)
    plt.savefig('./深圳数据可视化/转发热度时间趋势图.png')
    plt.show()


if __name__ == '__main__':
    main1()
    main2()
    main3()
    main4()

