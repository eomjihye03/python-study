# 리스트 복사하기: list.copy()
#   . shallow copy를 수행한다.

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '혜왕성']

solarsys2 = solarsys.copy() # 리스트 값을 그대로 복사하여 새 list 생성
solarsys2.remove('지구')
print(solarsys)
print(solarsys2)

# shallow copy 확인!
a = [[], [], []]
b = a.copy()
b[1].append('Hehehe')
print(a)
print(b)

a.append(100)
b.append(True)
print(a)
print(b)

c = a # 이건 복제가 아니라 참조임.

