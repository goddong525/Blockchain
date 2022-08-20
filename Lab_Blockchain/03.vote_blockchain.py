# 03. 투표 기록을 위한 블록체인

chain = []

block1 ={
    'type': 'open',  # vote started (투표를 열었다는 정보도 중요했다)
    'data': {
        'id': '투표 ID',
        'question': '투표 질문',
        'options': ['투표 항목1', '투표 항목2', '투표 항목3']   # get list (대괄호 안에 리스트 를 또 담을 수 있다)
    }
}

chain.append(block1)
print(chain)


block2 = {
    'type': 'vote',
    'data': {
        'id': '투표ID',
        'vote': '투표 항목1'  # 투표를 했냐, 어디에다 투표를 했냐.
    }
}

chain.append(block2)
print(chain)