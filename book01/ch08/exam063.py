# 리스트 맨 마지막에 요소 추가하기: list.append(값)

solarsys = ['태양', '수성', '금성', '지구', '화성']

solarsys.append('일론머스크')
print(solarsys)

solarsys += '일론머스크' # 문자열은 sequence이기 때문에 낱개로 추가한다.
print(solarsys)
