# 텍스트 파일 저장하기
#   . f.write(str): 문자열을 파일에 저장
#   . f.writelines(Iterable): 리스트의 문자열을 파일에 저장

a = ["hello", "nice to meet you"]

with open('mydata1.txt', 'w') as f:
    f.write(a[0])
    f.write(a[1])

with open('mydata2.txt', 'w') as f:
    f.writelines(a[0])
    f.writelines(a[1])

with open('mydata3.txt', 'w') as f:
    f.writelines(a)
