# 딕셔너리 모든 키로 iterator 생성

d = {'name': 'Elena', 'age': 22, 'working': True}
i = iter(d) # __iter__() 호출
print(type(i), i)


for key in i:
    print(key)

d.clear()
print(d)

