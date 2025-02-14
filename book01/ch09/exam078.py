# str.find()

contents = "print(f'요일: {value:%A}, {value:%a}, {value:%w}')"
idx = contents.find('value')
print(idx)

idx = contents.find('value', idx + 1)
print(idx)

idx = contents.find('value', idx + 1)
print(idx)

idx = contents.find('value', idx + 1)
print(idx)