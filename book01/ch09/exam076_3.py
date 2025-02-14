# :옵션

# 진수 포맷
value = 126
print(f'value: {value}') # 기본 10진수
print(f'value: {value:d}') # 10진수
print(f'value: {value:b}') # 2진수
print(f'value: {value:o}') # 8진수
print(f'value: {value:x}') # 16진수(소문자)
print(f'value: {value:X}') # 16진수(대문자)
print(f'value: {value:c}') # 유니코드 문자

# 부동소수점 자릿수 포맷
value = 123.4567
print(f'value: {value}') # 기본 고정 소수점
print(f'value: {value:f}') # 고정 소수점
print(f'value: {value:.2f}') # 소수점 이하 자릿수 지정(자동 반올림)
print(f'value: {value:10.2f}') # 전체 자릿수(10), 소수점 이하(2), 빈자리(공백)
print(f'value: {value:010.2f}') # 전체 자릿수(10), 소수점 이하(2), 빈자리(0)

# 날짜 포맷
from datetime import datetime

today = datetime.now()
print(f'{today}')
print(f'{today:%Y-%m-%d %a %H:%M:%S}') 