# 문자열의 왼쪽을 0으로 채우기
# str.zfill()
#   . width 자릿수에서 빈자리는 0으로 채운다.

print('5'.zfill(4))
print('-5'.zfill(4)) # 부호까지 포함해서 4자리
print('020'.zfill(4)) 
print('1004'.zfill(4)) 
print('12345'.zfill(4)) # 자리수 넘어가면 0 채우지 않음.

