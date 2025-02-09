# 특별한 식별자: '__이름' (private 멤버)
# - private 멤버
# 외부에서 접근 불가! 강제적.

class C1:
    def __init__(self):
        self.v1 = 100
        self._v2 = 200
        self.__v3 = 300

obj = C1()
print(obj.v1)
print(obj._v2) # protected 멤버 (강제성은 X)
print(obj.__v3) # private 멤버 (강제성 O)