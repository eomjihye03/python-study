# str.isalpha()
#   . 문자열이 문자로만 구성되었는지 검사

a = ['Hello', '오징어', 'love 파이썬', 'world!', 'Python3']

for text in a:
    print(f'{text}: {text.isalpha()}')