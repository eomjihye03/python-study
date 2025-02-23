# 디렉토리 생성 및 제거
# os.mkdir(), os.rmdir()

from os import mkdir, rmdir

mkdir('tmp2')
rmdir('tmp2')
mkdir('tmp') # 파일이 있는 폴더는 삭제할 수 없음.
