# 지연변수와 전역변수: global

a = 100
def f1(a): # 파라미터도 지역 변수이다.
    a += 100
    print(a)

f1(a)
print(a)

def f2():
    a = 300 # 로컬 변수

f2() # 로컬 별수는 함수 호출 종료시 제거된다.
print(a)

# 함수에서 전역변수 사용하기
def f3():
    global a # a는 전역변수임을 선언한다.
    a = 300
f3()
print(a)
