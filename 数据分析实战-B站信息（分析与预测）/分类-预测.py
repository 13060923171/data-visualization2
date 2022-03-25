import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import confusion_matrix,precision_recall_curve
from sklearn.metrics import r2_score
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn import svm
import numpy as np
import seaborn as sns
df = pd.read_csv('top100.csv')

count = {}
for i in df['分类']:
    i = str(i).split(' ')
    for j in i:
        count[j] = count.get(j,0)+1

ls = list(count.items())
ls.sort(key=lambda x:x[1],reverse=True)

x1 = []
for key,value in ls:
    if len(key) ==2 and value >=1:
        x1.append(key)


def leibie(x):
    for j in x1:
        if j in x:
            return j


df['类别'] = df['分类'].apply(leibie)
le = LabelEncoder()
df['类别1'] = le.fit_transform(df['类别'])
df['排名'] = [i for i in range(1,101)]
def time_length(x):
    x = str(x).split(":")
    x1 = int(x[0]) * 60
    x2 = int(x[1])
    x3 = int(x1 + x2)
    return x3

df['时长'] = df['时长'].apply(time_length)
def fensi_number(x):
    x = str(x)
    if '万' in x:
        x = x.replace('万','')
        x = float(x) * 10000
        return int(x)
    elif str(x) == 'nan':
        return int(0)
    else:
        return int(x)
df['up粉丝数'] = df['up粉丝数'].apply(fensi_number)
df['点赞'] = df['点赞'].apply(fensi_number)
df['投币'] = df['投币'].apply(fensi_number)
df['收藏'] = df['收藏'].apply(fensi_number)
df['转发'] = df['转发'].apply(fensi_number)


def leibie_bar():
    x_data = []
    y_data = []
    for key, value in ls[0:10]:
        x_data.append(key)
        y_data.append(value)

    plt.style.use('ggplot')
    plt.figure(figsize=(12, 9),dpi=300)
    plt.bar(x_data, y_data)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("前10个最热门标签")
    plt.xlabel("标签")
    plt.ylabel("数量")
    plt.xticks(rotation=65)
    plt.savefig('前10个最热门标签.jpg')
    plt.show()

def barh_paiming():
    plt.style.use('ggplot')
    plt.figure(figsize=(12, 9), dpi=300)
    plt.bar(df['排名'], df['播放量'],color='#1ABC9C')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("播放量与排名关系")
    plt.xlabel("名称")
    plt.ylabel("播放量")
    plt.xticks(rotation=65)
    plt.savefig('播放量与排名关系.jpg')
    plt.show()

def heat_map():
    # 画热力图，看看哪些参数影响较大
    corr = df.corr()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(20, 15))
    sns.heatmap(corr, annot=True)
    plt.savefig('特征关系热力图.jpg')
    plt.show()

def fenlei_svm():
    data = df[['up粉丝数','收藏','播放量','弹幕量','评论数','时长','点赞','投币','转发']]
    target = df['类别1']
    # train_x, test_x, train_y, test_y = train_test_split(data, target, test_size=0.25)

    # 采用Min-Max规范化
    mm = preprocessing.MinMaxScaler()
    train_mm_x = mm.fit_transform(data)
    # test_mm_x = mm.transform(test_x)

    # 创建SVM分类器
    model1 = svm.SVC()
    # 用训练集做训练
    model1.fit(train_mm_x, target)
    # 用测试集做预测
    prediction1 = model1.predict(train_mm_x)
    return prediction1
    # df['视频类型-分类'] = prediction1


def yuce_ranking():
    data = df[['up粉丝数', '收藏', '播放量', '弹幕量', '评论数', '投币', '转发']]
    target = df['点赞']
    # train_x, test_x, train_y, test_y = train_test_split(data, target, test_size=0.25)
    # 采用Min-Max规范化
    mm = preprocessing.MinMaxScaler()
    train_mm_x = mm.fit_transform(data)
    # test_mm_x = mm.transform(test_x)
    # knn预测
    clf = KNeighborsRegressor()
    clf.fit(train_mm_x, target)
    # 预测排名
    predict_y = clf.predict(train_mm_x)
    # 算出它的正确率，正确率在77%算是较为高的比分
    score = r2_score(target, predict_y)
    print(score)
    return predict_y


if __name__ == '__main__':
    leibie_bar()
    barh_paiming()
    heat_map()
    prediction1 = fenlei_svm()
    prediction2 = yuce_ranking()
    df['视频类型-分类'] = prediction1
    df['视频点赞-预测'] = prediction2
    df.to_excel('new-top100视频信息.xlsx')