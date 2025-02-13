# 슬라이싱
#   . s[m:n]: m 이상 n 미만
#   . s[:n]: 0 이상 n 미만
#   . s[m:]: m 이상 모든 요소
#   . s[:-n]: 0 이상 끝에서 n 번째 미만
#   . s[-m:]: 끝에서 m번째 이상 모든 요소
#   . s[:]: 모든 요소

a = "ABCDEFGHIJK"
print(a[3:9])
print(a[:9])
print(a[3:])
print(a[:-5])
print(a[-5:])
print(a[:])
print(a)

print(a[::2])
print(a[3::2])

s1 = slice(3, 9)
print(a[s1])


# 슬라이스 자리에 데이터를 대체하기
a2 = list(a)
a2[3:7] = ['X', 'X', 'X']
print(a2)