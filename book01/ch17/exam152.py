# 파일 읽기
#   . f.read(size): size byte만큼 읽기
#   . 텍스트를 읽는 경우 size의 단위는 문자이다.
#   . f.read() 모든 내용 읽기

# 영문 텍스트 읽기
# with open('poetry_en.txt', 'r') as f:
#     content = f.read()
# print(content)

# 한글 텍스트 읽기
#   . 기본으로 파일 인코딩이 utf-8 이라고 가정한다.
with open('poetry_ko_utf8.txt', 'r') as f:
    content = f.read(10) # 5문자 읽기
print(content)

# 한글 텍스트 읽기
#   . 파일의 인코딩이 utf-8이 아닐 경우 파일을 열 때 알려줘야 한다.
with open('poetry_ko_cp949.txt', 'r', encoding='cp949') as f:
    content = f.read()
print(content)

# 바이너리 파일 읽기
with open('Damon.jpg', 'rb') as f:
    byte_data = f.read(50) # 50 바이트만 읽는다.
print(byte_data.hex(' '))
