# 정규표현식 (regular expression)
# 반복표현
# *: 0회 이상 반복
# +: 1회 이상 반복
# ?: 0회 또는 1회 반복
# {m}: m회 반복
# {m, n}: m회 이상, n회 이하 반복

# 매칭표현식
# .: 줄바꿈 문자를 제외한 모든 문자와 매치
# ^: 문자열의 시작과 매치
# [^a]: a를 제외한 모든 문자와 매치
# $: 문자열의 끝과 매치 
# \A: 문자열의 처음과 매치
# \Z: 문자열의 끝과 매치
# \b: 단어 경계(word boundary)
# \B: 단어 경계가 아님
# \d: 숫자와 매치
# \D: 숫자가 아닌 것과 매치
# \s: whitespace 문자와 매치
# \S: whitespace 문자가 아닌 것과 매치
# \w: 대소문자 + 숫자와 매치
# \W: 대소문자 + 숫자가 아닌 문자와 매치
# |: 또는
# (): 그룹
# []: 문자집합. 범위 지정은 - 사용.

s = '''\
http://www.static.com:8080/a/jpg
A: https://admin.static-best.io/show?no=1
B: https://static-best.site.org/show.jpg?no=1
http://static best.net/#!/ibare
https://static.net/#!/ibare\
'''

print(s)