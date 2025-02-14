# 문자열에서 특정 문자열을 다른 문자열로 바꾸기
# str.replace()

a = 'Hello, Python, world!'
r = a.replace('Python', 'Java') # str 타입은 immutable 객체다.
print(a)
print(r)

# 파이썬 리턴 값 관례
#   . return 값이 None이면 원본 객체 변경.
#   . return 값이 None이 아니면, 새 객체 생성.
