# 파일의 특정 부분만 읽고 복사: f.seek(offset)
#   . 기준(파일 시작)에서 상대 위치
#   . offset: 기준(파일 시작)에서 offset 바이트 위치로 커서 이동.
# utf-8로 인코딩 된 텍스트를 읽을 때 seek()를 사용하여 바이트 이동시 문제가 발생할 수 있다. 

with open('poetry_en.txt', 'r') as f:
    f.seek(3) # 파일 시작에서 3지점 문자로 이동. (0부터 시작.)
    data = f.read(2) # 2문자 읽기
    print(data) 
    f.seek(2)  # 파일 시작에서 5지점 문자로 이동. (0부터 시작.)
    data = f.read(2) # 2문자 읽기
    print(data)

# 주의!
#   . utf-8로 인코딩된 텍스트 파일을 읽을 때 seek() 메서드를 주의해서 사용해야 한다.
#   . seek(offset) 메서드 아규먼트인 offset은 바이트 단위이다.
#   . 따라서 한글을 읽을 때 3 바이트 단위로 이동해야 하므로 offset 계산을 주의해야 한다.