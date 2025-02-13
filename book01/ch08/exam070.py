# 튜플 이해하기

t1 = ('Damon', 172, False)
print(type(t1), t1)

t1 = 'Elena', 22, False # 튜플은 괄호 생략 가능.
print(type(t1), t1)

# tuple unpacking I
name, age, working = t1
print(name, age, working)

# tuple unpacking II
name, age, working = 'Stefan', 166, False
print(name, age, working)

name, _, working = 'Stefan', 166, False
print(name, working)

t1[1] = 40 # tuple은 immutable 객체다.