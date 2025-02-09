import json

# 파이썬 딕셔너리
data = {
    "name": "소크라테스",
    "age": 70,
    "skills": ["토론", "철학"]
}

# JSON 파일로 저장
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4) # json을 파일로 저장.

# JSON 문자열로 변환
json_str = json.dumps(data, ensure_ascii=False, indent=4) # json을 문자열로 변환.
print(json_str)

# JSON 파일에서 읽기
with open("data.json", "r", encoding="utf-8") as f:
    data_loaded = json.load(f)
print(data_loaded)

# JSON 문자열을 파이썬 객체로 변환
json_str = '{"name": "소크라테스", "age": 70}'
data_dict = json.loads(json_str)
print(data_dict)
