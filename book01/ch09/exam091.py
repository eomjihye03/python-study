# 문자열을 바이트 문자열로 변환하기
# str.encode()

s = 'AB가각💕'
b = s.encode() # 기본 인코딩 character set은 utf-8
print(type(b),'defalut:', b) # 41 42 43 ea b0 80 ea b0 81 ea b0 84

b = s.encode('utf-8') 
print(type(b), 'utf-8:', b) # 41 42 43 ea b0 80 ea b0 81 ea b0 84

b = s.encode('utf-16') 
print(type(b), 'utf-16:', b) # ff f3 41 00 42 00 43 00 ea b0 80 ea b0 81 ea b0 84

b = s.encode('utf-16le') # 기본 인코딩 character set은 utf-8
print(type(b), 'utf-16le:', b) 

b = s.encode('utf-16be') # 기본 인코딩 character set은 utf-8
print(type(b), 'utf-16be:', b) 

b = s.encode('utf-32') # 기본 인코딩 character set은 utf-8
print(type(b), 'utf-32:', b) 


s = 'AB가각'

b = s.encode('cp949') # 기본 인코딩 character set은 utf-8
print(type(b), 'cp949:', b) 

b = s.encode('ms949') # 기본 인코딩 character set은 utf-8
print(type(b), 'ms949:', b) 

b = s.encode('euc-kr') # 기본 인코딩 character set은 utf-8
print(type(b), 'euc-kr:', b) 
