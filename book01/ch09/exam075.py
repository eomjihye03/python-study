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
print("A\101\377") # code point(8진수) 0 ~ 377 => REPL 환경에서는 0~377 유효.
print("\N{SMILING FACE WITH SUNGLASSES}") # \N{문자에 부여된 이름}
print('\u0041\uac00') # \uxxxx (16진수 unicode code point)
print('\U0001f495') # \Uxxxxxxxx (4바이트 16진수 unicode code point)