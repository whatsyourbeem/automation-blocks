# mergeTextFile.py
##################################################
# description
#   : 여러 텍스트 파일 합치기
# parameters
#   1. 최종 텍스트 파일의 경로
#   2~. 합치고자 하는 텍스트 파일의 경로 (2개 이상 입력)
##################################################
import sys

def main():
    print(sys.argv[0] + " 시작...")
    isPassed = check_validity(sys.argv)
    if not isPassed:
        fail_log()
        return False
    
    output_filename = sys.argv[1]
    print(output_filename + " -> 이 경로에 텍스트 파일을 생성할게요")

    file_list = sys.argv.copy()
    del file_list[0] # "mergeTextFile.py" 제외
    del file_list[0] # 최종 텍스트 파일 경로 제외

    output_file = open(output_filename, 'w')
    for filename in file_list:
        if ".txt" not in filename:
            print("앗, 이 파일은 '.txt' 포맷이 아니에요. 이 파일은 건너뛸게요. - " + filename)
            continue
        print("다음 텍스트 파일을 합칩니다 - " + filename)
        file = open(filename, 'r')
        for line in file:
            output_file.write(line)
        file.close()
    output_file.close()
    
    done_log()


##################################################
# 예외 처리 정의
##################################################
def check_validity(argv):
    isPassed = True
    # Input Argument 개수 검사
    if len(argv) < 3:
        print("최소 1개 이상의 텍스트 파일을 입력해주세요!")
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