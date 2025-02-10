# iter(), next()

a = [1, 2, 3, 4, 5, 2, 3]
obj_iterator1 = a.__iter__()
obj_iterator2 = iter(a) # iter() --> a.__iter__()

print(obj_iterator1, obj_iterator2)

print(obj_iterator1.__next__())
print(next(obj_iterator2)) # next() --> __next__()

# next()
# - Iterator의 __next__()를 호출하여 값을 꺼낸다.
# - 더이상 꺼낼 값이 없으면 StopIteration 예외 발생!
