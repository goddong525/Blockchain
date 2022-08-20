# 도전과제 1번

from flask import Flask, jsonify, request

app = Flask(__name__)

chain = []
cnt = 0  # 투표의 개수


# 3가지의 API 만들기


@app.route('/list', methods=['GET'])
def vote_list():
    return jsonify(chain)  # chain 을 dictionary 형태로 만들어 뒀기 때문에 바로 jsonify 에다가 넘겨줄 수 있음.


@app.route('/open', methods=['POST'])  # 투표 열기
def vote_open():
    global cnt  # cnt를 쓰기 위해 global 을 앞에 써둠.
    try:  # try : 에러 났을 때 프로그램이 죽는게 아니라 계속 프로그램 실행.
        data = request.get_json()
        block = {  # 블록을 만들어줌
            'type': 'open',  # 투표가 열리니깐 open
            'data': {
                'id': str(cnt),
                'question': data['question'],
                'options': data['options']
            }
        }

        cnt += 1
        chain.append(block)
        return jsonify({'status': 'succes'})
    except:  # try 문 안에 오류가 일어났을때 except 안으로 옴.
        return jsonify({'status': 'fail'})


@app.route('/vote', methods=['POST'])
def vote():
    try:
        data = request.get_json()
        block = {
            'type': 'vote',
            'data': {
                'id': data['id'],
                'vote': data['vote']
            }
        }
        chain.append(block)
        return jsonify({'status': 'success'})
    except:
        return jsonify({'status': 'fail'})


app.run()
