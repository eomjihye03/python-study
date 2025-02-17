# 생성자(constructor)

class MyClass:
    a = 100
    def __init__(self):
        '''인스턴스를 생성할 때마다 호출됨.'''
        print('MyClass.__init__() 호출됨.')
        self.b = 200

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()