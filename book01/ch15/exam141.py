# 예외 처리: 특정 예외 다루기

a = range(10)
try:
    index = int(input('number > '))
    print(a[index])
except ValueError:  
    print("숫자를 입력하세요!!")
except IndexError: 
    print("유효한 범위가 아닙니다.")
except Exception: # 부모 예외를 뒤에 배치해야 한다.
    print("오류 발생!!!")

