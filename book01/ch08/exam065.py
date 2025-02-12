# 리스트 요소를 역순으로 만들기: list.reverse()

solarsys = ['태양', '수성', '금성', '지구', '화성']
print(id(solarsys), solarsys)
solarsys.reverse() # 원본을 변경
print(id(solarsys), solarsys)


# list의 값을 역순으로 꺼내주는 reversed 객체를 리턴.
# reversed 객체는 iterable 객체이기 때문에 list로 변경 가능.
solarsys = ['태양', '수성', '금성', '지구', '화성']
solarsys2 = reversed(solarsys) # 역순으로 바꾼 iterable을 리턴.
print(id(solarsys2), type(solarsys2), list(solarsys2))