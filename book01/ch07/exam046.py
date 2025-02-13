# 순차적 정수열 만들기: range()

a = range(10)
print(list(a))

print(list(range(0, 3)))
print(list(range(3, 7)))
print(list(range(7, 10)))

print(list(range(2, 20, 3)))

# list comprehension
print([x for x in range(1, 10, 2)])
