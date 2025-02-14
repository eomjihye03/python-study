# 날짜 포맷 옵션

from datetime import datetime, timezone

value = datetime.now()
# value = datetime.now(timezone.utc)
print(f'{value}') # 2025-02-14 18:38:44.113432
print(f'년: {value:%Y}, {value:%y}') 
print(f'월: {value:%B}, {value:%b}, {value:%m}') 
print(f'일: {value:%d}') 
print(f'요일: {value:%A}, {value:%a}, {value:%w}') # 일(0)~토(6)
print(f'오전/오후: {value:%p}') 
print(f'시: {value:%H}') 
print(f'분: {value:%M}') 
print(f'초: {value:%S}') 
print(f'마이크로초: {value:%f}') 
print(f'365일: {value:%j}') # 001 ~
print(f'52주: {value:%U}') # 00주부터 카운트~
print(f'로케일 기준 일자 및 시각: {value:%c}') # 지역 기준
print(f'로케일 기준 일자: {value:%x}') 
print(f'로케일 기준 시각: {value:%X}') 
print(f'문자 출력: {value:%Y-%m-%d %% %H:%M%S}') 
