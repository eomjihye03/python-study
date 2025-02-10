# 자료형 변환

i = int(3.14) # 반올림 없이, 소수점 부분을 삭제함.
print(i, type(i))

i = int('314')
print(i, type(i))

# i = int('3.14') # 정수로 못바꾸는 문자열인 경우 오류!
# print(i, type(i))

f = float('3.14')
print(f, type(f))

f = float('0.0314e2')
print(f, type(f))

print(str(123), str(3.14), str(0.0314e2))