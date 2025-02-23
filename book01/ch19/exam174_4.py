# 정규표현식 (regular expression) 응용

import re

s = '''\
<article>
    <h1>Time Cook didn't address Apple's real privacy problem</h1>
    <h2>Time Cook didn't address Apple's real privacy problem</h2>
    <h2>Time Cook didn't address Apple's real privacy problem</h2>
    <h3>Time Cook didn't address Apple's real privacy problem</h1>
    <h4>Time Cook didn't address Apple's real privacy problem</h4>
</article>
'''
# p = re.compile(r'<h1>.+</h1>')
# p = re.compile(r'<h[1-6]>.+</h[1-6]>')
p = re.compile(r'<h([1-6])>.+?</h\\1>')

# 정규표현식 수정: 전체 태그를 포함한 매칭을 캡처

# findall() 대신 finditer()를 사용하여 전체 태그 매칭을 찾음
matches = p.finditer(s)

# 각 매칭된 전체 태그 출력
for match in matches:
    print(match.group(0))  # group(0)은 전체 매칭된 문자열

