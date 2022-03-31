# parseTextorigin.py
##################################################
# description
#   : 텍스트 파일에서 조건에 맞는 문자열을 추출
# parameters
#   1. 대상 텍스트 파일
#   2. 조건1 ("word" 혹은 "line")
#   3. 조건2 ("before" 혹은 "after" 혹은 "contains")
#   4. 타겟 문자열
#   5. 새로 저장할 텍스트 파일
##################################################
import sys

def main():
    print(sys.argv[0] + " 시작...")
    isPassed = check_validity(sys.argv)
    if not isPassed:
        fail_log()
        return False

    origin = sys.argv[1]
    cond1 = sys.argv[2]
    cond2 = sys.argv[3]
    target = sys.argv[4]
    dest = sys.argv[5]

    print(origin + " 에서 '" + target + "'", end='')
    print(" 앞의" if cond2=="before" else(" 뒤의" if cond2=="after" else (" 를 포함하는" if cond2=="contains" else "")), end='')
    print(" 단어를" if cond1=="word" else(" 라인을" if cond1=="line" else ""), end='')
    print(" 추출한 후,")
    print(dest + " 에 저장할게요.")

    origin_file = open(origin, 'r')
    dest_file = open(dest, 'w')
    contents = origin_file.readlines()

    if cond1=='line':
        if cond2=='contains':
            for line in contents:
                if line.find(target)>-1:
                    dest_file.write(line)
        elif cond2=='before':
            for line in contents:
                if line.find(target)>-1:
                    dest_file.write(line.split(target)[0])
        elif cond2=='after':
            for line in contents:
                if line.find(target)>-1:
                    dest_file.write(line.split(target)[1])

    elif cond1=='word':
        if cond2=='contains':
            for line in contents:
                word = line.split(' ')
                for index in range(len(word)):
                    if word[index].find(target)>-1:
                        dest_file.write(word[index])
        elif cond2=='before':
            for line in contents:
                word = line.split(' ')
                for index in range(len(word)):
                    if word[index].find(target)>-1:
                        if index > 0:
                            dest_file.write(word[index-1])
        elif cond2=='after':
            for line in contents:
                word = line.split(' ')
                for index in range(len(word)):
                    if word[index].find(target)>-1:
                        if index < len(word)-1:
                            dest_file.write(word[index+1])
    
    origin_file.close()
    dest_file.close()
    
    done_log()


##################################################
# 예외 처리 정의
##################################################
def check_validity(argv):
    isPassed = True
    # Input Argument 개수 검사
    if len(argv) != 6:
        print("Input 개수가 올바르지 않습니다.")
        isPassed = False
    # 조건 정합성 검사
    if (argv[2]!="word") and (argv[2]!="line"):
        print("두번째 조건이 올바르지 않습니다. 'word' 혹은 'line'으로 입력해주세요.")
        isPassed = False
    if (argv[3]!="before") and (argv[3]!="after") and (argv[3]!="contains"):
        print("세번째 조건이 올바르지 않습니다. 'before' 혹은 'after' 혹은 'contains' 로 입력해주세요.")
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