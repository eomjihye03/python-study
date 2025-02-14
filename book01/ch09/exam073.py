# 문자 코드값 구하기: ord()
#   . 순서대로 문자에 부여한 유니코드 번호 => 서수(ordinal)의 약자
#   . code point라고 부른다. (10진수)

while True:
    s = input("문자 > ")
    if s.lower() == 'q':
        break
    print(f'{s}: {hex(ord(s))}')

