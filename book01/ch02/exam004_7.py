# 특별한 식별자: '_이름'
# - 보호 모드 변수

# - 모듈 안의 멤버인 경우 
# 'from 모듈명 import *' 로 가져올 수 없다.
# 'from 모듈명 import _v2' 으로 직접 명시한다면 사용 가능.

# - 클래스 안의 멤버
# 클래스 내부에서만 사용한다는 것을 암시. 단, 강제적 X

v1 = 100
def f1():
    pass

class C1:
    pass

_v2 = 200
def _f2():
    pass

class _C2:
    pass
