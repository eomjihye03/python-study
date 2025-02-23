# 현재 작업 디렉토리 알아내기, 작업 디렉토리 변경하기
# os.getcwd(), os.chdir()

from os import getcwd, chdir

print(getcwd())
chdir('..')
print(getcwd())
chdir('ch17')
print(getcwd())