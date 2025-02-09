# 식별자 (identifier)
# - 변수명, 함수명, 클래스명, 모듈명을 가리키는 용어.
# - 알파벳 대소문자, 숫자, _로 작성할 수 있다.
# - 단, 숫자는 맨 앞에 올 수 없다.
# - 대소문자 구분.
# - 파이썬 3.0부터 유니코드에 속한 문자는 식별자로 작성 가능.
# - 단, 그 외 문자들은 권장 X

a = 100
abc = 100
abc_def = 100
_abc = 100

ABC = 200
Abc = 300

print(abc, ABC, Abc)

# 1abc = 100 (오류)

가나다 = 100
print(가나다)

# _%%% = 100
# print(_%%%) 오류
print('*' * 100)

# NFKC(Normalization Form KC) 변환
# - 파이썬은 코드를 파싱할 때 모든 식별자를 NFKC 형식으로 변환한다. 
# - 문자가 달라도 의미가 같으면 같은 문자로 변환한다.

𝐀 = 100
𝐴 = 200
𝑨 = 300
𝒜 = 400
𝓐 = 500
𝔄 = 600
𝔸 = 700
A = 800

print(𝐀, 𝐴, 𝑨, 𝒜, 𝓐, 𝔄, 𝔸, A)

import unicodedata
print(unicodedata.normalize('NFKC', '𝓐'))
print(unicodedata.normalize('NFKC', '𝔄'))
print(unicodedata.normalize('NFKC', '𝔸'))
