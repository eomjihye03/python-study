# 파일을 열고 닫기

import os
print(os.getcwd())
os.chdir('book01/ch17')

f = open('myfile.txt', 'w', encoding='utf-8')
f.write('ABC가각간')
f.close()

f = open('Damon.jpg', 'rb')
b = f.read(10)
f.close()
print(b)
