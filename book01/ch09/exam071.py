# 문자열 객체
'''
이 문자열은 주석 대신으로 사용하는 경우가 있다. 
문제는 리터럴 문자열이기 때문에 메모리를 차지한다.
주석은 실행할 때 무시되는 것과 다름.
'''

# 주석은 여러 줄 쓰려면
# 맨 앞에 '#'을 붙여야 한다.

s1 = 'he said "you are jerk"'
s2 = "she thought 'haha'"

print(s1, s2)
print("*" * 50)

# 줄 예쁘게 맞추려고 하면 안됨. 
s3 = """aaa 
bbb # 이건 주석이 아니다.
ccc"""
print(s3) 
print("*" * 50)


