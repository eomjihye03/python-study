print('m1 모듈 로딩됨!')

def f1():
    print('p1.m1.f1()')
def f2():
    print('p1.m1.f2()')

# 보호 모드 함수
def _f3():
    print('p1.m1._f3()')