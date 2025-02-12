# 시퀀스 자료형
#   . Sequence 서브 타입 객체
#   예) str, bytes, memoryview, array.array, bytearray, tuple, list
#   . 특징
#       . 인덱싱(0, 1, 2,...)
#       . 슬라이싱(:)
#       . 연결(+)
#       . 반복(*)
#       . 멤버(in) --> 존재 유무 검사
#       . 크기(len)



from collections.abc import Sequence
from array import array

# (immutable)Sequence
print(issubclass(str, Sequence))
print(issubclass(bytes, Sequence))
print(issubclass(memoryview, Sequence))
print(issubclass(tuple, Sequence))
print(issubclass(range, Sequence))

# MutableSequence
print(issubclass(array, Sequence))
print(issubclass(bytearray, Sequence))
print(issubclass(list, Sequence))


