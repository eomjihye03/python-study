# hex()

print(hex(20), hex(100))
print(hex(20) + hex(100)) # 문자열임을 확인

i1 = int('0x24', base=16) # base를 명시하면 변환 가능.
print(i1)

# bin()
print(bin(20)) # 리턴값은 문자열.
i2 = int('0b0001_0100', base=2)
print(i2)
