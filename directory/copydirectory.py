# copydirectory.py
##################################################
# description
#   : 디렉토리 전체 복사 후 원하는 경로에 붙여넣기
# parameters
#   1. 복사하고자 하는 디렉토리
#   2. 붙여넣고자 하는 디렉토리
##################################################
import os, sys, shutil

def main():
    origin = sys.argv[1]
    dest = sys.argv[2]

    files = os.listdir(origin)

    # dest 디렉토리가 없다면, 디렉토리 생성
    if not os.path.isdir(dest):
        os.makedirs(dest)

    for file in files:
        if not os.path.exists(dest+'\\'+file):
            shutil.copy(origin+'\\'+file, dest+'\\'+file)


if __name__ == "__main__":
    main()