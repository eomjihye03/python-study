# 딕셔너리 갱신하기
# d.update()

d = {'name': 'Damon', 'age': 172, 'working': False}
d2 = {'gender': 'man', 'tel': '010-1111-2222'}
d.update(d2) # 원본 변경
print(d2)

d = {'name': 'Damon', 'age': 172, 'working': False}
d2 = {'gender': 'man', 'tel': '010-1111-2222'}
d3 = d | d2 # 새로 만듦.
print(id(d), id(d3))
print(d)
print(d3)

d = {'name': 'Damon', 'age': 172, 'working': False}
d2 = {'gender': 'man', 'tel': '010-1111-2222'}
print(id(d))
d |= d2 # d.update(d2)와 같다.
print(id(d))
print(d)

