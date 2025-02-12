# 리스트에서 요소 삭제하기 2: list.remove(값)
#   . 순서 상 제일 처음 찾은 값을 제거. 
#   . 중복 되는 경우 하나만 지움.

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '혜왕성']

solarsys.remove('화성')
print(solarsys)

# solarsys.remove('치킨') # 존재하지 않는 값을 지우라고 하면
# print(solarsys) # ValueError 발생!!!

if '치킨' in solarsys:
    solarsys.remove('치킨')

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '혜왕성', '화성']
solarsys.remove('화성')
print(solarsys)

