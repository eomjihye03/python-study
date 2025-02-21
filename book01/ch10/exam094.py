# 바이트 문자열을 16진수 표시 문자열로 변환
# bytes.hex()

b = b'ABCabc\xea\xb0\x80\xea\xb0\x81\xea\xb0\x84'
# 내부 메모리: 41 42 43 61 62 63 ea b0 80 ea b0 81 ea b0 84 (바이트 배열)

hex_str = b.hex()
print(type(hex_str), hex_str)

hex_str = b.hex('-')
print(type(hex_str), hex_str)

hex_str = b.hex('-', 2) # 맨 오른쪽을 기준으로 2바이트마다 - 구분자 삽입.

print(type(hex_str), hex_str)

# str: '4142'
# byte 배열: 34 31 34 32
