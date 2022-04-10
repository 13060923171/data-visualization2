import pandas as pd
import matplotlib.pyplot as plt
import paddlehub as hub
df = pd.read_csv('../data/疫情-处理好的文本.csv')


#疫情的微博数量变迁趋势
def number_change():
    new_df = df['time'].value_counts()
    new_df = new_df.sort_index(ascending=True)
    x_data = list(new_df.index)
    y_data = list(new_df.values)
    plt.figure(figsize=(9,6),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.style.use('ggplot')
    plt.plot(x_data,y_data,'o-',color='#b82410',linewidth=3)
    plt.title('疫情的微博数量变化趋势')
    plt.xlabel('时间')
    plt.ylabel('数量')
    plt.savefig('../data/疫情的微博数量变化趋势.png')
    plt.show()


#疫情的关注度变化趋势
def heat_change():
    data1 = df[['time','transmit','comment','praise']].groupby('time').sum()
    x_data = list(data1.index)
    y_data1 = list(data1['transmit'])
    y_data2 = list(data1['comment'])
    y_data3 = list(data1['praise'])

    plt.figure(figsize=(9, 6), dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.style.use('ggplot')
    plt.plot(x_data, y_data1, 'o-', color='#b82410', linewidth=2.5,label='转发')
    plt.plot(x_data, y_data2, '^-', color='#239B56', linewidth=2.5,label='评论')
    plt.plot(x_data, y_data3, '*-', color='#2E86C1', linewidth=2.5,label='点赞')
    plt.title('疫情的关注度变化趋势')
    plt.legend()
    plt.xlabel('时间')
    plt.ylabel('数量')
    plt.savefig('../data/疫情的关注度变化趋势.png')
    plt.show()


def emotion_score():
    def max_comment(x):
        df = x
        new_df = df.sort_values('comment',ascending=False)
        max_emotion_score = new_df['emotion_score']
        score = list(max_emotion_score.values)[0]
        return score

    data1 = df.groupby('time').apply(max_comment)

    x_data = list(data1.index)
    y_data = list(data1.values)
    plt.style.use('ggplot')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(9, 6),dpi=300)
    plt.bar(x_data, y_data)
    plt.title("微博-疫情-关注度最高的情感倾向")
    plt.xlabel("时间")
    plt.ylabel("分数")
    plt.savefig('../data/微博-疫情-关注度最高的情感倾向.png')
    plt.show()


if __name__ == '__main__':
    number_change()
    heat_change()
    emotion_score()
