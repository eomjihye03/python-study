# list()
# . list 클래스
# . list(iterable 객체) => list 생성 
# . iterable 객체
#       . iterator 객체를 리턴하는 __iter__() 매직 메서드를 갖고 있는 클래스
# . iterator 객체
#       . 컬렉션(값 목록 객체)에서 값을 꺼내주는 __next__() 매직 메서드를 갖고 있는 클래스

t = (10, 20, 30)
print(list(t))

s = 'Hello, World'
print(list(s))

# MutableSequence
# list

l = list() # empty list
print(type(l))

# 객체가 클래스의 인스턴스인지 확인
from collections.abc import *
print(isinstance(l, list))
print(isinstance(l, MutableSequence))
print(isinstance(l, Sequence))
print(isinstance(l, Collection))
print(isinstance(l, Reversible))
print(isinstance(l, Container))
print(isinstance(l, Sized))
print(isinstance(l, Iterable))

# 클래스의 상속관계 확인
print(issubclass(list, MutableSequence))
print(issubclass(list, Sequence))
print(issubclass(list, Collection))
print(issubclass(list, Reversible))
print(issubclass(list, Sized))
print(issubclass(list, Container))
print(issubclass(list, Iterable))

print(issubclass(tuple, MutableSequence))
print(issubclass(tuple, Sequence))
print(issubclass(tuple, Collection))
print(issubclass(tuple, Reversible))
print(issubclass(tuple, Sized))
print(issubclass(tuple, Container))
print(issubclass(tuple, Iterable))

print(issubclass(set, MutableSet))
print(issubclass(set, Set))
print(issubclass(set, Collection))
print(issubclass(set, Reversible))
print(issubclass(set, Sized))
print(issubclass(set, Container))
print(issubclass(set, Iterable))

print(issubclass(dict, MutableMapping))
print(issubclass(dict, Mapping))
print(issubclass(dict, Collection))
print(issubclass(dict, Reversible))
print(issubclass(dict, Sized))
print(issubclass(dict, Container))
print(issubclass(dict, Iterable))

