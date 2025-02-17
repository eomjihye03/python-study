# 바이트 문자열 이해하기

s = "ABCabc"
b = b"ABCabc"
print(s[0], b[0])

print(type(s[0]), type(b[0]))

b1 = b'ABC'
# b2 = b'가각간' # ASCII 문자만 가능.

# non-ASCII 문자를 바이트 배열로 화면에 표현하려면?
#   . \xHH (HH: 문자의 16진수 코드 값)

b = 'ABCabc가각간'.encode('utf-8') # utf-16 (str) ==> utf-8 (bytes)
print(type(b), b) 
# bytes: 41 42 43 61 62 63 ea b0 80 ea b0 81 ea b0 84

s = b.decode('utf-8') # utf-8 (bytes)==> utf-16 (str)
print(type(s), s)

