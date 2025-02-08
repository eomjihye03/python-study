# 리터럴(literal): 값을 표현하는 방법

# 수치
print(100) # 정수
print(3.14) # 부동소수점
print(3.4 + 5.6j) # 복소수
print(True, False) # 논리값

# 시퀀스
# - 순서가 있고, 인덱스로 값을 조회할 수 있는 값 목록
print("ABC012가각간\uAC00\U0001D54F") # 문자열
# Unicode(0x000000~0x10fff) 문자는 \uXXXX, \UXXXXXXXX 형태로 적는다.

print(f"3 * 5 = {3 * 5}") # f문자열

print(b"ABC012\xC2\xA9") # 바이트 배열: "ABC012©"의 UTF-8 인코딩
print(b"ABC012\xC2\xA9".decode("UTF-8")) # UTF-8 바이트배열 ==> UTF-16BE
print("ABC012©".encode("UTF-8")) # UTF-16BE => UTF-8 바이트배열

# ASCII(0x00 ~ 0x7F) 문자는 그대로 적는다. 예) ABX
# non-ASCII(0x80 ~ 0xFF)는 \xHH 형태로 적는다. 예) \xa4


print(["홍길동", "임꺽정", "유관순", "Elena"]) # 리스트
print(("홍길동", "임꺽정", "유관순", "Elena")) # 튜플 (read only)

# 집합 (set)
print({"홍길동", "임꺽정", "유관순", "임꺽정"}) 


# 맵
# - 키와 값 형태로 저장된 목록
print({"name": "Damon", "age": 177, "working": False})

# None
print(None)

# ... Ellipse
print(...)

