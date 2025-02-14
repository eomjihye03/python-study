# 문자열로 리스트 요소 연결하기: str.join()

a = ['Damon', 'Elena', 'Stefan', 'Kaluse']
print(', '.join(a))

a = ['Damon', 20, False] # TypeError 문자열만 가능
print(', '.join(a))

