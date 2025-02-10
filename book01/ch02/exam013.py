# 패키지 및 모듈 사용

from abc_m1.m1 import * 
print(a)

# from abc-m2.m2 import * 
# 직접 만든 패키지 이름에 -가 있으면 import 할 수 없다.
# import 하려면 importlib를 사용해야 함.
import importlib
m2 = importlib.import_module('abc-m2.m2')
print(m2.b)

# 단, pip로 설치할 경우에는 -가 _로 자동 변환된다.

# from abc_m2.m2 import *
# print(b)
