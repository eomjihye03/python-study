# 정규표현식 (regular expression) 응용

import re

s = '''\
.brand {
    font-size: 22px;
    color: #ff0000;
    background-color: #00ff00;
    border-color: #ddd;
    margin: 10px 10px 10px 5px;
    padding 2em 1em 2em 1em;
    }\
'''
p = re.compile(r'#[0-9A-Za-z]')
p = re.compile(r'#[0-9A-Za-z][0-9A-Za-z]')
p = re.compile(r'#[0-9A-Za-z][0-9A-Za-z][0-9A-Za-z]')
p = re.compile(r'#[0-9A-Za-z]{6}|#[0-9A-Za-z]{3}')
p = re.compile(r'#[0-9A-Za-z]{3,6}')
p = re.compile(r'#[0-9A-Za-z]+;')
p = re.compile(r'#[0-9A-Za-z]+(?=;)')
r = p.findall(s)
print(r)

