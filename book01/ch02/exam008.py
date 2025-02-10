# len()

name = "ABC니나노"
print(len(name))

names: list[str] = ["Damon", "Stefan", True] # 강제성 X
print(len(names))

students: tuple[str, int, bool] = ("Elena", "Bonnie", "Caroline", True)
print(len(students))

age_dict: dict[str, int] = {'Damon': 172, 'Stefan': 166, 'Elena': True}
print(len(age_dict))

evens: set[int] = {2, 4, 6, 8, 10}
print(len(evens))

# __len__ 를 호출.

