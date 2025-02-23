# 정규표현식 (regular expression) 응용

import re

s = '''\
http://www.static.com:8080/a/jpg
A: https://admin.static-best.io/show?no=1
B: https://static-best.site.org/show.jpg?no=1
http://static best.net/#!/ibare
https://static.net/#!/ibare\
'''

p = re.compile(r'https?:')

# match(): 문자열이 해당 패턴으로 시작하는지 확인
#   . 매칭되면 Match 객체 리턴, 매칭되지 않으면 None 리턴
r = p.match(s) # Match 객체 리턴
print(r, type(r))
print(r.group(), r.start(), r.end(), r.span())

# search(): 문자열에서 해당 패턴을 한 번만 찾는다.
r = p.search(s) # Match 객체 리턴
print(r, type(r))
print(r.group(), r.start(), r.end(), r.span())

# findall(): 문자열에서 해당 패턴과 일치하는 모든 문자열을 찾는다.
#   . 리스트로 반환
r = p.findall(s) # Match 객체 리턴
print(r, type(r))
for s in r:
    print(s)
    