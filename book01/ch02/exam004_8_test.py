# '_이름' 식별자 (클래스 멤버) 테스트 

from exam004_8 import *

obj = C1()
print(obj.v1)
print(obj._v2) # 사용할 수 있지만, 권장하지 않음.

# 이유?
# 식별자가 "_이름" 형태로 되었다면, 
# 그 클래스를 만든 개발자는 내부적으로 사용할 용도로 만들었다는 뜻이기 때문.
# 즉, 나중에 언제든 필요에 따라 해당 변수를 변경할 수 있음을 의미.
# "내부용으로 만들었는데 괜히 사용하다가 문제가 발생할 수 있다. 
# 필요에 따라 없앨 수도 있습니다" 라는 뜻.
