# 현재 시간을 연-월-일 시:분:초로 출력하기
# time.localtime(), time.strftime()

from time import localtime, strftime

t = localtime() # UTC 기준, 현재 로컬 시간 (+9)
print(t, type(t))
print(f'년도: {t.tm_year}, {t[0]}')
print(f'월: {t.tm_mon}, {t[1]}')
print(f'일: {t.tm_mday}, {t[2]}')
print(f'시: {t.tm_hour}, {t[3]}')
print(f'분: {t.tm_min}, {t[4]}')
print(f'초: {t.tm_sec}, {t[5]}')
print(f'요일: {t.tm_wday}, {t[6]}') # 0이 월요일
print(f'날짜수: {t.tm_yday}, {t[7]}')
print(f'서머타임 여부: {t.tm_isdst}, {t[8]}') 


print(strftime('%Y-%m-%d %H:%M:%S', localtime()))
print(strftime('%x', localtime())) # 월/일/년
print(strftime('%X', localtime())) # 시/분/초
