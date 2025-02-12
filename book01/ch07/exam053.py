# 요소의 인덱스 알아내기: s.index(값)

a = ['Damon', 'Elena', 'Stefan', 'Bonnie']
print(a.index('Stefan'))
print(a.index('Caroline'))

b = ['apple', 'pear', 'peach', 'strawberry', 'banna', 'pear', 'strawberry']
print(b.index('pear', 2))
print(b.index('grape')) # ValueError: 없으면 에러.

