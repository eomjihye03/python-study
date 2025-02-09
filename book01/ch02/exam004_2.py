# immutable 객체 캐싱 
# - 값을 변경할 수 없는(immutable) 객체는 캐싱 O
#      => int, float, complex, bool, str, bytes, tuple, ...

# int 객체 캐싱 (integer interning)
a1 = -5
a2 = 7 - 12
print(a1, a2)
print(id(a1), id(a2))

b1 = 256
b2 = 100 + 120 + 36
print(b1, b2)
print(id(b1), id(b2))

print('*' * 100)

# float 객체 캐싱
# - 부동소수점은 2진수로 정규화되는 과정에서 완전하게 바뀌지 못하는 경우가 있다.
# - 그래서 계산 상으로 같은 값일지라도 메모리 상에서는 다를 수 있다.
# - 즉, 상황에 따라 캐싱이 안될 경우도 있다. 

c1 = 3.14
c2 = 2.1 + 1.04
print(c1, c2)
print(id(c1), id(c2)) # 캐싱 되는 경우
print(c1 == c2) # 같다

c1 = 3.14
c2 = 2.11 + 1.03
print(c1, c2)
print(id(c1), id(c2)) # 캐싱 안되는 경우
print(c1 == c2) # 다르다
print(round(c1, 2) == round(c2, 2)) # 부동소수점 비교할 때는 반올림해서 비교해야 한다.

print('*' * 100)

# complex 객체 캐싱
d1 = 3.4 + 56.1j
d2 = 3.4 + 50j + 6.1j
print(d1, d2)
print(id(d1), id(d2)) # 캐싱 되는 경우
print(d1 == d2) # 같다

d1 = 3.4 + 56.7j
d2 = 3.4 + 51.3j + 5.4j
print(d1, d2)
print(id(d1), id(d2)) # 캐싱 안되는 경우
print(d1 == d2) # 다르다

print('*' * 100)

# bool 객체
b1 = True
b2 = 100 > 40
print(b1, b2)
print(id(b1), id(b2))

print('*' * 100) # 캐싱된다.

# str 객체

a1 = 'Hello'
a2 = 'He' + 'llo' # concatenation
print(a1, a2)
print(id(a1), id(a2)) # 리터럴끼리 연결된 것은 리터럴로 간주. => 캐싱됨.

b1 = "He"
b2 = "llo"
b3 = b1 + b2 
print(b3, id(b3)) # 변수와 변수의 연결은 새로운 str 생성. => 캐싱 X

c1 = str("Hello") # 클래스로 str 객체 생성하는 것은 리터럴을 직접 쓰는 것과 동일. 
c2 = str("Hello")
print(c1, c2)
print(id(c1), id(c2))

print('*' * 100)

# bytes 객체
a1 = b'ABC'
a2 = bytes(b'ABC')
print(a1, a2)
print(id(a1), id(a2)) # 캐싱됨!
print('*' * 100) 

# tuple 객체
b1 = (100, 200, 300)
b2 = (100, 200, 300)
print(id(b1), id(b2)) # 튜플은 캐싱된다. 변경되지 않기 때문.