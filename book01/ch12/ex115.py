# 딕셔너리로 모든 요소 복제
# shallow copy

d = {'name': 'Damon', 'age': 172, 'working': False}

d2  = d.copy()
d['name'] = 'Stefan'
d2['name'] = 'Elena'

print(d)
print(d2)