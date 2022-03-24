# deleteRowColumn.py
##################################################
# description
#   : 행/열 삭제
# parameters
#   1. 대상 엑셀 파일
#   2. 대상 시트 이름
#   3. 삭제하고자 하는 행 번호 혹은 열 문자
##################################################
import sys, xlwings

def main():
    print(sys.argv[0] + " 시작...")
    isPassed = check_validity(sys.argv)
    if not isPassed:
        fail_log()
        return False

    fileName = sys.argv[1]
    sheetName = sys.argv[2]
    target = sys.argv[3]
    print("- '" + fileName + "' 파일의 '" + sheetName + "' 시트에서, " + target, end='')
    print("행을 삭제할게요." if target.isdigit() else ("열을 삭제할게요." if target.isalpha() else ""))

    file = xlwings.Book(fileName)
    sheet = file.sheets(sheetName)

    # 행을 삭제하는 경우
    if target.isdigit():
        sheet.api.Rows(target).Delete()
    # 열을 삭제하는 경우
    elif target.isalpha():
        sheet.api.Columns(target).Delete()
    
    file.save(fileName)

    done_log()


##################################################
# 예외 처리 정의
##################################################
def check_validity(argv):
    isPassed = True
    # Input Argument 개수 검사
    if len(argv) != 4:
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