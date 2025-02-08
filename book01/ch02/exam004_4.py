# 기타 객체 캐싱 
# - 값을 변경할 수 있는(mutable) 객체는 캐싱 X
#      => list, set, dict, ...
# - 값을 변경할 수 없는(immutable) 객체는 캐싱 O
#      => int, float, complex, bool, str, bytes, tuple, ...

a1 = [100, 200, 300]
a2 = [100, 200, 300]
print(id(a1), id(a2)) # 리스트는 캐싱 X
                    # 리스트는 변경되기 때문.

b1 = (100, 200, 300)
b2 = (100, 200, 300)
print(id(b1), id(b2)) # 튜플은 캐싱된다. 변경되지 않기 때문.

c1 = {1, 2, 3}
c2 = {1, 2, 3}
print(id(c1), id(c2)) # 집합은 캐싱 X. 변경 가능하기 때문.

d1 = 3.1 + 4.5j # 리터럴로 객체 생성.
d2 = complex(3.1 + 4.5j) # 클래스로 객체 생성.
print(id(d1), id(d2)) # 복소수는 캐싱 O

e1 = {'name': 'Damon', 'age': '172'}
e2 = {'name': 'Damon', 'age': '172'}
print(id(e1), id(e2))



