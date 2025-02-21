# 딕셔너리에서 값 추출하기 2
# d.get()

d = {'name': 'Elena', 'age': 22, 'working': True}
print(d.get('name'))

d2 = {11: 'Elena', 12: 'Stefan', 13: 'Bonnie'}
print(d2.get(12))

print(d.get('gender')) # 존재하지 않은 key는 에러.
print(d2.get(100))

print(d.get('name', 'No name')) # 'name'이 없으면 'No name'이라고 출력.
print(d.get('gender', 'Woman'))