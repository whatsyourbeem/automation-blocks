# deletefile.py
##################################################
# description
#   : 파일 삭제
# parameters
#   1. 삭제하고자 하는 파일의 경로
##################################################
import os, sys

def main():
    print(sys.argv[0] + " 시작...")
    isPassed = check_validity(sys.argv)
    if not isPassed:
        fail_log()
        return False
    
    target = sys.argv[1]
    print(target + " -> 이 파일을 삭제할게요.")
    
    os.remove(target)

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
    # 삭제하고자 하는 파일이 있는지 검사
    if not os.path.isfile(argv[1]):
        print("앗 삭제하고자 하는 파일이 이미 존재하지 않아요.")
        isPassed = False
    return isPassed

##################################################
# Default 영역
##################################################
def fail_log():
    print(sys.argv[0] + " 실패:(")
    for _ in range(100):
        print("#", end='')
    print('')

def done_log():
    print(sys.argv[0] + " 성공:)")
    for _ in range(100):
        print("#", end='')
    print('')

if __name__ == "__main__":
    for _ in range(100):
        print("#", end='')
    print('')
    main()