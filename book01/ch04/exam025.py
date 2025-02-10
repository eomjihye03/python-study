# 비트 연산자

a = 0b1010_1100 # 172
b = 0b1100_1010 # 202

print(a & b) # 10진수로 나옴.

print(bin(a & b)) # 1000_1000 
print(bin(a | b)) # 1110_1110
print(bin(a ^ b)) # 0110_0110
print(~a, bin(~a)) # -0b10101101
print(bin(~b)) # -0b11001011

print(a << 1) # 2배 한 효과 => 344
print(a << 2) # 4배 한 효과 => 688
print(a << 3) # 8배 한 효과 => 1376

print(a >> 1) # 2로 나눈 효과 => 86
print(a >> 2) # 4로 나눈 효과 => 43
print(a >> 3) # 8로 나눈 효과 => 21
