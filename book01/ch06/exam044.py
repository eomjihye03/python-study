# sorted(iterable 객체)
#   . 오름차순으로 정렬하여 list를 리턴함. (default)

from random import random
# random(): 0 <= x < 1, 부동소수점
a = [int(random() * 10) for _ in range(10)]
sorted_a = sorted(a) # 원본을 변경하지 않고 정렬된 새 list를 리턴.
print(a)
print(sorted_a)

a = ('apple', 'pear', 'banana', 'grape', 'mango', 'carot', 'strawberry')
a2 = sorted(a)
print(a)
print(a2)
a3 = sorted(a, reverse=True)
print(a3)

s = 'Hello, World!'
sorted_s = sorted(s)
print(s)
print(sorted_s)

a = {'name': 'Damon', 'age': 172, 'gender': 'man', 'working': True}
sorted_a = sorted(a) # key만 정렬하여 list를 리턴.
print(a)
print(sorted_a)

