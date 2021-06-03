import base64
from io import BytesIO
from lxml import etree
from matplotlib import pyplot as plt
from demo.data.forecast import chinaforcast
from demo.data.new_julei import julei

def pltxianshi():
    chinaforcast()
    # figure 保存为二进制文件
    buffer = BytesIO()
    plt.savefig(buffer)
    plt.savefig('static/images/wangye.png')
    # plot_data = buffer.getvalue()
    # #图像数据转化为HTML格式
    # imb = base64.b64encode(plot_data)
    # ims = imb.decode()
    # imd = "data:image/png;base64," + ims
    # iris_im = """<h1>国内预测</h1>  """ + """<img src="%s">""" % imd
    #
    # root = "<title>国内预测</title>"
    # root = root +  iris_im  # 将多个 html 格式的字符串连接起来
    # # lxml 库的 etree 解析字符串为 html 代码，并写入文件
    # html = etree.HTML(root)
    # tree1 = etree.ElementTree(html)
    # # return tree1
    # tree1.write('wangye2.html')

def pltxianshi2():
    julei()
    # figure 保存为图片
    buffer = BytesIO()
    plt.savefig(buffer)
    plt.savefig('static/images/wangye2.png')
    # data = base64.encodebytes(buffer.getvalue()).decode()
    # html = '''
    #        <html>
    #            <body>
    #                <img src="data:image/png;base64,{}" />
    #            </body>
    #         <html>
    #     '''
    # plt.close()
    # tree = etree.ElementTree(html)
    # # 记得关闭，不然画出来的图是重复的
    # # return html.format(data)
    # tree.write('wangye2.html')

pltxianshi()

