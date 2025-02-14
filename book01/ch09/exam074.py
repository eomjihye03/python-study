# code point로 문자 알아내기: chr()
#   . code point에 해당하는 문자를 리턴한다.

while True:
    a = input("유니코드 code point 16진수 > ")
    if len(a) == 0:
        break
    print(f'{a}: {chr(int(a, 16))}')    # '0x0041' --> 0x0041 --> 'A'

