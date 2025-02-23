# 바이너리 파일 복사하기
# f.read()
# f.write()

with open('test.jpg', 'rb') as f:
    with open('test_copy.jpg', 'wb') as h:
        while data := f.read(1024):
            h.write(data)