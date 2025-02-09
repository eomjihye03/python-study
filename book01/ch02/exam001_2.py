# 문자열 리터럴(literal) II

# "", '' 둘이 동일함.
print("Hello")
print('Hello')

# 멀티 라인 문자열: """멀티라인""", '''멀티라인'''
print("""abc
def
ghi""")

print('''abc
    def
    ghi''')

print("*" * 50)

# 한 문장을 여러 줄로 나눠서 작성하기
# 역슬래쉬: 뒤에 나오는 줄바꿈은 실행할 때 제거됨. \ 뒤에 공백이나 다른 문자가 오면 X.
# 1) 문자열
print("Hello\
, Pytho\
n World!")

# 2) 문장
for i in\
        range(1, 10):
    print(i, end=' ') # 키워드 아규먼트는 붙여서 표현.
print()

for i in range(1, 
                10): # 괄호 안의 문장은 \ 없이 다음 줄에 작성 가능.
    print(i, end=' ') 
print()