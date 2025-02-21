# 함수 정의: def

def f1():
    print("Hello")

def f2(name):
    print(f"Hello, {name}")

def f3():
    return "Hello"

def f4(name):
    return f"Hello, {name}"

f1()
r = f1() # None 
print(r)

f2("Damon") # positional argument
f2(name='Elena') # keyword argument

r = f3()
print(r)

r = f4('Damon')
print(r)


