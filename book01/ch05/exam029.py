# divmod(): divide, modulus

a = 37
b = 5

print(a / b)
print(a // b)
print(a % b)

print(divmod(a, b)) # tuple로 결과가 나옴.
r1, r2 = divmod(a, b) # tuple unpacking = destructuring 
print(r1, r2)

