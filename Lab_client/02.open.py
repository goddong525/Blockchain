import requests
import json

headers = {'Content-Type': 'application/json'}  # Content-Type 는 어떤 형태의 데이터를 보낼껀지를 적어주는것. 이걸 headrs 로.

data = {
    'question': 'Q1',
    'options': ['A1', 'A2', 'A3']
}

res = requests.post('http://127.0.0.1:5000/open', data=json.dumps(data), headers=headers)  # posts 라는 함수에서 요구되는 데이터들을 same name

print(res.text)