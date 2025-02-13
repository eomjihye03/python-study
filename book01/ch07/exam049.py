# 시퀀스 자료 연결, 반복: +, *

s1 = "ABCDE"
s2 = "XYZ"
print(s1 + s2) # concatenation

a = [0, 1, 2]
b = [3, 4, 5]
print(a + b)

# print(s1 + a) # TypeError: 같은 타입끼리 연결해야 함.
# print([1, 2, 3] + (4, 5, 6)) # TypeError

print(s2 * 4) # 반복 연결하기
print(a * 3)