# 예외 처리: try ~ except ~ else

file_names = ['aa.gif', 'bb.gif', 'cc.gif', 'dd.gif']

try:
    for file_name in file_names:
            name, ext = file_name.split('.')
            print(f'파일명: {name}, 확장자: {ext}')
except:         # 중간에 중단됐을 때 실행.
    print(f'{name} 파일 처리 중 오류 발생!')
else:           # 정상적인 작업 후 실행.
    print("처리 완료!!")