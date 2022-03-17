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
    print(sys.argv[0] + " 시작...")
    isPassed = check_validity(sys.argv)
    if not isPassed:
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

    done_log()


##################################################
# 예외 처리 정의
##################################################
def check_validity(argv):
    isPassed = True
    # Input Argument 개수 검사
    if len(argv) != 3:
        print("Input 개수가 올바르지 않습니다.")
        isPassed = False
    return isPassed

##################################################
# Default 영역
##################################################
def fail_log():
    print(sys.argv[0] + " 실패:(")
    print('#'*100)

def done_log():
    print(sys.argv[0] + " 성공:)")
    print('#'*100)

if __name__ == "__main__":
    print('#'*100)
    main()