# f' '
#   . 문자열 포맷팅
#   . f'문자열 {expression}...'

name = 'Damon'
print("이름은 " + name + "입니다.")
print("이름은 {}입니다.".format(name))
print(f'이름은 {name}입니다.')
print(F'이름은 {name}입니다.')
print(f"이름은 {name}입니다.")
print(F"이름은 {name}입니다.")

print(f'2 + 3 = {2 + 3}')

# {표현식!s} = {str(표현식)} = {표현식}
# 표현식의 결과를 str 타입으로 변환한다.
print(f'{2 + 3!s} = {str(2 + 3)} = {2 + 3}')

# {표현식!r} = {repr(표현식)}
# 표현식의 결과를 '결과'로 변환한다.
print(f'{name!r} = {repr(name)} = {name}')