# RESTful API 클라이언트 요청 방식 메서드(method) : GET, POST

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api1', methods=['GET'])  # GET 방식
def f1():
    # return 'GET api1'
    return jsonify({'status': 'success'})  # 출력결과 는 {'status':'success'}


@app.route('/api2', methods=['POST'])  # POST 방식
def f2():
    # return 'POST api2'
    data = request.get_json()  # data 에 넣고 출력
    return jsonify(data)


app.run()