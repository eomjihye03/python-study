# 최대/최소 요소 찾기: max(), min()

from random import random

a = [int(random() * 100) for _ in range(20)]
print(a)
print(max(a))
print(min(a))

b = ['Damon', 'Elena', 'Stefan', 'Caroline', 'Bonnie']
print(max(b), min(b))

c = [100, 20, 60, 'Damon', 'Elena', 'Stefan', 'Caroline', 'Bonnie']
print(max(c), min(c)) # TypeError: 크기 비교가 불가능한 경우

d = [100, 30, 34.5, True, False] # 복소수는 비교할 수 없다.
print(max(d), min(d))

from numbers import *
print(issubclass(int, Integral)) # int는 Integral의 virtual subclass다
print(issubclass(bool, int)) 
print(issubclass(float, Real)) # Virtual Class
print(issubclass(Integral, Real))
print(issubclass(Rational, Real))
print(issubclass(Complex, Number))
print(issubclass(complex, Complex)) # complex는 Complex의 virtual subclass다. 
print(issubclass(float, Real))
