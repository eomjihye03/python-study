# set에서 랜덤 요소 추출
# set.pop()

s1 = set('abcde') # 각 항목의 값을 hash 알고리즘으로 계산하여 위치 지정.
print(s1)
print(s1.pop()) # 맨 앞 위치의 값부터 제거
print(s1.pop()) 
print(s1.pop()) 
print(s1.pop())
print(s1.pop())
print(s1.pop()) # 더이상 꺼낼 값이 없다면 KeyError 발생.
