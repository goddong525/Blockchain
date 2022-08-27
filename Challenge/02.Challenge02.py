# 도전과제 2번

from flask import Flask, jsonify, request
import requests, json

print("1. 블록 체인 조회")
print("2. 투표 생성")
print("3. 투표")

n = int(input("=>"))

if n == 1:
    res = requests.get('http://127.0.0.1:5000/list')
    print(res.text)

if n == 2:
    headers = {'Content-Type': 'application/json'}

    data = {
        'question': 'Q1',
        'options': ['A1', 'A2', 'A3']
    }

    Q1 = input("질문: ")
    A1 = input("선택지1: ")
    A2 = input("선택지2: ")
    A3 = input("선택지3: ")

    data['question'] = Q1
    data['options'][0] = A1
    data['options'][1] = A2
    data['options'][2] = A3

    res = requests.post('http://127.0.0.1:5000/open',
                        data=json.dumps(data),
                        headers=headers)

    print(res.text)

if n == 3:
    headers = {'Content_Type': 'application/json'}

    data = {'id': '0', 'vote': 'A1'}

    id = input("투표ID: ")
    A1 = input("투표: ")

    data['id'] = id;
    data['vote'] = A1;

    res = requests.post(
        'http://127.0.0.1:5000/vote',
        data=json.dumps(data),
        headers=headers)  # 서버요청

    print(res.text)





