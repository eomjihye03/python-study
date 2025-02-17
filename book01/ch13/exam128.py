# 이름없는 한줄짜리 함수 만들기
# lambda

def power(x, y):
    return x ** y

print(power(2, 4))

power2 = lambda x, y: x ** y
print(power2(2, 4))