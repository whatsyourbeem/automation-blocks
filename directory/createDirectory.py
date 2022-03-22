# createdirectory.py
##################################################
# description
#   : 디렉토리 생성
# parameters
#   1. 생성하고자 하는 디렉토리
##################################################
import os, sys, shutil

def main():
    print(sys.argv[0] + " 시작...")
    isPassed = check_validity(sys.argv)
    if not isPassed:
        fail_log()
        return False

    path = sys.argv[1]

    print(path + " 폴더를 생성할게요.")

    # dest 디렉토리가 없다면, 디렉토리 생성
    if not os.path.isdir(path):
        os.makedirs(path)
    else:
        print("이미 해당 폴더가 존재해요!")

    done_log()


##################################################
# 예외 처리 정의
##################################################
def check_validity(argv):
    isPassed = True
    # Input Argument 개수 검사
    if len(argv) != 2:
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