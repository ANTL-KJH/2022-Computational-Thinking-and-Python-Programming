"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW09.3 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - tkinter GUI 기반 Stop Watch를 구현하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.11.04
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.11.04	    v1.0	최초 작성
"""
import time
from tkinter import *

def runTimer():
    global start_time, elapsed_time, prev_elapsed_time, timeText        # 함수 작동에 필요한 global 변수
    if (running):           # stop watch is running
        cur_time = time.time()              # current time
        time_diff = cur_time - start_time   # time diff
        elapsed_time = time_diff + prev_elapsed_time        # elapsed time
        timeText.configure(text="{:7.3f}".format(elapsed_time))
    window.after(10, runTimer)

def start():            # start
    global running, start_time, elapsed_time, prev_elapsed_time
    if (running != True):               # stop watch isn't running
        running = True
        start_time = time.time()
        prev_elapsed_time = elapsed_time

def stop():             # stop
    global running, prev_elapsed_time, elapsed_time        # 함수 작동에 필요한 global 변수
    running = False         # running = False
    prev_elapsed_time = elapsed_time

def reset():            # reset
    global running, elapsed_time, prev_elapsed_time, timeText        # 함수 작동에 필요한 global 변수
    running = False
    elapsed_time = 0.0
    prev_elapsed_time = 0.0
    timeText.configure(text=str(elapsed_time))

def main():
    global running, elapsed_time, prev_elapsed_time, start_time, window, timeText    # stop watch에 사용하는 Gobal 변수
    running = False
    window = Tk()
    timer = 0
    #start_time = time.time()
    #stop_time = time.time()
    elapsed_time = 0.0
    prev_elapsed_time = 0.0
    window.title("My Simple Stop Watch")                    # title
    timeText = Label(window, height=5, text="0", font=("Arial 40 bold"))    # time text
    timeText.pack(side=TOP)

    startButton = Button(window, width=10, text="Start", bg="green", command=start)     # Start button
    startButton.pack(side=LEFT)
    stopButton = Button(window, width=10, text="Stop", bg="red", command=stop)          # stop button
    stopButton.pack(side=LEFT)
    resetButton = Button(window, width=10, text="Reset", bg="yellow", command=reset)    # reset button
    resetButton.pack(side=LEFT)

    runTimer()
    window.mainloop()

if __name__ == "__main__":
    main()
