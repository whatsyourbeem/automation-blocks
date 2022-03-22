# deleteSpecificFiles.py
##################################################
# description
#   : 폴더 내에서 특정 조건을 만족하는 파일들을 삭제
# parameters
#   1. 삭제하고자 하는 파일들이 들어있는 폴더의 경로
#   2. 조건(1): 타겟 단어를 포함하는 파일을 고를지 포함하지 않는 파일을 고를지 입력
#     - “contains” 혹은 “without” 로 입력해야 함
#   3. 조건(2): 타겟 단어
##################################################
import os, sys, shutil

def main():
    print(sys.argv[0] + " 시작...")
    isPassed = check_validity(sys.argv)
    if not isPassed:
        fail_log()
        return False

    path = sys.argv[1]
    cond = sys.argv[2]
    target = sys.argv[3]

    print(" - " + path + " 에서,")
    print(" - '" + target + "' 이 포함된" if cond=="contains" else("포함되지 않은" if cond=="without" else ""), end='')
    print(" 파일을 찾아서 삭제할게요.")

    fileList = os.listdir(path)
    for fileName in fileList:
        if ((cond=="contains") and (fileName.find(target) != -1)) or ((cond=="without") and (fileName.find(target) == -1)):
            os.remove(path+'\\'+fileName)

    # shutil.copy(origin, dest)
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
    # 조건 정합성 검사
    if (argv[2]!="contains") and (argv[2]!="without"):
        print("두번째 조건이 올바르지 않습니다. 'contains' 혹은 'without'으로 입력해주세요.")
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