# 함수의 매개변수와 인자

# default argument
def set_level(character, level=1):
    print(f'{character}의 레벨: {level}')

set_level('Damon', 2)
set_level('Stefan')

def set_level2(character="No Name", level = 1):
    print(f'{character}의 레벨: {level}')

set_level2()
set_level2(2) # default argument가 여러 개 있을 경우 구분이 힘들다. => 키워드 아규먼트를 통해 지정해줘야 한다.
set_level2(level=3) 

# # default argument 뒤에 일반 아규먼트가 올 수 없다.
# def set_level2(level=1, character):
#     print(f'{character}의 레벨: {level}')
# set_level()
# # SyntaxError: parameter without a default follows parameter with a default

# positional variable-length argument
def print_names(*names): # 아규먼트를 튜플 객체로 묶어서 받는다.
    print(names)

# 0개 이상의 아규먼트를 넘길 수 있다.
print_names() 
print_names('Damon')
print_names('Damon', 'Stefan', 'Elena')

# keyword variable-length argument
def print_names2(**names): # 아규먼트를 dict 객체로 묶어서 받는다.
    print(type(names), names)

print_names2()
print_names2(name='Damon', age=20, working=True)

# mixed argument
def print_movie(title, time, *actors):
    print(f'제목: {title}')
    print(f'상영시간: {time}분')
    print(f'배우: {actors}')

print_movie('스터디그룹', 45, '황민현', '땡땡땡', '딩띵딩')
print_movie('스터디그룹', 45)


def print_car(model, maker, **options):
    print(f'모델: {model}')
    print(f'제조사: {maker}')
    for name, value in options.items():
        print(f'{name}: {value}')
print_car('소나타', '현대자동차')
print_car('소나타', '현대자동차', aircon=True, airbag=True, sunroof=False)

# 가변 길이 positional argument + 가변 길이 keyword argument
# 단, keyword argument 뒤에 positional argument가 올 수 없다.
def print_book(title, press, *writers, **options):
    print(f'제목: {title}')
    print(f'출판사: {press}')
    for writer in writers:
        print(writer, end=' ')
    print()
    for key, value in options.items():
        print(f'{key}: {value}')
    
print_book("웹개발 워크북", '프리렉')
print_book("웹개발 워크북", '프리렉', '엄진영', '엄지혜')
print_book("웹개발 워크북", '프리렉', '엄진영', '엄지혜', height=23, width=45)

print_movie('스터디그룹', 45, '황민현', '땡땡땡', '딩띵딩')
print_movie('스터디그룹', 45)




