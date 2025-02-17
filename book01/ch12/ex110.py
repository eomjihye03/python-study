# 딕셔너리에 요소를 추가하고 값을 얻기
# d.setdefault()

d = {'name': 'Elena', 'age': 22, 'working': True}
name = d.setdefault('name') # name 값 꺼내기
print(name)
print(d)

# key에 해당하는 값이 없으면 None 리턴., key를 등록한 후 None으로 설정.

d = {'name': 'Elena', 'age': 22, 'working': True}
gender = d.setdefault('gender') # name 값 꺼내기
print(gender)
print(d)

# key에 해당하는 값이 없으면 'Woman' 리턴., key를 등록한 후 'Woman'으로 설정.

d = {'name': 'Elena', 'age': 22, 'working': True}
gender = d.setdefault('gender', 'Woman') # name 값 꺼내기
print(gender)
print(d)

