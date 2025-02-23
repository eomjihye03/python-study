# 프로그램 실행 소요 시간 계산
# time.time()

from time import time, sleep

print(time()) # 1970-01-01 00:00:00 UTC 기준으로 경과한 시간 (초)

sleep(1)
print(time()) 
