# 클래스 변수와 인스턴스 변수

class MyClass:
    a = 100
    def __init__(self):
        self.b = 200

MyClass.a = 400
print(MyClass.a)
print(MyClass.b) # b는 인스턴스 변수다.

obj1 = MyClass()
obj2 = MyClass()
obj1.b += 50
obj2.b += 70
print(obj1.b, obj2.b)