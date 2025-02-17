# 숫자 왼쪽에 0을 채워서 문자열로 만들기
# format()
# .f''나 str.format() 형식이 같다.

print('[' + format('Dam', '5') + ']')
print('[' + format('Dam', '05') + ']')
print('[' + format('Dam', '>5') + ']')
