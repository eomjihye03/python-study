# 리스트 요소 무작위로 섞기: random.shuffle(MutableSequence) 

from random import shuffle

solarsys = ['태양', '수성', '금성', '지구', '화성']
print(id(solarsys), solarsys)
print(shuffle(solarsys)) # return 값 None => 원본 변경.
print(id(solarsys), solarsys)

# 원본을 변경하지 않고 섞고 싶다면...?
solarsys = ['태양', '수성', '금성', '지구', '화성']
solarsys2 = solarsys.copy()
shuffle(solarsys2)
print(solarsys)
print(solarsys2)