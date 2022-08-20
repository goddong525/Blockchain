from flask import Flask
app = Flask(__name__)


@app.route("/")   # 기본 (시작하자마자 나오는것)
def f1():  # f1 이라는 함수 하나 만들기
    return "시작 페이지"


@app.route("/abcd")   # 링크에 /abcd 입력했을때 "abcd" 가 적혀있는 화면으로 감.
def f2():
    return "abcd"


app.run()