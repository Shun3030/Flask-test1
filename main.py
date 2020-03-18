from flask import Flask, render_template
from random import randint


app = Flask(__name__)


@app.route('/')
def index():
    text = 'Hello from main.py'
    lis = ["first", "second", "third"]
    dic = {"name": "Shun", "age": 27}
    x = randint(0, 10)

    return render_template('index.html', text=text, lis=lis, dic=dic, x=x)


# 本番実行用の関数
def main():
    app.debug = True
    app.run(host='0.0.0.0', port=8080)


# テスト実行用の関数
def test():
    app.debug = True
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    #main()
    test()