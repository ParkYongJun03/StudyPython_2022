import os

print('============')
PRJ_ROOT = os.path.dirname(os.path.abspath(__file__))
print(PRJ_ROOT)  # py 파일이 위치한 경로
print('============')

BASE_DIR = os.path.dirname(PRJ_ROOT)
print(BASE_DIR)  # 프로젝트 기반 폴더 경로
