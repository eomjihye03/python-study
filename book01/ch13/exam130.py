# 데코레이터: @



def border_report(func):
    def draw_border(content):
        print('-' * 50)
        func(content)
        print('-' * 50)
    return draw_border

def star_report(func):
    def draw_border(content):
        print('*' * 50)
        func(content)
        print('*' * 50)
    return draw_border

@border_report # 애노테이션을 붙였다 뗐다 하기 쉽다. 기능 추가 / 삭제가 쉽다.
def report(content):
    print(content)

# 데코레이터 붙이기 전/후
report('본문내용')

