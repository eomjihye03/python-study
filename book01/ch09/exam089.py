# 문자열로 된 식을 실행하기
# eval(파이썬 표현식)
#   . 파이썬 표현식을 실행한 후 그 결과를 리턴.
#   . 표현식: 결과를 리턴하는 문장


a = eval('100 + 200')
print(a)

# a = eval("x = 100") # expression 아니다.
# print(a)

# a = eval("x := 100") # expression 아니다.
# print(a)

a = eval('len("ABC")')
print(a)

a = eval('print("Hello")')
print(a)

def f1():
    pass # 함수에 리턴문이 없으면 None을 리턴한다.
print(f1())

