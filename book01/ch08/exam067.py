# 리스트 요소 무작위로 섞기: random.shuffle(MutableSequence) 

from random import shuffle

solarsys = ['태양', '수성', '금성', '지구', '화성']
print(id(solarsys), solarsys)
print(shuffle(solarsys)) # return 값 None => 원본 변경.
print(id(solarsys), solarsys)