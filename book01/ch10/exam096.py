# 바이트 문자열에 대해 사용할 수 있는 주요 메서드들

b = b'abcdefgabcdefgabcdefg'

# bytes.replace(): 해당 바이트 문자열을 모두 찾아 변경한다.
b2 = b.replace(b'ab', b'AB') # 새 바이트 문자열 리턴
print(type(b), b)
print(type(b2), b2)

# bytes.find(): 해당 바이트 문자열을 찾아 인덱스를 리턴한다.
index1 = b.find(b'a') 
print(index1)
print(b.find(b'a', 1))
print(b.find(b'a', 8))

# bytes.strip(): 공백제거
b = b'          ABCabc                     '
print(b)
print(b.strip())
print(b.rstrip())
print(b.lstrip())