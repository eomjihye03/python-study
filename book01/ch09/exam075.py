# 이스케이프 문자
#   . 특별한 의미를 지니는 문자
#   . \?

print('Hello,\nworld') # Linefeed(LF; 0x0A)
print('ABCDEFGHI,\rworld') # Carriage Return (CR; 0x0D)
print('Hello,\fworld') # Formfeed
print('Hello,\tworld') # Horizontal Tab
print('Hello,\vworld') # Vertical Tab
print('Hello,\b\bworld') # Backspace
print('Hello,\a\a\a\a\a\aworld') # Bell
print('c:\\User\\user1') 
print('Hello, "Brother"')
print('Hello, \'Brother\'')
print("Hello, 'Brother'")
print("Hello, \"Brother\"")
print("A\101\377") # code point(8진수) 0 ~ 377