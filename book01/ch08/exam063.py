# 리스트 확장하기: list.extend()
#   . 다른 리스트의 요소를 복사해온다.

solarsys = ['태양', '수성', '금성', '지구', '화성']
solarsys2 = ['목성', '토성', '천왕성', '해왕성']

print(id(solarsys), solarsys)
print(id(solarsys2), solarsys2)

solarsys.extend(solarsys2) # solarsys += solarsys2 와 같다.
print(id(solarsys), solarsys)
print(id(solarsys2), solarsys2)

solarsys.append(solarsys2) # solarsys2의 주소 자체가 들어감.
print(id(solarsys), solarsys)
print(id(solarsys2), solarsys2)


solarsys = ['태양', '수성', '금성', '지구', '화성']
solarsys2 = ['목성', '토성', '천왕성', '해왕성']
for item in solarsys2:
    solarsys.append(item)
print(solarsys)


solarsys = ['태양', '수성', '금성', '지구', '화성']
solarsys2 = ['목성', '토성', '천왕성', '해왕성']
print(id(solarsys), solarsys)
print(id(solarsys2), solarsys2)
solarsys += solarsys2 # list concatenation은 각 원소를 append
print(id(solarsys), solarsys) # solarsys.extend(solarsys2)
print(id(solarsys2), solarsys2) 