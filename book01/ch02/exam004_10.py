# 특별한 식별자: '__이름__' (magic method)

# - 파이썬 내부에서 사용할 목적으로 정의한 식별자
# - 특별한 역할을 수행하는 메서드를 정의.
# - 가능한 개발자는 이 형식으로 식별자를 작성하면 안된다.

class C1:
    ''' 
    클래스를 설명할 때 주석 대신 많이 사용.
    이유: API 문서를 만들 때 사용되기 때문. 
    이런 문자열을 "docstring"이라고 한다.

    터미널에서 다음 명령어를 사용하여 API 문서를 생성할 수 있다.
    $ python3 -m pydoc -w (모듈명) <-- .py 확장자 없이
    '''
    
    def __init__(self):
        '''
        이 함수는 생성자이다. 
        인스턴스를 생성할 때 자동 호출된다.
        '''
        print("__init__() 호출됨.")

    def __len__(self):
        return 100

obj = C1() # 인스턴스 생성할 때 생성자라는 매직 메서드 호출.
print(len(obj)) # 매직 메서드 __len__() 호출

print(obj.__len__()) # 매직 메서드를 직접 호출하는 것은 비추!!

