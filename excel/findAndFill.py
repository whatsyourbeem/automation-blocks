# findAndFill.py
##################################################
# description
#   : 엑셀 파일에서 특정 조건을 만족하면 특정 셀에 특정 값을 쓰기
# parameters
#   1. 엑셀 파일
#   2. 검색 대상 행 번호 혹은 열 번호
#   3. 조건(1): 타겟 단오를 포함하는 셀을 찾을지 포함하지 않는 셀을 찾을지 입력
#       - "contains" 혹은 "without" 으로 입력해야 함
#   4. 조건(2): 타겟 단어
#   5. 조건을 만족하는 경우 작성할 행 번호 혹은 열 번호
#   6. 조건을 만족하는 경우 작성할 내용
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
    field = sys.argv[3]
    condition = sys.argv[4]
    targetWord = sys.argv[5]
    targetPlace = sys.argv[6]
    content = sys.argv[7]

    # 검색 대상이 행인지 열인지 구분
    searchMode = 'row' if field.isdigit() else 'column'

    print("- '" + fileName + "' 파일의 '" + sheetName + "' 시트를 탐색합니다.")
    print("- " + field, end='')
    print("행에서, " if searchMode=='row' else "열에서, ", end='')
    print("'" + targetWord + "' 단어가 ", end='')
    print("포함된 " if condition=="contains" else "포함되지 않은 ", end='')
    print("열을 찾아," if searchMode=='row' else "행을 찾아,")
    print("- 해당하는 열의 " if searchMode=='row' else "- 해당하는 행의 ", end='')
    print(targetPlace, end='')
    print("행에, " if searchMode=='row' else "열에, ", end='')
    print("'" + content + "' 라고 작성 후 저장할게요.")

    file = xlwings.Book(fileName)
    sheet = file.sheets(sheetName)
    last_row = sheet.range(field + str(sheet.cells.last_cell.row)).end('up').row
    last_column = sheet.range(get_column_name(sheet.cells.last_cell.column) + field).end('left').column
    
    # 행에서 탐색하는 경우
    if searchMode=='row':
        for i in range(1, last_column+1):
            # 비교 대상 값
            value = sheet.range(get_column_name(i)+field).value
            if (((condition=="contains") and (targetWord in value)) or
                ((condition=="without") and (targetWord not in value))):
                sheet.range(get_column_name(i)+targetPlace).value = content
    # 열에서 탐색하는 경우
    elif searchMode=='column':
        for i in range(1, last_row+1):
            # 비교 대상 값
            value = sheet.range(field+str(i)).value
            if (((condition=="contains") and (targetWord in value)) or
                ((condition=="without") and (targetWord not in value))):
                 sheet.range(targetPlace+str(i)).value = content

    file.save(fileName)

    done_log()

# Column 번호를 문자로 변환하는 함수
def get_column_name(n):
    name = ''
    while n > 0:
        n, r = divmod(n-1, 26)
        name = chr(r + ord('A')) + name
    return name

##################################################
# 예외 처리 정의
##################################################
def check_validity(argv):
    isPassed = True
    # Input Argument 개수 검사
    if len(argv) != 8:
        print("Input 개수가 올바르지 않습니다.")
        isPassed = False
    # 엑셀 파일의 확장자 검사
    if (".xlsx" not in argv[1] and
        ".xls" not in argv[1] and
        ".xlsm" not in argv[1] and
        ".xlsb" not in argv[1] and
        ".xltm" not in argv[1] and
        ".xlam" not in argv[1] and
        ".xltx" not in argv[1]):
        print("저장할 엑셀 파일의 확장자를 다시 확인해주세요. (xlsx, xls, xlsm, xlsb, xltm, xlam, xltx)")
        isPassed = False
    # 검색 대상에 행/열이 섞여 있는지 검사
    if not argv[3].isalpha() and not argv[3].isdigit():
        print("검색 대상이 잘못 되엇습니다. 행의 번호 또는 열의 문자를 입력하셔야 합니다.")
        isPassed = False
    # 조건 정합성 검사
    if (argv[4]!="contains") and (argv[4]!="without"):
        print("4번째 조건이 올바르지 않습니다. 'contains' 혹은 'without'으로 입력해주세요.")
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