# 문자열 저장
# 문자열을 메모리에 저장할 때 문자열에 포함된 문자 중에서 
# '가장 큰 코드 값(코드포인트)'의 크기로 통일. 
# 1, 2, 4 바이트 중 하나로 결정.
# 코드포인트: 문자에 대해 부여한 유니코드 정수값

import sys
# 1) 영문자만 있으면 모든 문자는 한 문자 당 1byte 차지. (Latin-1)
print(sys.getsizeof("A")) # 42 byte
print(sys.getsizeof("ABC")) # 44 byte --> 한 문자당 1byte

# 2) 한글이 포함되어 있으면 모든 문자는 한 문자 당 2byte 차지. (UTF-16)
print(sys.getsizeof("가")) # 60 byte
print(sys.getsizeof("가각간")) # 64 byte --> 한 문자당 2byte
print(sys.getsizeof("가각간ABC")) # 70 byte --> 한 문자당 2byte

# 3) 2byte 초과 특수 문자가 있으면 모든 문자는 한 문자 당 4byte 차지. (UTF-32)
print(sys.getsizeof("𝕏"))
print(sys.getsizeof("𝕏𝕏")) # 한 문자당 4byte
print(sys.getsizeof("가각간ABC𝕏")) # 88 byte --> 한 문자당 4byte


# 참고!
# - 문자열을 UTF-16으로 바꿀 때 
print("AB가각".encode("UTF-16")) # ff fe 41 00 42 00 ac 01 ac
print("AB가각".encode("UTF-16BE")) # 00 41 00 42 ac 00 ac 01
print("AB가각".encode("UTF-16LE")) # 41 00 42 00 00 ac 01 ac
print("AB가각".encode("UTF-8")) # 41 42 ea b0 80 ea b0 81

# Big-endian: MSB가 상위 비트에 저장.
# Little-endian: LSB가 상위비트에 저장. 

