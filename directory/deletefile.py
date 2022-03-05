# deletefile.py
##################################################
# description
#   : 파일 삭제
# parameters
#   1. 삭제하고자 하는 파일의 경로
##################################################
import os, sys, shutil

def main():
    for _ in range(100):
        print("#", end='')
    print('')

    print(sys.argv[0] + " 시작...")
    if len(sys.argv) != 2:
        print("Error: Input 개수가 올바르지 않습니다.")
        print(sys.argv[0] + " 실패:(")
        return False
    
    target = sys.argv[1]
    print(target + " -> 이 파일을 삭제할게요.")

    if not os.path.isfile(target):
        print("앗 삭제하고자 하는 파일이 이미 존재하지 않아요.")
        print(sys.argv[0] + " 실패:(")
        return False
    
    os.remove(target)

    print(sys.argv[0] + " 성공:)")
    for _ in range(100):
        print("#", end='')
    print('')

if __name__ == "__main__":
    main()