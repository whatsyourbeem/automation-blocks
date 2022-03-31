# createTextFile.py
##################################################
# description
#   : .txt 파일 생성
# parameters
#   1. 생성하고자 하는 파일의 경로 (파일명 포함)
#   2. 텍스트 파일 내용 (개행의 경우 \n으로 표시)
##################################################
import os, sys

def main():
    print(sys.argv[0] + " 시작...")
    isPassed = check_validity(sys.argv)
    if not isPassed:
        fail_log()
        return False

    path = sys.argv[1]
    content = sys.argv[2]

    print(path + " -> 이 경로에 텍스트 파일을 생성할게요")

    # 디렉토리가 없다면, 디렉토리 생성
    if not os.path.isdir(os.path.dirname(path)):
        print("목적지 경로를 찾을 수 없네요ㅠㅠ 제가 생성할게요!")
        os.makedirs(os.path.dirname(path))

    f = open(path, 'w')
    content_list = content.split('\\n')
    for line in content_list:
        f.write(line + '\n');
    f.close()
    
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