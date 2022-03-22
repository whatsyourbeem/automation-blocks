# copySpecificFiles.py
##################################################
# description
#   : 폴더 내에서 특정 조건을 만족하는 파일들을 복사 후, 원하는 경로에 붙여넣기
# parameters
#   1. 복사하고자 하는 파일들이 들어있는 폴더의 경로
#   2. 붙여넣고자 하는 폴더의 경로
#   3. 조건(1): 타겟 단어를 포함하는 파일을 고를지 포함하지 않는 파일을 고를지 입력
#     - “contains” 혹은 “without” 로 입력해야 함
#   4. 조건(2): 타겟 단어
##################################################
import os, sys, shutil

def main():
    print(sys.argv[0] + " 시작...")
    isPassed = check_validity(sys.argv)
    if not isPassed:
        fail_log()
        return False

    path = sys.argv[1]
    dest = sys.argv[2]
    cond = sys.argv[3]
    target = sys.argv[4]

    print(" - " + path + " 에서,")
    print(" - '" + target + "' 이 포함된" if cond=="contains" else("포함되지 않은" if cond=="without" else ""), end='')
    print(" 파일을 찾아서, ")
    print(" - " + dest + " -> 여기로 복사할게요.")

    # dest 디렉토리가 없다면, 디렉토리 생성
    if not os.path.isdir(dest):
        print("목적지 경로를 찾을 수 없네요ㅠㅠ 제가 생성할게요!")
        os.makedirs(dest)

    fileList = os.listdir(path)
    for fileName in fileList:
        if ((cond=="contains") and (fileName.find(target) != -1)) or ((cond=="without") and (fileName.find(target) == -1)):
            shutil.copy(path+'\\'+fileName, dest)

    # shutil.copy(origin, dest)
    done_log()


##################################################
# 예외 처리 정의
##################################################
def check_validity(argv):
    isPassed = True
    # Input Argument 개수 검사
    if len(argv) != 5:
        print("Input 개수가 올바르지 않습니다.")
        isPassed = False
    # 조건 정합성 검사
    if (argv[3]!="contains") and (argv[3]!="without"):
        print("세번째 조건이 올바르지 않습니다. 'contains' 혹은 'without'으로 입력해주세요.")
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