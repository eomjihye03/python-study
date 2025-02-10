# None 상수

v1 = None # 변수에 값이 없음을 의미.
print(type(v1)) # NoneType

v1 = 100
print(type(v1))

def f1():
    pass

print(f1()) # 리턴값이 없으면 None을 리턴함.

if f1(): # Boolean context(논리 값이 있어야 할 장소)에서 None은 False로 간주.
    print("값 리턴")
else:
    print("값 리턴하지 않음")


# := (walrus operator)
# - 값을 할당하면서 동시에 해당 값을 사용할 때.
a = 0
while (x := a ** 2) < 100:
    print(x)
    a += 1