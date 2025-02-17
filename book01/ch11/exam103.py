# set에서 요소 제거
# set.remove()

s1 = set("abcde")
s1.remove('c')
print(s1)

# s1.remove('x') # 존재하지 않는 항목 삭제 시 KeyError 발생.

s1.discard('x')
print(s1)