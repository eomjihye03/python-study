# 문자열을 구분자로 분리하기: str.split()
# split()과 join()은 반대 역할을 한다.

a = 'Damon,Elena,Stefan,Klause,Caroline'
print(a.split(','))

a = 'I      AM      \t \n \t  DAMON'
print(a.split()) # 공백(whitespace; space, tab, newline)으로 분리. 기본.

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=아주대학교'

a = url.split('?')
print(a)

for param in a[1].split('&'):
    name_value = param.split('=')
    print(name_value[0], name_value[1])

for param in a[1].split('&'): # name과 value 으로 unpacking
    name, value = param.split('=')
    print(name, value)

