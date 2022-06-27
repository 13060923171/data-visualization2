import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
df = pd.read_csv('./output/聚类结果.csv')


def time_qx(x):
    x = str(x)
    x = x.split(" ")
    x = x[0].split("-")
    x = x[0] + "-" + x[1]
    return x


df = df.dropna(subset=['comment'])
df['发文时间'] =  df['发文时间'].apply(time_qx)


def key_total(x):
    list_count = []
    for i in df['comment']:
        num = i.count(x)
        list_count.append(num)
    return list_count


def word_number(key):
    df[key] = key_total(key)
    new_df = df.groupby('发文时间').agg('sum')
    x_data = [x for x in new_df.index]
    y_data = [y for y in new_df[key]]
    return key,x_data,y_data

def main1():
    key1, x_data1, y_data1 = word_number('delivery')
    key2, x_data2, y_data2 = word_number('deliveries')
    key3, x_data3, y_data3 = word_number('shipping')
    key4, x_data4, y_data4 = word_number('shift')
    key5, x_data5, y_data5 = word_number('local')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data1, y_data1, '*--', linewidth=2, color='#34495E', label=key1)
    plt.plot(x_data2, y_data2, '*--', linewidth=2, color='#F7DC6F', label=key2)
    plt.plot(x_data3, y_data3, '*--', linewidth=2, color='#F1C40F', label=key3)
    plt.plot(x_data4, y_data4, '*--', linewidth=2, color='#E74C3C', label=key4)
    plt.plot(x_data5, y_data5, '*--', linewidth=2, color='#EC7063', label=key5)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别1')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别1.png')
    plt.show()

def main2():
    key6, x_data6, y_data6 = word_number('buy')
    key7, x_data7, y_data7 = word_number('buying')
    key8, x_data8, y_data8 = word_number('saving')
    key9, x_data9, y_data9 = word_number('free')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data6, y_data6, '*--', linewidth=2, color='#34495E', label=key6)
    plt.plot(x_data7, y_data7, '*--', linewidth=2, color='#F7DC6F', label=key7)
    plt.plot(x_data8, y_data8, '*--', linewidth=2, color='#F1C40F', label=key8)
    plt.plot(x_data9, y_data9, '*--', linewidth=2, color='#E74C3C', label=key9)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别2')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别2.png')
    plt.show()


def main3():
    key10, x_data10, y_data10 = word_number('spent')
    key11, x_data11, y_data11 = word_number('spending')
    key12, x_data12, y_data12 = word_number('times')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data10, y_data10, '*--', linewidth=2, color='#34495E', label=key10)
    plt.plot(x_data11, y_data11, '*--', linewidth=2, color='#F7DC6F', label=key11)
    plt.plot(x_data12, y_data12, '*--', linewidth=2, color='#F1C40F', label=key12)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别3')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别3.png')
    plt.show()

def main4():
    key13, x_data13, y_data13 = word_number('increased')
    key14, x_data14, y_data14 = word_number('increase')
    key15, x_data15, y_data15 = word_number('accelerated')
    key16, x_data16, y_data16 = word_number('rise')
    key17, x_data17, y_data17 = word_number('growth')
    key18, x_data18, y_data18 = word_number('boom')
    key19, x_data19, y_data19 = word_number('trends')
    key20, x_data20, y_data20 = word_number('surge')
    key21, x_data21, y_data21 = word_number('impact')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data13, y_data13, '*--', linewidth=2, color='#34495E', label=key13)
    plt.plot(x_data14, y_data14, '*--', linewidth=2, color='#F7DC6F', label=key14)
    plt.plot(x_data15, y_data15, '*--', linewidth=2, color='#F1C40F', label=key15)
    plt.plot(x_data16, y_data16, '*--', linewidth=2, color='#E74C3C', label=key16)
    plt.plot(x_data17, y_data17, '*--', linewidth=2, color='#EC7063', label=key17)
    plt.plot(x_data18, y_data18, '*--', linewidth=2, color='#F7DC6F', label=key18)
    plt.plot(x_data19, y_data19, '*--', linewidth=2, color='#F1C40F', label=key19)
    plt.plot(x_data20, y_data20, '*--', linewidth=2, color='#E74C3C', label=key20)
    plt.plot(x_data21, y_data21, '*--', linewidth=2, color='#EC7063', label=key21)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别4')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别4.png')
    plt.show()


def main5():
    key22, x_data22, y_data22 = word_number('safe')
    key23, x_data23, y_data23 = word_number('check')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data22, y_data22, '*--', linewidth=2, color='#34495E', label=key22)
    plt.plot(x_data23, y_data23, '*--', linewidth=2, color='#F7DC6F', label=key23)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别5')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别5.png')
    plt.show()

def main6():
    key24, x_data24, y_data24 = word_number('stay')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data24, y_data24, '*--', linewidth=2, color='#34495E', label=key24)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别6')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别6.png')
    plt.show()

def main7():
    key25, x_data25, y_data25 = word_number('feel')
    key26, x_data26, y_data26 = word_number('survey')
    key27, x_data27, y_data27 = word_number('services')
    key28, x_data28, y_data28 = word_number('customer')
    key29, x_data29, y_data29 = word_number('experience')
    key30, x_data30, y_data30 = word_number('love')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data25, y_data25, '*--', linewidth=2, color='#34495E', label=key25)
    plt.plot(x_data26, y_data26, '*--', linewidth=2, color='#F7DC6F', label=key26)
    plt.plot(x_data27, y_data27, '*--', linewidth=2, color='#F1C40F', label=key27)
    plt.plot(x_data28, y_data28, '*--', linewidth=2, color='#E74C3C', label=key28)
    plt.plot(x_data29, y_data29, '*--', linewidth=2, color='#EC7063', label=key29)
    plt.plot(x_data30, y_data30, '*--', linewidth=2, color='#F7DC6F', label=key30)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别7')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别7.png')
    plt.show()

def main8():
    key31, x_data31, y_data31 = word_number('stores')
    key32, x_data32, y_data32 = word_number('amazon')
    key33, x_data33, y_data33 = word_number('store')
    key34, x_data34, y_data34 = word_number('shops')
    key35, x_data35, y_data35 = word_number('mall')
    key36, x_data36, y_data36 = word_number('market')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data31, y_data31, '*--', linewidth=2, color='#34495E', label=key31)
    plt.plot(x_data32, y_data32, '*--', linewidth=2, color='#F7DC6F', label=key32)
    plt.plot(x_data33, y_data33, '*--', linewidth=2, color='#F1C40F', label=key33)
    plt.plot(x_data34, y_data34, '*--', linewidth=2, color='#E74C3C', label=key34)
    plt.plot(x_data35, y_data35, '*--', linewidth=2, color='#EC7063', label=key35)
    plt.plot(x_data36, y_data36, '*--', linewidth=2, color='#F7DC6F', label=key36)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别8')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别8.png')
    plt.show()

def main9():
    key37, x_data37, y_data37 = word_number('news')
    key38, x_data38, y_data38 = word_number('items')
    key39, x_data39, y_data39 = word_number('products')
    key40, x_data40, y_data40 = word_number('unique')
    key41, x_data41, y_data41 = word_number('finding')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data37, y_data37, '*--', linewidth=2, color='#34495E', label=key37)
    plt.plot(x_data38, y_data38, '*--', linewidth=2, color='#F7DC6F', label=key38)
    plt.plot(x_data39, y_data39, '*--', linewidth=2, color='#F1C40F', label=key39)
    plt.plot(x_data40, y_data40, '*--', linewidth=2, color='#E74C3C', label=key40)
    plt.plot(x_data41, y_data41, '*--', linewidth=2, color='#EC7063', label=key41)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别9')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别9.png')
    plt.show()

def main10():
    key42, x_data42, y_data42 = word_number('digital')
    key43, x_data43, y_data43 = word_number('learned')
    key44, x_data44, y_data44 = word_number('learn')
    key45, x_data45, y_data45 = word_number('habits')
    key46, x_data46, y_data46 = word_number('changed')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data42, y_data42, '*--', linewidth=2, color='#34495E', label=key42)
    plt.plot(x_data43, y_data43, '*--', linewidth=2, color='#F7DC6F', label=key43)
    plt.plot(x_data44, y_data44, '*--', linewidth=2, color='#F1C40F', label=key44)
    plt.plot(x_data45, y_data45, '*--', linewidth=2, color='#E74C3C', label=key45)
    plt.plot(x_data46, y_data46, '*--', linewidth=2, color='#EC7063', label=key46)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别10')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别10.png')
    plt.show()

def main11():
    key47, x_data47, y_data47 = word_number('holiday')
    key48, x_data48, y_data48 = word_number('christmas')
    key49, x_data49, y_data49 = word_number('gifts')
    key50, x_data50, y_data50 = word_number('demand')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data47, y_data47, '*--', linewidth=2, color='#34495E', label=key47)
    plt.plot(x_data48, y_data48, '*--', linewidth=2, color='#F7DC6F', label=key48)
    plt.plot(x_data49, y_data49, '*--', linewidth=2, color='#F1C40F', label=key49)
    plt.plot(x_data50, y_data50, '*--', linewidth=2, color='#E74C3C', label=key50)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别11')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别11.png')
    plt.show()

def main12():
    key51, x_data51, y_data51 = word_number('restrictions')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data51, y_data51, '*--', linewidth=2, color='#34495E', label=key51)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别12')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别12.png')
    plt.show()

def main13():
    key52, x_data52, y_data52 = word_number('restrictions')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data52, y_data52, '*--', linewidth=2, color='#34495E', label=key52)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别13')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别13.png')
    plt.show()

def main14():
    key53, x_data53, y_data53 = word_number('restrictions')
    plt.figure(figsize=(20,9),dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.plot(x_data53, y_data53, '*--', linewidth=2, color='#34495E', label=key53)
    plt.legend(loc=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    plt.title('类别14')
    plt.xticks(rotation=65)
    plt.savefig('./output/类别14.png')
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
    main9()
    main10()
    main11()
    main12()
    main13()
    main14()





