# 딕셔너리 갱신하기
# d.update()

d = {'name': 'Damon', 'age': 172, 'working': False}
d2 = {'gender': 'man', 'tel': '010-1111-2222'}
d.update(d2)
print(id(d), d)
print(id(d2), d2)