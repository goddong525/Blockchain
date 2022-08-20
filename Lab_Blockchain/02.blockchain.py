#블록체인
chain = []

# 1번블록
block1 = {

    'key1': 'value1'
}

chain.append(block1)
# 원래는 빈 대괄호였다가 block1 번이 추가됨.

print(chain)

block2 = {
    'key2': 'value2'
}

chain.append(block2)
print(chain)


# 실행결과
"""
[{'key1': 'value1'}]
[{'key1': 'value1'}, {'key2': 'value2'}]
"""