# 함수의 타입 어노테이션

def compute(name: str, kor: int, eng: int, math: int) -> tuple:
    sum = kor + eng + math
    aver = sum / 3
    return (name, sum, aver)

r = compute('Damon', 100, 80, 75)
print(r)

def compute2(kor: int, eng: int, math: int) -> dict[str, int]:
    return {'국어': kor, '영어': eng, '수학': math, '합계': kor + eng + math}
r = compute2(100, 90, 80)
print(r)

def greeting(name: str) -> None:
    print(f'Hello, {name}. Glad to meet you here!')

greeting('Elena')