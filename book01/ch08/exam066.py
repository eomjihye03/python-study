# 리스트 요소 정렬: list.sort()

solarsys = ['태양', '수성', '금성', '지구', '화성']
print(id(solarsys), solarsys)

solarsys.sort() # 원본 변경
# 리턴 값이 None이면 원본을 변경한다.

print(id(solarsys), solarsys)


solarsys = ['태양', '수성', '금성', '지구', '화성']
print(id(solarsys), solarsys)

solarsys.sort(reverse=True) # 원본 변경
# 리턴 값이 None이면 원본을 변경한다.

print(id(solarsys), solarsys)
