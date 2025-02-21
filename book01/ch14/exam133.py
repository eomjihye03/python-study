# 메서드

class MyClass:
    a = 100
    def __init__(self):
        self.b = 200

    def f1(self):
        print(self.b)
    
    @classmethod
    def f2(cls):
        print(cls.a)

    @staticmethod
    def f3():
        print('f3()')

MyClass.f2() # 클래스 메서드 호출
MyClass.f3() # 스태틱 메서드 호출
MyClass.f1() # 인스턴스 메서드는 인스턴스를 가지고 호출해야 한다.

obj = MyClass()
obj.f1() # 인스턴스 메서드 호출

