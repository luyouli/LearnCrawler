# coding:utf8
from flask import Flask,render_template
from time import sleep
# 实例化一个APP
app = Flask(__name__)

# 创建视图函数和路由地址
@app.route('/Baby')
def index_1():
    sleep(2)
    return render_template('test.html')
@app.route('/jay')
def index_2():
    sleep(2)
    return render_template('test.html')
@app.route('/tom')
def index_3():
    sleep(2)
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
