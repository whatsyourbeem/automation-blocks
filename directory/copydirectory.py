# copydirectory.py
##################################################
# description
#   : 디렉토리 전체 복사 후 원하는 경로에 붙여넣기
# parameters
#   1. 복사하고자 하는 디렉토리
#   2. 붙여넣고자 하는 디렉토리
##################################################
import os, sys, shutil

def fail_log():
    print(sys.argv[0] + " 실패:(")
    for _ in range(100):
        print("#", end='')
    print('')

def main():
    for _ in range(100):
        print("#", end='')
    print('')

    print(sys.argv[0] + " 시작...")
    if len(sys.argv) != 3:
        print("Input 개수가 올바르지 않습니다.")
        fail_log()
        return False

    origin = sys.argv[1]
    dest = sys.argv[2]

    print(origin + " -> 이 폴더를")
    print(dest + " -> 여기로 복사할게요.")

    files = os.listdir(origin)

    # dest 디렉토리가 없다면, 디렉토리 생성
    if not os.path.isdir(dest):
        print("목적지 경로를 찾을 수 없네요ㅠㅠ 제가 생성할게요!")
        os.makedirs(dest)

    for file in files:
        if not os.path.exists(dest+'\\'+file):
            shutil.copy(origin+'\\'+file, dest+'\\'+file)

    print(sys.argv[0] + " 성공:)")

    for _ in range(100):
        print("#", end='')
    print('')

if __name__ == "__main__":
    main()