# 타입 힌팅

name = "Stefan"
age = 166
working = False
weight = 72.5

print(name, age, working, weight)

# 변수에 타입 정보를 지정할 수 있다.
# 가독성 및 유지보수를 용이하게 함. 
# 단, 강제성은 없다.

name2: str = "Stefan"
age2: int = 166
working2: bool = False
weight2: float = 72.5

name2 = 100 # 타입 힌트와 다른 타입의 값을 넣어도 에러 X

print(name2, age2, working2, weight2)

names: list[str] = ["Damon", "Stefan", True] # 강제성 X
print(names)

students: tuple[str, int, bool] = ("Elena", "Bonnie", "Caroline", True)
print(students)

age_dict: dict[str, int] = {'Damon': 172, 'Stefan': 166, 'Elena': True}
print(age_dict)

# 변수에 지정한 타입 힌트를 모두 출력.
print(__annotations__)

def plus(a: int, b: int) -> int:
    return a + b

r = plus(1, 2)
print(r)