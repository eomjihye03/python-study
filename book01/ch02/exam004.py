# 변수와 타입
# - 파이썬은 '동적(dynamic) 타입 바인딩'을 사용.
# - 변수에 값을 넣을 때 변수의 타입이 결정됨.

a = 100
print(a, type(a))

a /= 2 # a는 int이기 때문에 int용 연산자 사용 가능.
print(a, type(a)) # 연산 결과가 float이 되면서 타입 변경.

a = 'Hello' # str으로 변경.
print(a, type(a))

a /= 2 # a는 str이기 때문에 int용 연산자 사용 X
# 현재 변수 타입에 따라 사용 가능한 연산자 결정.

# 참고: C, C++, Java는 대표적은 '정적(static) 타입 바인딩'을 사용한다.
#  
