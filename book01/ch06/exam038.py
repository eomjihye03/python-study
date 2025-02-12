# filter()

# filter(fun, iterable)

# set-builder notation(수학 집합 생성 표기법) => list comprehension(파이썬)

# [표현식 for guard]
# 표현식: 값을 리턴하는 문장 (statement)
# guard: 조건문
a = [x for x in range(101) if (x % 2) == 0]
print(a)


# filter()를 이용한 리스트 생성.
def check_even(x):
    '''짝수인지 검사하는 함수'''
    if (x % 2) == 0:
        return True
    else:
        return False
    
b = [x for x in range(101)]

even_list = filter(check_even, b)
print(type(even_list))
print(list(even_list))
