# copyfile.py
##################################################
# description
#   : 파일을 복사 후 원하는 디렉토리에 붙여넣기
# parameters
#   1. 복사하고자 하는 파일의 경로
#   2. 붙여넣고자 하는 디렉토리의 경로
##################################################
import os, sys, shutil

def main():
    origin = sys.argv[1]
    dest = sys.argv[2]

    # dest 디렉토리가 없다면, 디렉토리 생성
    if not os.path.isdir(dest):
        os.makedirs(dest)

    shutil.copy(origin, dest)


if __name__ == "__main__":
    main()