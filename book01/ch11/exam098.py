# set 연산: |(합집합), &(교집합), -(차집합), ^(교집합의 여집합)

s1 = set("abcde")
s2 = set("cdefg")

print(s1 | s2) 
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)

s3 = set("ac")
print(s2 <= s1) # s2가 s1의 부분집합이냐
print(s3 <= s1) # s3가 s1의 부분집합이냐
