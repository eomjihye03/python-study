# 예외 처리: try ~ except Exception as e

file_names = ['aa.gif', 'bb.gif', 'cc', 'dd.gif']

try:
    for file_name in file_names:
            name, ext = file_name.split('.')
            print(f'파일명: {name}, 확장자: {ext}')
except Exception as e:        
    print(f'{name} 파일 처리 중 오류 발생!')
    print(f'예외 클래스 이름: {e.__class__.__name__}')
    print(f'예외 내용: {e.__str__()}')

s = "Hello"
print(s.__class__)
print(s.__class__.__name__)
print(s.__str__())
print(s.__repr__()) # 객체를 만든건 보여줌.

