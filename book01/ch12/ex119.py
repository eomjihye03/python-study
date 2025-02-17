# 딕셔너리 키 순서를 거꾸로

d = {'name': 'Damon', 'age': 172, 'working': False}

key_list = d.keys()
print(key_list)

key_list2 = list(reversed(d)) # 사실상 의미 없음.
print(key_list2)