# 기타 포맷 옵션

# 정렬 포맷
value = 'Damon'
print(f'[{value}]') 
print(f'[{value:10}]') # 10자리. 기본 왼쪽 정렬
print(f'[{value:<10}]') # 10자리. 왼쪽 정렬.
print(f'[{value:>10}]') # 10자리. 오른쪽 정렬.
print(f'[{value:*>10}]') # 10자리. 오른쪽 정렬. 빈자리는 *로 채우기.
print(f'[{value:*<10}]') # 10자리 왼쪽 정렬. 빈자리는 *로 채우기.
print(f'[{value:*^10}]') # 10자리. 가운데 정렬. 빈자리는 *로 채우기.

value = 100
print(f'[{value}]') 
print(f'[{value:10}]') # 10자리. 기본 오른쪽 정렬. 
print(f'[{value:010}]') # 10자리. 빈자리는 0으로 채우기.
print(f'[{value:0<10}]') # 10자리. 왼쪽 정렬.
print(f'[{value:0>10}]') # 10자리. 오른쪽 정렬.
print(f'[{value:*>10}]') # 10자리. 오른쪽 정렬. 빈자리는 *로 채우기.
print(f'[{value:*<10}]') # 10자리 왼쪽 정렬. 빈자리는 *로 채우기.
print(f'[{value:*^10}]') # 10자리. 가운데 정렬. 빈자리는 *로 채우기.

value = 100
print(f'{value}') # 기본 10진수
print(f'{value:#b}') # 2진수
print(f'{value:#d}') # 10진수
print(f'{value:#o}') # 8진수
print(f'{value:#x}') # 16진수

value = 1234567890
print(f'{value}')
print(f'{value:,}') # 세 자리마다 ,를 써라
print(f'{value:_}') # 세 자리마다 _를 써라

# 부동소수점 자릿수 포맷
print(f'[{value}]') 
print(f'[{value:e}]') # e 지수 표기법
print(f'[{value:E}]') # E 지수 표기법
print(f'[{value:.1%}]') # 맨 뒤에 % 붙이기
print(f'[{value:0>10}]') # 10자리. 오른쪽 정렬.
print(f'[{value:*>10}]') # 10자리. 오른쪽 정렬. 빈자리는 *로 채우기.
print(f'[{value:*<10}]') # 10자리 왼쪽 정렬. 빈자리는 *로 채우기.
print(f'[{value:*^10}]') # 10자리. 가운데 정렬. 빈자리는 *로 채우기.