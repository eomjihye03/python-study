# 함수 처리 결과 리턴
# return

# 1)
def reverse(*names):
    result = []
    index = len(names) - 1
    while index >= 0:
        result.append(names[index])
        index -= 1
    return result

# 2)
def reverse(*names):
    result = []
    index = len(names)
    while index > 0:
        result.append(names[index := index - 1])
    return result


r = reverse('Damon', 'Stefan', 'Klause')
print(r)
