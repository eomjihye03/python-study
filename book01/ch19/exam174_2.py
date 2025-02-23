# 정규표현식 (regular expression) 응용

import re

s = '''\
http://www.static.com:8080/a/jpg
A: https://admin.static-best.io/show?no=1
B: https://static-best.site.org/show.jpg?no=1
http://static best.net/#!/ibare
https://static.net/#!/ibare\
'''
# p = re.compile(r'https?://')
# p = re.compile(r'https?://www')
# p = re.compile(r'https?://\w')
# p = re.compile(r'https?://\w+')
# p = re.compile(r'https?://[^:/\s]')
# p = re.compile(r'https?://[^:/\s]+')
# p = re.compile(r'https?://[^:/\s]+\.\w+')
# p = re.compile(r'https?://[^:/\s]+\.\w+:\d+')
# p = re.compile(r'https?://[^:/\s]+\.\w+(?::\d+)?')
# p = re.compile(r'^https?://[^:/\s]+\.\w+(?::\d+)?') # 무조건 이 규칙으로 시작해야함. ^가 대괄호 밖이랑 안에서의 의미가 다름.
p = re.compile(r'^https?://[^:/\s]+\.\w+(?::\d+)?', re.M) # 멀티라인 모드

r = p.findall(s)
print(r)

