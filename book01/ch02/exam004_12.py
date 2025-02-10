# 객체 생성
# - 리터럴, 클래스, 표현식, 함수에서 생성한다.

a1 = 100
a2 = int(100)

b1 = 3.14
b2 = float(3.14)

c1 = 3.5 + 5.4j
c2 = complex(3.5 + 5.4j)

d1 = True
d2 = bool(True)

e1 = 'Hello'
e2 = str('Hello')

f1 = b'ABC'
f2 = bytes(b'ABC')

# list
g1 = [] 
g2 = list()
g1 = [100, 200]
g2 = list(100, 200) # 에러!!!!
g2 = list([100, 200]) # 리스트로 넘겨 줘야함.

# tuple
h1 = ()
h2 = tuple()
h1 = (100, 200)
h2 = tuple(100, 200) # 에러!!! 
h2 = tuple([100, 200]) # 리스트로 넘겨서 튜플로 변환.

h1 = (1) # 값이 한 개 있으면 괄호는 일반괄호로 인식. 
print(type(h1)) # int라고 나옴.
h1 = (1, ) # 끝에 콤마를 붙이면 튜플로 인식.
print(type(h1))

# set
i1 = {} # set이 아님!!!!!!! 기본은 빈 dict 객체.
print(type(i1))
i2 = set()
i1 = {1} # 최소 한 개 항목이 있어야만 set 객체를 만든다.
i2 = set([1])

# dict
j1 = {}
j2 = dict()
j1 = {'name': 'Stefan', 'age': 166}
j2 = dict(name='Damon', age=172, working=False)

print(j1, j2)
