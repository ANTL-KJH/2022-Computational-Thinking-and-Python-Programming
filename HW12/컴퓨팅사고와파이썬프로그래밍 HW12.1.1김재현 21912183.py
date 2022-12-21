"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW12.1.1 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - text chat program with socket communication, client ver
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.11.25
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.11.25	    v1.0	최초 작성
"""

from Class_TextChat import *

# client ver
def main():                                 # main
    print("Running TCP Client")
    textChatClient = TextChat('Client')     # role = client
    textChatClient.win.mainloop()


if __name__ == "__main__":
    main()