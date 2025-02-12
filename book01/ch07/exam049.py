# 슬라이싱: slice 클래스
#   . 슬라이싱 정보를 다루는 객체
#   . 슬라이싱을 객체화시켜 이름을 부여하면 패턴으로 다루기 편하다.

PRODUCT_NO = slice(0, 4) # 안바꿀거여서 대문자로 적음.
DESCRIPTION = slice(5, 19)
UNIT_PRICE = slice(19, 24)
QUANTITY = slice(26, 31)
TOTAL_PRICE = slice(32, 38)



a = """
01234567891123456789212345678931234567894123456789
   1 aaa             2000     5  50000
                            
 107 bbb            17000     2  34000
  13 ccc           456000     1 456000
"""
itme_lines = a.split('\n')

for item_line in itme_lines[2:]:
    if len(item_line) != 38:
        continue
    print(f'제품번호: {item_line[PRODUCT_NO].lstrip()}')
    print(f'제품명: {item_line[DESCRIPTION].rstrip()}')
    print(f'가격: {item_line[UNIT_PRICE].lstrip()} 원')
    print(f'수량: {item_line[QUANTITY].lstrip()}')
    print(f'합계: {item_line[TOTAL_PRICE].lstrip()}')
    print("--------------------------------------------")

