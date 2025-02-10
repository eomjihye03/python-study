# for문

# for 변수 in iterable객체:
#     문장

# iterable 객체?
# __iter__() 매직 메서드(magic method; dunder method)가 리턴한 객체
# 값을 꺼내는 던더 메서드 __next__() 가 있다.
# 또는 던더 메서드 __getitem__() 이 있다.


s1 = "abcdef"
for ch in s1:
    print(ch, end=' ') # 포지셔널 아규먼트 / 키워드 아규먼트 

a = ['Damon', 'Elena', 'Stefan']
for name in a:
    print(name)

d = {'name': 'Elena', 'age': 20, 'working': True}
for key in d: # 키워드만 꺼냄...
    print(key) 

d = {'name': 'Elena', 'age': 20, 'working': True}
for key in d: # 인덱싱 이용
    print(key, d[key]) 

d = {'name': 'Elena', 'age': 20, 'working': True}
for value in d.values(): # 값만 꺼낸다.
    print(value)

d = {'name': 'Elena', 'age': 20, 'working': True}
for key_value in d.items(): # 키워드와 값을 튜플로 묶어서 꺼냄. (keyword, value)
    print(key_value[0], key_value[1])

d = {'name': 'Elena', 'age': 20, 'working': True}
for key, value in d.items(): # 튜플을 언패킹(unpacking; destructuring)
    print(key, value)

for i in range(1, 11): # range 클래스 이용.
    print(i, end=' ')

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if (i % 2) == 0:
        continue
    print(i, end=' ')

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if i == 5:
        break
    print(i, end=' ')


