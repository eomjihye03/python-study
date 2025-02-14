# 기타

a = ['1004', '0b0110', '0o777', '0xac00', '-100', 'IX', '⅓', '5²', '50%']

# str.isdecimal(): 10진수
# str.isdigit(): 10진수, 지수
# str.numeric(): 모든 숫자 형태
for value in a:
    print(f'{value:10}', value.isdecimal(), value.isdigit(), value.isnumeric())
print('-' * 50)
