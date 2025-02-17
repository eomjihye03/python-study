# 소멸자(Destructor)

class MyClass:
    a = 100
    def __init__(self):
        '''인스턴스를 생성할 때마다 호출됨.'''
        print('MyClass.__init__() 호출됨.')
        self.b = 200
    def __del__(self):
        '''객체를 삭제할 때 호출됨.'''
        print('MyClass.__del__() 호출됨.')
    
obj1 = MyClass()
del obj1 # __del__() 호출됨.


