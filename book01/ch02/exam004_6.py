# 키워드는 식별자로 사용 X
# ex) False None True and as assert async await 
# break class continue def del elif else except finally 
# for from global if import in is lambda nonlocal not or pass 
# raise return try while with yield

# and = 100 (X)
# class = 200 (X)


print(abs(-100))

# 기존 함수 이름을 덮어쓰지 않도록 해야 한다.
# 파이썬은 이에 대한 방어가 없음.
abs = 300 # 내장 함수를 식별자로 사용.
print(abs)
print(abs(-100)) 

