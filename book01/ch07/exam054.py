# (인덱스, 요소) 생성: enumerate(iterable)

a = ['Damon', 'Elena', 'Stefan', 'Bonnie']
for name in a:
    print(name)

a = ['Damon', 'Elena', 'Stefan', 'Bonnie']
for item in enumerate(a):
    print(item)

a = ['Damon', 'Elena', 'Stefan', 'Bonnie']
for item in enumerate(a, start=1):
    print(item)

a = ['Damon', 'Elena', 'Stefan', 'Bonnie'] 
for num, name in enumerate(a, start=1): # tuple unpacking
    print(num, ':', name)


