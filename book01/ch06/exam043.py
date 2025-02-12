# 모든 요소가 참인지 거짓인지 확인: all(), any()
#   . all(iterable 객체): 모든 요소가 참일 때만 True 리턴.
#   . any(iterable 객체): 참이 하나라도 존재하면 True 리턴.

# 값을 bool 타입으로 따졌을 때

print(bool(1)) # True
print(bool(-1)) # True
print(bool(0)) # False
print(bool(0.0)) # False
print(bool(3.14)) # True
print(bool(0.00000001)) # True
print(bool(3 + 3j)) # True
print(bool('')) # False
print(bool('True')) # True
print(bool('False')) # True
print(bool(b'0000_0000')) # True
print(bool(b'')) # False
print(bool([])) # False
print(bool([1])) # True
print(bool(())) # False
print(bool((1,))) # True
print(bool(set())) # False
print(bool({1, 2})) # True
print(bool({})) # False
print(bool({'name': 'Damon'})) # True
print(bool(None)) # False
print(bool(...)) # True

a = [0, 1, 2, 3, 4]
print(all(a)) # False
print(any(a)) # True

b = [0, False, '', [], (), set(), {}, None]
print(all(b)) # False
print(any(b)) # False




