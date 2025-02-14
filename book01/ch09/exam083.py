# 문자열에서 좌우 문자/공백 제거하기
# str.strip(), str.lstrip(), str.rstrip()

a = "           Elena   "
print(f'[{a}]') 
print(f'[{a.strip()}]') # strip(): 양쪽 공백 제거
print(f'[{a.lstrip()}]') # lstrip(): 왼쪽 공백 제거
print(f'[{a.rstrip()}]') # rstrip(): 오른쪽 공백 제거

a = 'www.python.com'
print(a.strip())
print(a.strip('wmoc.'))

