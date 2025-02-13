# 리스트에서 특정 위치 요소 추출 후 삭제: list.pop(위치)

solarsys = ['태양', '수성', '금성', '지구', '화성']
value = solarsys.pop() # LIFO: Last In First Out
print(solarsys, value)

value = solarsys.pop(1) 
print(solarsys, value)

# 원본을 바꿈.

