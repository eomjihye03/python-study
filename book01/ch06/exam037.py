# generator로 Iterator 만들기
def MyRange(n):
    cursor = 0
    while cursor < n:
        yield cursor # 자동으로 generator가 되게 함.
        cursor += 1
# 단축코드!!!! 코드 최적화. 프레임 워크.
    
my_range = MyRange(5) # generator: iterable 객체
print(type(my_range))
my_iterator = my_range.__iter__()
print(my_iterator.__next__())
print(my_iterator.__next__())
print(my_iterator.__next__())
print(my_iterator.__next__())
print(my_iterator.__next__())
print(my_iterator.__next__())

my_range = MyRange(5)
my_iterator = iter(my_range)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))