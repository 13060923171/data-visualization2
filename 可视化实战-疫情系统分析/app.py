
import os
import sys
import matplotlib
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/map1')
def map1():
    return render_template('map1.html', title='中国疫情地图')


@app.route('/map2')
def map2():
    return render_template('map2.html', title='世界疫情地图')


@app.route('/line')
def line():
    return render_template('line.html', title='中国疫情状况曲线图')



@app.route('/line2')
def line2():
    return render_template('line2.html', title='印度疫情状况曲线图')


@app.route('/Word')
def Word():
    return render_template('Word.html', title='疫情热词词云图')

@app.route('/rote_learning')
def rote_learning():
    return render_template('rote_learning.html', title='机器预测疫情发展曲线图')


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
