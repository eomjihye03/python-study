# 딕셔너리에서 요소를 제거한 후 값 조회
# d.pop(), d.popitem()

# pop() 사용법
d = {'name': 'Damon', 'age': 172, 'working': False}
print(d.pop('age'))
print(d)

print(d.pop('gender')) # KeyError
print(d.pop('gender', 20)) # 존재하지 않으면 20 리턴해라.

# popitem() 사용법
d = {'name': 'Damon', 'age': 172, 'working': False}
print(d.keys()) # 입력된 순서대로 key list 리턴.
print(d.popitem()) # 맨 뒤의 (key, value) 튜플 리턴.
print(d)
print(d.popitem())
print(d.popitem())
print(d.popitem()) # 꺼낼게 없다면 KeyError