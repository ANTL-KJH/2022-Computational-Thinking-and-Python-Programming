"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW09.2 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - tkinter 기반 거리의 단위인 Km와 mile 변환 계산기
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.11.04
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.11.04	    v1.0	최초 작성
"""

from math import *
from tkinter import *
class Km_Mile_Converter:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.Km_Var = DoubleVar()
        Entry(frame, textvariable=self.Km_Var).grid(row=0, column=0)    # Km 입력부
        Label(frame, text='Km').grid(row=0, column=1)

        self.Mile_Var = DoubleVar()
        Entry(frame, textvariable=self.Mile_Var).grid(row=0, column=2)  # Mile 입력부
        Label(frame, text='Mile').grid(row=0, column=3)

        Km_Mile_button = Button(frame, text='Km -> Mile', command=self.KmtoMile)    # Km->Mile 버튼
        Km_Mile_button.grid(row=1, column=0)                                        # 출력

        Mile_Km_button = Button(frame, text='Km -> Mile', command=self.MiletoKm)    # Mile->Km 버튼
        Mile_Km_button.grid(row=1, column=2)                                        # 출력

    def KmtoMile(self):                     # Km -> Mile 변환
        Km = self.Km_Var.get()              # Km Data get
        Mile = Km / 1.60934                 # Calc
        self.Mile_Var.set(round(Mile, 3))   # 계산결과 set

    def MiletoKm(self):                     # Mile -> Km 변환
        Mile = self.Mile_Var.get()          # Mile Data get
        Km = Mile * 1.60934                 # Calc
        self.Km_Var.set(round(Km, 3))       # 계산결과 set

def main():
    window = Tk()
    window.wm_title('Km <-> Mile Converter')        # Title : Km <-> Mile Converter
    app = Km_Mile_Converter(window)                 # Km_Mile_Converter Class 사용
    window.mainloop()


if __name__ == "__main__":
    main()
