# 텍스트 파일을 한 라인씩 읽기
# f.readline(): 한 줄씩 읽기 (개행문자 포함)
# f.readlines(): 모든 줄을 읽어 리스트로 반환

with open('poetry_ko_utf8.txt', 'r') as f:
    line = f.readline()
    while line != '':
        print(f'>> {line[:-1]}')
        line = f.readline()

with open('poetry_ko_utf8.txt', 'r') as f:
    line = f.readlines()
    while line != '':
        print(f'>> {line[:-1]}')
        line = f.readline()

with open('poetry_ko_utf8.txt', 'r') as f:
    while (line := f.readlines()) != '':
        print(f'>> {line[:-1]}')
        line = f.readline()