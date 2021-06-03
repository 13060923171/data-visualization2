import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']

df = pd.read_excel('百奥泰-U.xlsx',sheet_name='公司经营成果').loc[:,['采购额（万元）','占比']]

x_data = []
y_data = []

for x in df['采购额（万元）']:
    x = str(str(x) + '(万元)')
    x_data.append(x)

for y in df['占比']:
    y = float(y*100)
    y_data.append(y)
print(y_data,x_data)
colors = ['mediumspringgreen','mediumaquamarine','aquamarine','turquoise','lightseagreen'] #每块颜色定义
explode = (0,0,0.02,0,0) #将某一块分割出来，值越大分割出的间隙越大
patches,text1,text2 = plt.pie(y_data,
                      explode=explode,
                      labels=x_data,
                      colors=colors,
                      labeldistance = 1,#图例距圆心半径倍距离
                      autopct = '%.1f%%', #数值保留固定小数位
                      shadow = False, #无阴影设置
                      startangle =90, #逆时针起始角度设置
                      pctdistance = 0.6) #数值距圆心半径倍数距离
#patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部文本
# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')
plt.legend()
plt.title('公司经营成果图')
plt.savefig('图2.jpg')
plt.show()