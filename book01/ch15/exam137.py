# 예외처리: try-except
#   . 실행 중에 예외 상황이 발생했을 때 적절한 조치를 취한 후에 중단 없이 계속 실행하게 해주는 문법.
#
file_names = ['aa.gif', 'bb.gif', 'cc', 'dd.gif']

for file_name in file_names:
    try:
        name, ext = file_name.split('.')
        print(f'파일명: {name}, 확장자: {ext}')
    except:
        print(f'{name} 파일 처리 중 오류 발생!')

