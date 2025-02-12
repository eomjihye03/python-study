# 연습

NAME = slice(0, 10)
AGE = slice(10, 17)
SPECIES = slice(17, 28)
SEX = slice(28, 40)

VD = """
01234567891123456789212345678931234567894123456789
 Damon    172    Vampire    Man
 Stefan   166    Vampire    Man
 Elena    22     Human      Woman
 Caroline 22     Human      Woman
"""
itme_lines = VD.split('\n')

for item_line in itme_lines[2:]:
    print(f'이름: {item_line[NAME].lstrip()}')
    print(f'나이: {item_line[AGE].rstrip()}')
    print(f'종: {item_line[SPECIES].lstrip()}')
    print(f'성별: {item_line[SEX].lstrip()}')
    print("--------------------------------------------")

