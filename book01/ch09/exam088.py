# 문자열 정렬하기
# sorted(), ''.join()

a = "Hello, Python World!"
r = sorted(a) # 문자열을 code point 오름차순으로 정렬한 후 list 객체로 리턴
print(a)
print(r)

print('_'.join(r))
