# sendmail.py
##################################################
# description
#   : 메일 전송
# parameters
#   1. 나의 메일 주소
#   2. 나의 메일 계정 비밀번호
#   3. 받는 메일 주소(여러 명일 경우 ', '(콤마+스페이스)로 구분)
#   4. 메일 내용(.txt 파일 경로)
#   5. 첨부 파일 경로(여러 개일 경우 ', '(콤마+스페이스)로 구분)
#   6. 참조 메일 주소(여러 명일 경우 ', '(콤마+스페이스)로 구분)
# Readme!
#   IMAP 설정 방법 (Gmail)
#   1. Gmail 상에서 톱니바퀴 버튼 클릭 후 "모든 설정 보기" 클릭
#   2. "전달 및 POP/IMAP" 카테고리 선택 후 "IMAP 액세스" 에서 "IMAP 사용" 선택
#   비밀번호 생성 방법 (Gmail)
#   1. https://myaccount.google.com/security 접속
#   2. 2단계 인증 사용 설정하기
#   3. 앱 비밀번호 설정
#   IMAP 설정 방법 (NAVER)
#   https://help.naver.com/support/contents/contents.help?serviceNo=532&categoryNo=11047
##################################################
import os, sys, shutil, smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
from email.mime.base import MIMEBase
from email.encoders import encode_base64

def main():
    print(sys.argv[0] + " 시작...")
    isPassed = check_validity(sys.argv)
    if not isPassed:
        fail_log()
        return False

    # 필수 입력
    my_account = sys.argv[1]
    my_password = sys.argv[2]
    to_email = sys.argv[3]
    # 선택 입력
    content = sys.argv[4] if len(sys.argv)>4 else '본문 없음'
    title = os.path.splitext(os.path.basename(content))[0] if content!='' else '제목 없음'
    attachments = sys.argv[5] if len(sys.argv)>5 else '첨부 없음'
    cc_email = sys.argv[6] if len(sys.argv)>6 else ''

    # 입력 확인
    print("- 보내는 사람: " + my_account)
    print("- 받는 사람: " + to_email)
    print("- 제목: " + title)
    print("- 내용: " + content)
    print("- 첨부: " + attachments)
    print("- 참조: " + cc_email)

    # SMTP 설정
    if 'naver.com' in my_account:
        smtp_server = "smtp.naver.com"
        smtp_port = 587
    elif 'gmail.com' in my_account:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
    else:
        print('메일 주소를 확인해 주세요. 현재 지메일,네이버 만 지원합니다ㅠㅠ')
        fail_log()
        return False
    
    # 메일 컨텐츠 설정
    message = MIMEMultipart()
    # 보내는 사람
    message['From'] = my_account
    # 받는 사람
    message['To'] = to_email
    # 참조
    message['Cc'] = cc_email
    # 날짜
    message['Date'] = formatdate(localtime=True)
    # 제목
    message['Subject'] = Header(s=title, charset='utf-8')
    # 본문
    f = open(content, 'r', encoding='utf8')
    body = MIMEText(f.read())
    f.close()
    message.attach(body)
    # 첨부
    if attachments!='첨부 없음':
        try:
            attachments_list = attachments.split(', ')
            for file in attachments_list:
                part = MIMEBase('application', "octet-stream")
                part.set_payload(open(file,"rb").read())
                encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"' %os.path.basename(file))
                message.attach(part)
        except:
            print('첨부 파일이 잘못 입력되었습니다.')
            print(' - 입력하신 경로에 파일이 있나요?')
            print(' - 파일이 여러 개인 경우 ", "(콤마+스페이스) 로 정확히 구분하셨나요?')
            fail_log()
            return False

    try:
        # SMTP 초기화
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        # SMTP에게 Hello 보내기
        smtp.ehlo
        # SMTP 시작
        smtp.starttls()
    except:
        print(smtp_server+'서버가 응답하지 않아요ㅜㅜ 인터넷 연결을 확인해 주세요.')
        fail_log()
        return False
    
    try:
        # SMTP 로그인
        smtp.login(my_account , my_password)
    except:
        print('계정 혹은 비밀번호가 일치하지 않아요ㅜㅜ 다시 한 번 확인해 주세요.')
        print('(여기서 비밀번호란 실제 계정의 비밀번호를 의미하는 것이 아닙니다. 자세한 내용은 가이드 문서를 참고해주세요.)')
        fail_log()
        return False
    
    try:
        smtp.send_message(message)
    except:
        print('이메일 전송에 실패했어요ㅜㅜ')
        fail_log()
        return False

    smtp.quit()
    
    done_log()


##################################################
# 예외 처리 정의
##################################################
def check_validity(argv):
    isPassed = True
    # Input Argument 개수 검사
    if len(argv) < 4:
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