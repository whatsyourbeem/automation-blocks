# copyfile.py
##################################################
# description
#   : 파일을 복사 후 원하는 디렉토리에 붙여넣기
# parameters
#   1. 복사하고자 하는 파일의 경로
#   2. 붙여넣고자 하는 디렉토리의 경로
##################################################
import os, sys, shutil

def main():
    for _ in range(100):
        print("#", end='')
    print('')

    print(sys.argv[0] + " 시작...")
    if len(sys.argv) != 3:
        print("Error: Input 개수가 올바르지 않습니다.")
        print(sys.argv[0] + " 실패:(")
        return False
    
    origin = sys.argv[1]
    dest = sys.argv[2]

    print(sys.argv[1] + " -> 이 파일을")
    print(sys.argv[2] + " -> 여기로 복사할게요.")

    # dest 디렉토리가 없다면, 디렉토리 생성
    if not os.path.isdir(dest):
        print("목적지 경로를 찾을 수 없네요ㅠㅠ 제가 생성할게요!")
        os.makedirs(dest)

    shutil.copy(origin, dest)
    print(sys.argv[0] + " 성공:)")
    
    for _ in range(100):
        print("#", end='')
    print('')

if __name__ == "__main__":
    main()