# 파일 쓰기
#   . f.write(data)

# 텍스트 쓰기 (utf-16 --> utf-8)
with open('test.txt', 'w') as f:
    f.write('ABC012가각간') # 기본으로 utf-8로 인코딩하여 파일에 쓴다.

# 바이너리 형식으로 저장하기 (utf-16 --> bytes(utf-8) --> 바이트 배열)
s = 'ABC012가각간'
b = s.encode() # utf-8로 인코딩한 바이트 문자열 리턴.
with open('test.bin', 'wb') as f:
    f.write(b) # 바이트 문자열