# for ~ else문

# for 변수 in iterable객체:
#   문장
# else
#   for문이 중간에 멈추지 않고 정상 수행됐을 때 실행할 문장

for i in range(1, 10, 2):
    if i == 5:
        break
    print(i)
else:
    print('완료!')

