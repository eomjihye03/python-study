# map(func, iterable)
#   . iterable 객체의 값을 꺼내서 func으로 가공한 후 값을 리턴하는 역할.

a = [1, 2, 3, 4, 5]

# 1) 값을 처리하는 함수를 따로 정의
def power(x):
    return x * x


power_map = map(power, a) # iterable 객체 값을 꺼내서 함수로 처리
print(type(power_map))

# map은 iterator 역할 수행한다.
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())

print(list(power_map))

# 2) 값을 처리하는 함수를 람다(lambda)로 정의
#   . lambda: 함수의 간결한 문법

power_map2 = map(lambda x: x * x, a)
print(list(power_map2))

# 3) 두 개의 리스트를 처리하기
a = ['사과', '배', '복숭아']
b = [2000, 3000, 1500]

prod_map = map(lambda x, y: (x, y), a, b)
print(list(prod_map))

# map 없이 구현하려면??