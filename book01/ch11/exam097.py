# set 자료형
#   . Iterable 객체
#   . value의 hash 값을 기준으로 저장 위치 결정. => 순서 없음.
#   . 중복 허용 안함.

s = {'apple', 'grape', 'peach', 'strawberry', 'tangerin'}
print(s)

# str -------------> set
s = "helloworld"
s2 = set(s) # 순서가 다르고, 중복 제거
print(s2) 

# tuple --------------> set
s = ('apple', 'apple', 'grape', 'grape', 'peach', 'strawberry', 'tangerin')
s2 = set(s)
print(s2)