# 함수의 타입 어노테이션

def compute(name: str, kor: int, eng: int, math: int) -> tuple:
    sum = kor + eng + math
    aver = sum / 3
    return (name, sum, aver)

r = compute('Damon', 100, 80, 75)
print(r)