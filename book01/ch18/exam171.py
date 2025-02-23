# 올해의 경과된 날짜 수 계산
# time.localtime()

from time import localtime, strftime

t = localtime()
today = strftime('%Y-%m-%d', t)
print(today)
print(f'{t.tm_year}년 1월 1일 기준으로 {t.tm_yday}일째 되는 날')

weekdays = ['월', '화', '수', '목', '금', '토', '일']
print(f'{weekdays[t.tm_wday]}요일 입니다.')
