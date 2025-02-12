# 리스트에 요소 삽입: list.insert()

solarsys = ['태양', '수성', '금성', '지구', '화성']
solarsys.insert(2, '달')
print(solarsys)

solarsys = ['태양', '수성', '금성', '지구', '화성']
solarsys.insert(-1, '일론머스크')
print(solarsys)

solarsys = ['태양', '수성', '금성', '지구', '화성']
solarsys.insert(100, '일론머스크')
solarsys.insert(-100, '일론머스크')
print(solarsys)
print(len(solarsys))

