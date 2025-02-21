# 딕셔너리 요소 추가하고 값을 얻기

d = {'name': 'Elena', 'age': 22, 'working': True}
d['gender'] = 'Woman'
print(d)

key_list = ['name', 'age', 'working']
value_list = ['Damon', 172, False]

d2 = {}
for item in zip(key_list, value_list): # 두 리스트의 각 항목을 튜플로 묶는다.
    d2[item[0]] = item[1]
print(d2)

d2 = {}
for k, v in zip(key_list, value_list): # 두 리스트의 각 항목을 튜플로 묶는다.
    d2[k] = v
print(d2)


d2 = {}
for k in d: # dict에서 key를 꺼낸다.
    d2[k] = d[k]
print(d2)

d2 = {}
for k in d.keys(): # dict에서 key를 꺼낸다.
    d2[k] = d[k]
print(d2)

d2 = []
for value in d.values(): # dict에서 value를 꺼낸다.
    d2.append(value)
print(d2)

d2 = {}
for item in d.items(): # dict에서 (key, value) 튜플을 꺼낸다.
    d2[item[0]] = item[1]
print(d2)

d2 = {}
for k, v in d.items(): # dict에서 (key, value) 튜플을 꺼낸다.
    d2[k] = v           # unpacking (destructuring)
print(d2)