# 바이트 문자열을 유니코드 문자열로 변환하기
# bytes.decode()

b = b'ABCabc\xea\xb0\x80\xea\xb0\x81\xea\xb0\x84'
# 내부 메모리: 41 42 43 61 62 63 ea b0 80 ea b0 81 ea b0 84 (바이트 배열)

str_data = b.decode() # 기본(utf-8) ==> utf-16 문자열
print(type(str_data), str_data)

str_data = b.decode('utf-8') # 기본(utf-8) ==> utf-16 문자열
print(type(str_data), str_data)

print(b'ABab'.decode('utf-8')) # ASCII ==> utf-16
# print(b'Abab가각'.decode('utf-8'))
print(b'ABab\xea\xb0\x80\xea\xb0\x81'.decode('utf-8')) # utf-8 ==> utf-16
print(b'ABab\xb0\xa1\xb0\xa2'.decode('euc-kr')) # euc-kr ==> utf-16
print(b'AB\xb0\xa1\xb0\xa2'.decode('cp949')) # cp949 ==> utf-16
print(b'\x00\x41\x00\x42\xac\x00\xac\x01'.decode('utf-16be')) # utf-16be ==> utf-16
print(b'\x41\x00\x42\x00\x00\xac\x01\xac'.decode('utf-16le')) # utf-16 ==> utf-16

# 파이썬에서 바이트 배열을 만드는 방법
# 예) 바이트 문자열로 만들기
b'AB\xea\xb0\x80' # 바이트 문자열

# 자바에서 바이트 배열을 만드는 방법
# byte[] = new bytes[] {0x41, 0x42, 0xea, 0xb0, 0x80}