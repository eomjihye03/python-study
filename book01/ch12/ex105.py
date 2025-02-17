# 딕셔너리에서 값 추출하기
# d[key]

d = {'name': 'Elena', 'age': 22, 'working': True}
print(d['name'])
print(d['age'])
print(d['working'])

d2 = {11: 'Elena', 12: 'Stefan', 13: 'Bonnie'}
print(d2[12])

print(d['gender']) # 존재하지 않은 key는 에러.
print(d2[100])
