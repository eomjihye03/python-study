# while문

# while 조건:
#   문장

i = 0
while i < 10:
    print(i, end=' ')
    i += 1

i = -1
while i < 10:
    i += 1
    if (i % 2) == 0:
        continue
    print(i, end=' ')

i = 0
while i < 10:
    if i == 5:
        break
    print(i, end=' ')
    i += 1

