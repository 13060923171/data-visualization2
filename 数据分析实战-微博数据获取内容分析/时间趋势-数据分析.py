import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('情感_离婚冷静期.csv')
df['数量'] = 1

def time1(x):
    x1 = str(x).split('日')
    x1 = x1[0] + '日'
    return x1

df['时间'] = df['时间'].apply(time1)
df['时间'] = pd.to_datetime(df['时间'],format='%Y年%m月%d日')
df.index = df['时间']

df = df[df['认证'] != '微博官方认证']



#时间趋势
def main1():
    new_df = df['数量'].resample('W').sum()
    x_data = [str(n).split(" ")[0] for n in new_df.index]
    y_data = list(new_df.values)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(16, 9),dpi=300)
    plt.plot(x_data,y_data,color='#b82410')
    plt.title("时间热度趋势")
    plt.xlabel("时间")
    plt.ylabel("发帖数量")
    plt.xticks(rotation=65)
    plt.savefig('./数据可视化-无官方干预/发帖热度时间趋势图.png')
    plt.show()

#查看家暴的时间趋势变化
def main2():
    df1 = df[df['分类结果'] == '家暴']
    new_df = df1['数量'].resample('W').sum()
    new_df = new_df.sort_index()
    x_data = [str(n).split(" ")[0] for n in new_df.index]
    y_data = list(new_df.values)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(16, 9), dpi=300)
    plt.plot(x_data, y_data, color='#873600',label='家暴')
    plt.legend()
    plt.title("家暴-时间热度变化趋势")
    plt.xlabel("时间")
    plt.ylabel("发帖数量")
    plt.xticks(rotation=65)
    plt.savefig('./数据可视化-无官方干预/家暴-时间热度变化趋势.png')
    plt.show()


#查看性别对立的时间趋势变化
def main3():
    df2 = df[df['分类结果'] == '性别对立']
    new_df1 = df2['数量'].resample('W').sum()
    new_df1 = new_df1.sort_index()
    x_data1 = [str(n).split(" ")[0] for n in new_df1.index]
    y_data1 = list(new_df1.values)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(16, 9), dpi=300)
    plt.plot(x_data1, y_data1, color='#117A65', label='性别对立')
    plt.legend()
    plt.title("性别对立-时间热度变化趋势")
    plt.xlabel("时间")
    plt.ylabel("发帖数量")
    plt.xticks(rotation=65)
    plt.savefig('./数据可视化-无官方干预/性别对立-时间热度变化趋势.png')
    plt.show()


#查看女性不平等的时间趋势变化
def main4():
    df3 = df[df['分类结果'] == '女性不平等']
    new_df2 = df3['数量'].resample('W').sum()
    new_df2 = new_df2.sort_index()
    x_data2 = [str(n).split(" ")[0] for n in new_df2.index]
    y_data2 = list(new_df2.values)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(16, 9), dpi=300)
    plt.plot(x_data2, y_data2, color='#6C3483', label='女性不平等')
    plt.legend()
    plt.title("女性不平等-时间热度变化趋势")
    plt.xlabel("时间")
    plt.ylabel("发帖数量")
    plt.xticks(rotation=65)
    plt.savefig('./数据可视化-无官方干预/女性不平等-时间热度变化趋势.png')
    plt.show()


#查看情感变化的时间趋势变化
def main5():
    df3 = df[df['情感分值'] == '非负']
    new_df2 = df3['数量'].resample('W').sum()
    new_df2 = new_df2.sort_index()
    x_data2 = [str(n).split(" ")[0] for n in new_df2.index]
    y_data2 = list(new_df2.values)

    df4 = df[df['情感分值'] == '负面']
    new_df3 = df4['数量'].resample('W').sum()
    new_df3 = new_df3.sort_index()
    x_data3 = [str(n).split(" ")[0] for n in new_df3.index]
    y_data3 = list(new_df3.values)

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(16, 9), dpi=300)
    plt.plot(x_data2, y_data2, color='#148F77', label='非负')
    plt.plot(x_data3[1:], y_data3[1:], color='#922B21', label='负面')
    plt.legend()
    plt.title("情感倾向-时间热度变化趋势")
    plt.xlabel("时间")
    plt.ylabel("情感数量")
    plt.xticks(rotation=65)
    plt.savefig('./数据可视化-无官方干预/情感倾向-时间热度变化趋势.png')
    plt.show()


#点赞趋势
def main6():
    new_df = df['点赞'].resample('W').sum()
    x_data = [str(n).split(" ")[0] for n in new_df.index]
    y_data = list(new_df.values)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(16, 9),dpi=300)
    plt.plot(x_data,y_data,color='#b82410')
    plt.title("点赞热度趋势")
    plt.xlabel("时间")
    plt.ylabel("发帖数量")
    plt.xticks(rotation=65)
    plt.savefig('./数据可视化-无官方干预/点赞热度时间趋势图.png')
    plt.show()

#评论趋势
def main7():
    new_df = df['评论'].resample('W').sum()
    x_data = [str(n).split(" ")[0] for n in new_df.index]
    y_data = list(new_df.values)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(16, 9),dpi=300)
    plt.plot(x_data,y_data,color='#b82410')
    plt.title("评论热度趋势")
    plt.xlabel("时间")
    plt.ylabel("发帖数量")
    plt.xticks(rotation=65)
    plt.savefig('./数据可视化-无官方干预/评论热度时间趋势图.png')
    plt.show()

#转发趋势
def main8():
    new_df = df['转发'].resample('W').sum()
    x_data = [str(n).split(" ")[0] for n in new_df.index]
    y_data = list(new_df.values)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(16, 9),dpi=300)
    plt.plot(x_data,y_data,color='#b82410')
    plt.title("转发热度趋势")
    plt.xlabel("时间")
    plt.ylabel("发帖数量")
    plt.xticks(rotation=65)
    plt.savefig('./数据可视化-无官方干预/转发热度时间趋势图.png')
    plt.show()

if __name__ == '__main__':
    main1()
    main2()
    main3()
    main4()
    main5()
    main6()
    main7()
    main8()
