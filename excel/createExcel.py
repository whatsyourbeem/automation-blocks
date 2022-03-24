# createExcel.py
##################################################
# description
#   : 엑셀 파일 생성
# parameters
#   1. 생성하고자 하는 엑셀 파일
##################################################
import sys, xlwings

def main():
    print(sys.argv[0] + " 시작...")
    isPassed = check_validity(sys.argv)
    if not isPassed:
        fail_log()
        return False

    fileName = sys.argv[1]
    print(fileName + " 엑셀 파일을 생성할게요.")

    file = xlwings.Book()
    file.save(fileName)

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
    if (".xlsx" not in argv[1] and
        ".xls" not in argv[1] and
        ".xlsm" not in argv[1] and
        ".xlsb" not in argv[1] and
        ".xltm" not in argv[1] and
        ".xlam" not in argv[1] and
        ".xltx" not in argv[1]):
        print("저장할 엑셀 파일의 확장자를 다시 확인해주세요. (xlsx, xls, xlsm, xlsb, xltm, xlam, xltx)")
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