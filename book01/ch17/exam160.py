# 파일 이름 변경 / 파일 이용
# os.rename()

from os import rename

rename('myfile.txt', 'yourfile.txt')
rename('myfile.txt', 'tmp/yourfile.txt')