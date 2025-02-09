# mutable 객체 캐싱 
# - 값을 변경할 수 있는 객체는 캐싱 X
#      => list, set, dict, ...

a1 = [100, 200, 300]
a2 = [100, 200, 300]
print(id(a1), id(a2)) # 리스트는 캐싱 X
                    # 리스트는 변경되기 때문.

c1 = {1, 2, 3}
c2 = {1, 2, 3}
print(id(c1), id(c2)) # 집합은 캐싱 X. 변경 가능하기 때문.
print('*' * 100) 

e1 = {'name': 'Damon', 'age': '172'}
e2 = {'name': 'Damon', 'age': '172'}
print(id(e1), id(e2))



