# Iterable 객체

from collections.abc import Iterable
a = [1, 2, 3, 4, 5, 2, 3]
b = (1, 2, 3, 4, 5, 2, 3)
c = {1, 2, 3, 4, 5, 2, 3}
d = {'name': 'Caroline', 'age': 20}
e = 'hello'
f = b'ABCDE'
g = range(1, 11)

print(issubclass(list, Iterable))
print(issubclass(tuple, Iterable))
print(issubclass(set, Iterable)) 
print(issubclass(dict, Iterable)) 
print(issubclass(str, Iterable)) 
print(issubclass(range, Iterable)) 

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(c, Iterable))
print(isinstance(d, Iterable))
print(isinstance(e, Iterable))
print(isinstance(f, Iterable))

# iterable 인가 = 반복문에 올 수 있는가

