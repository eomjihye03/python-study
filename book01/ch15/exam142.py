# 예외 처리: assert 정상조건

a = ['a', 'bc', 1234, 'def', 'ghij']
try:
    for v in a:
        assert type(v) is str, f'{v}는 문자열이 아닙니다.'
        print(v)
except AssertionError as e:  
    print(e)

# 예외 발생: raise 예외객체
try:
    a = int(input("a > "))
    b = int(input('b > '))
    if b == 0:
        raise RuntimeError("0으로 나눌 수 없습니다...!!!")
    print(a / b)
except Exception as e:
    print(e)