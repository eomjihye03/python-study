# JSON 파일 다루기
# (Java Script Object Notation)

import json

with open('book.json') as f: # 기본적으로 읽기 모드
    data = json.load(f)

print(data)

print(type(data), data)

student = {
    "name": "데이먼",
    "age": 172,
    "alies": ['jerk', 'idiot'],
    'score': {'kor': 10, 'eng': 100}
    }

with open('student.json', 'w') as f:
    json.dump(student, f, indent=4) # non-ascii인 경우 유니코드로 변환.

with open('student2.json', 'w') as f:
    json.dump(student, f, indent=4, ensure_ascii=False) # non-ascii인 경우 UTF-8로 변환
