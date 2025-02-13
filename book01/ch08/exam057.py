# 리스트에서 요소 삭제하기: del list[i]

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '혜왕성']
del solarsys[3]
print(solarsys)

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '혜왕성']
del solarsys[-1]
print(solarsys)

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '혜왕성']
del solarsys[2:6]
print(solarsys)

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '혜왕성']
del solarsys[:]
print(solarsys)

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '혜왕성']
if '화성' in solarsys:
    idx = solarsys.index('화성')
    del solarsys[idx]
print(solarsys)

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '혜왕성']
solarsys2 = solarsys
del solarsys # 변수를 삭제한다. 변수가 참조하는 객체는 그대로 존재!!
print(solarsys2) 
print(solarsys) # NameError

