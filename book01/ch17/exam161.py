# 디렉토리에 존재하는 파일 목록 얻기
# os.listdir()
# glob.glob(): 패턴 매칭 가능.

from os import listdir
from glob import glob

r = listdir('./') 
print(r)

r2 = glob('*.txt')
print(r2)

r2 = glob('../**', recursive=True) # 현재 작업 디렉토리 + 하위 디렉토리
for r in r2:
    print(r)