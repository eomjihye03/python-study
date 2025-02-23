# 파일인지 디렉토리인지 체크
# os.path.isfile()
# os.path.isdir()

from os import listdir
from os.path import isfile, isdir

r = listdir('../ch16')

for filename in r:
    if isfile(f'../ch16/{filename}'):
        print(f" - {filename}")
    elif isdir(f'../ch16/{filename}'):
        print(f"d {filename}")
    else:
        print(f"? {filename}")