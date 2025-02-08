# str 객체 캐싱 
# - 리터럴로 str 객체를 생성할 때 캐싱한다.
# - 리터럴끼리 연결은 리터럴로 간주한다.
# - str 객체도 리터럴로 생성될 경우 캐싱하기도 한다.

a1 = 'Hello'
a2 = 'He' + 'llo' # concatenation
print(a1, a2)
print(id(a1), id(a2)) # 리터럴끼리 연결된 것은 리터럴로 간주. => 캐싱됨.

b1 = "He"
b2 = "llo"
b3 = b1 + b2 
print(b3, id(b3)) # 변수와 변수의 연결은 새로운 str 생성. => 캐싱 X

c1 = str("Hello") # 클래스로 str 객체 생성하는 것은 리터럴을 직접 쓰는 것과 동일. 
c2 = str("Hello")
print(c1, c2)
print(id(c1), id(c2))

