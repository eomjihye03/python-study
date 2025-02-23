# 정규표현식 (regular expression) 응용

import re

s = '<a href="help.html">도움말을 보려면 여기를 클릭하세요</a>\
<font size="15>'

p = re.compile(r'href=".*"', re.I)
p = re.compile(r'href=".*?"', re.I) # 최소 매치

r = p.findall(s)
print(r)