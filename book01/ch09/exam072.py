# 유니코드 문자열
#   . 문자열에 포함된 문자의 최대 code point 값을 기준으로 문자 크기가 결정된다.
#   . 0x0000 ~ 0x00FF: 문자당 1 byte (ISO-8859-1 코드 값)
#   . 0x0100 ~ 0xFFFF: 문자 당 2 byte (UCS2 = UTF-16 코드 값)
#   . 0x010000 ~ : 문자 당 4 byte (UTF-32 코드 값)

import sys

a = 'ABC' # ISO-8859-1 문자만 있을 때, 1 문자당 1byte
b = 'ABC가각간' # 한글 뮨자가 포함되면, 1 문자당 
c = 'ABC가각간💕' # code point가 0x10000 이상이면 1 문자당 4바이트

print(a, b, c)
print(sys.getsizeof('A'), sys.getsizeof(a)) 
print(sys.getsizeof('가'), sys.getsizeof(b))
print(sys.getsizeof('💕'), sys.getsizeof(c))

# 이모티콘을 함부로 쓰지 마라.

# UTF-8은 무엇인가

with open('ascii.txt', 'wb') as f:
    f.write("ABC".encode('latin-1'))


with open('euckr.txt', 'wb') as f:
    f.write("ABC가각똘똠똥".encode('euc-kr'))

with open('utf16.tzt', 'wb') as f:
    f.write("ABC가각똘똠똥".encode('utf-16'))
    
with open('utf16be.tzt', 'wb') as f:
    f.write("ABC가각똘똠똥".encode('utf-16be'))
       
with open('utf16le.tzt', 'wb') as f:
    f.write("ABC가각똘똠똥".encode('utf-16le'))

with open('utf32.tzt', 'wb') as f:
    f.write("ABC가각똘똠똥".encode('utf-32'))
       
with open('cp949.tzt', 'wb') as f:
    f.write("ABC가각똘똠똥".encode('cp949'))
       
with open('utf8.txt', 'wb') as f:
    f.write("ABC가각똘똠똥".encode('utf-8'))
       