# zip(iterable1, iterable2)
#   . 여러 개의 iterable 객체의 값을 묶는 일을 함.
#   . iterable 중 최소 개수를 기준으로 묶음. => 남는건 버림.
from collections.abc import Iterable

a = ['사과', '배', '복숭아', '딸기']
b = [2000, 3000, 1500, 2300]
c = [100, 20, 50]

prods = zip(a, b, c)
print(type(prods))
print(isinstance(prods, Iterable))
print(list(prods))

# Iterable 객체들의 크기가 같지 않을 경우 (꺼낼 때) 오류를 발생시키려면
# 엄격하게... 
prods = zip(a, b, c, strict=True)
prods_iterator = prods.__iter__()
prods_next = prods.__next__()
prods_next = prods.__next__()
prods_next = prods.__next__()
prods_next = prods.__next__()
print(list(prods))

########## zip 상태에서는 오류가 안나는데?
# __next__()를 호출할 때 짝이 맞지 않으면 오류 발생.

