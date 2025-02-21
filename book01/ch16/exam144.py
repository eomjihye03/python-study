# 모듈 사용

# from p1 import m1
# import p1.m1 as m1

# 1) 전체 모듈명 지정
# import p1.m1
# p1.m1.f1()        # 함수를 호출할 때마다 전체 모듈명을 지정해야 한다.
# p1.m1.f2()
# p1.m1._f3()

# 2) 별명 사용
# import p1.m1 as mx
# mx.f1()       # 전체 모듈명 대신 별명을 지정하면 된다.
# mx.f2()
# mx._f3()

# 3) 패키지의 특정 모듈만 임포트
# from p1 import m1
# m1.f1()
# m1.f2()
# m1._f3()

# 4) 모듈의 특정 함수만 임포트
# from p1.m1 import f1, f2, _f3
# f1() # 모듈명을 붙일 필요가 없다.
# f2()
# _f3()

# 5) 보호 모드 멤버는 제외하고 모두 가져오기
from p1.m1 import *
f1()
f2()
_f3() # 사용할 수 없다.