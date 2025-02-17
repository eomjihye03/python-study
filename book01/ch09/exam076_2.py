# f'' - !s, !r, !a 사용법

class Car:
    def __init__(self, model, maker, cc):
        self.model = model
        self.maker = maker
        self.cc = cc

    # @property
    # def model(self): # getter
    #     return self._model

    # @model.setter # setter는 모델 이름을 앞에 줘야 함.
    # def model(self, value):
    #     if (value == '소나타' or 
    #             value == '제네시스'):
    #             self._model = value
    #     else:
    #          raise ValueError()
    
    
    # built-in function: print() 호출할 때
    # str() 객체 생성할 때
    def __str__(self):
        '''사람이 읽기 쉬운 형태의 문자열'''
        return f'{self.model}, {self.maker}, {self.cc}'

    # build-in function: repr() 호출할 때
    def __repr__(self):
        '''개발자가 디버깅할 때 참고할 객체의 공식적인 문자열 표현'''
        return f'Car("{self.model}", "{self.maker}", {self.cc})'
    
c1 = Car('소나타', '현대자동차', 1980)
c1.model = '©제네시스💕'
print(c1) # __str__() 호출 ==> 없으면 __repr__() 호출
s1 = str(c1) # __str__() 호출 ==> 없으면 __repr__() 호출
print(s1)

s2 = repr(c1) # __repr__ 호출
print(s2)

# PYTHONIC!!!!!!

s3 = ascii(c1) # __repr__() 리턴 값, 단 non-ascii인 경우 \x, \u, \U로 변환.
# ASCII 문자: 변환 없이 그대로
# non-ASCII 문자(0x80 ~ 0xFF): \xHH 문자로 변환 (1byte)
# non-ASCII 문자(0x0100 ~ 0xFFFF): \uHHHH 문자로 변환 (2byte)
# non-ASCII 문자(0x01000 ~ 0x10FFFF): \UHHHHHHHH 문자로 변환 (4byte)
print(s3)

print("*" * 50)

print(f'{c1}') # str() ==> __str__() ==> 없으면 __repr__() 호출
print(f'{c1!s}') # str() ==> __str__() ==> 없으면 __repr__() 호출
print(f'{c1!r}') # repr() ==> __repr__()
print(f'{c1!a}') # ascii() ==> repr() ==> ASCII 문자는 그대로 non-ASCII 문자는 변환.