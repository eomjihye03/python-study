# 파일을 열고 자동으로 닫기

# import os
# print(os.getcwd())
# os.chdir('book01/ch17')

with open('myfile.txt', 'w', encoding='utf-8') as f:
    f.write('ABC가각간')

f = open('Damon.jpg', 'rb')
b = f.read(10)
f.close()
print(b)
