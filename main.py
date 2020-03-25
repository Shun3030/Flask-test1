from flask import Flask, render_template, abort
from random import randint


app = Flask(__name__)


@app.route('/')
def index():
    text = 'Hello from main.py'
    lis = ["first", "second", "third"]
    dic = {"name": "Shun", "age": 27}
    x = randint(0, 10)

    return render_template('index.html', text=text, lis=lis, dic=dic, x=x)


#500エラー発生関数
@app.route('/err500')
def err500():
    abort(500)


#エラー処理
@app.errorhandler(404)
def handle_404(exception):
    return {'message': 'Error: Resource not found.'}, 404


@app.errorhandler(500)
def handle_500(exception):
    return {'message': 'Please contact the administrator.'}, 500


# 実行用の関数
def main():
    app.debug = True
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
