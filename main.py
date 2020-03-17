from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


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