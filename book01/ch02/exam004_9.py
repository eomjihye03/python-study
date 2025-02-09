# 특별한 식별자: '_(wildcard)'

# match 문장
level = 'C'
match level:
    case 'A':
        print("amazing")
    case 'B':
        print("good")
    case _: 
        print("try harder")

print("*" * 50)

# 반복문 (반복만 중요할 때)
for _ in range(5):
    print("*", end=' ')
print()

print("*" * 50)

# 값을 받을 때
name, _, working = ("Damon", 172, False)
print(name, working)

