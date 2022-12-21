"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW13.1 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - Analog Clock testing with turtle graphics
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.12.02
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.12.02	    v1.0	최초 작성
"""
import time
import turtle
from turtle import *
from datetime import datetime

def jump(distance):             # move to forward without draw
    penup()                     # pen up
    forward(distance)           # jump
    pendown()                   # pen down

def rectangle(width, height):   # draw rectangle
    fd(width/2)                 # forward(width/2)
    lt(90)                      # turn left 90degree
    fd(height)                  # forward(height)
    lt(90)                      # turn left 90degree
    fd(width)                   # forward(width)
    lt(90)                      # turn left 90degree
    fd(height)                  # forward(height)
    lt(90)                      # turn left
    fd(width/2)                 # forward(width/2)

def make_hand_shape(name, width, height):       # gen hand shape
    reset()
    left(90)
    jump(-height*0.15)
    right(90)
    begin_poly()
    rectangle(width, height*1.15)   # draw rectangle
    end_poly()
    clock_hand = get_poly()
    register_shape(name, clock_hand)

def clockface(radius):          # draw clock face
    reset()
    pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)              # draw line at a multiple of five
            jump(-radius-25)
        else:
            dot(3)              # draw dot at not a multiple of five
            jump(-radius)
        rt(6)                   # turn right 6 degree

def setup():
    global sec_hand, min_hand, hour_hand, writer
    mode("logo")
    make_hand_shape("sec_hand", 5, 150)         # second hand
    make_hand_shape("min_hand", 10, 130)        # min hand
    make_hand_shape("hour_hand", 15, 110)       # hour hand
    clockface(160)

    hour_hand = Turtle()
    hour_hand.shape("hour_hand")                # shape = hour_hand
    hour_hand.color("yellow", "yellow")
    min_hand = Turtle()
    min_hand.shape("min_hand")                  # shape = min_hand
    min_hand.color("blue1", "blue1")
    sec_hand = Turtle()
    sec_hand.shape("sec_hand")                  # shape = sec_hand
    sec_hand.color("red", "red")
    clock_hand_ax = Turtle()
    clock_hand_ax.shape(name="circle")          # shape = circle
    clock_hand_ax.color("black")
    for hand in sec_hand, min_hand, hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    ht()
    writer = Turtle()
    # writer.mode("logo")
    writer.ht()
    writer.pu()
    writer.bk(85)

def getWeekDayString(t):
    weekday_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday_name[t.weekday()]

def getDateString(date):        # get date
    month_name = ["NULL", "Jan.", "Feb.", "Mar.", "Apr.", "May", "June.", "July.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    yr = date.year
    mn = month_name[date.month]
    dy = date.day
    return "%s %d %d" % (mn, dy, yr)

def tick():
    t = datetime.today()
    sec = t.second + t.microsecond*0.000001
    minute = t.minute + sec/60.0
    hour = t.hour + minute/60.0
    try:
        tracer(False)                   # Terminator can occur here
        writer.clear()
        writer.home()
        writer.pencolor("darkred")
        writer.forward(65)
        writer.write(getWeekDayString(t), align="center", font=("Courier", 14, "bold")) # printout weekday string
        writer.back(150)
        writer.pencolor("brown")
        writer.write(getDateString(t), align="center", font=("Courier", 14, "bold"))    # printout date string
        writer.back(30)
        hhmmss = "(%2d : %2d : %2d)" % (hour, minute, sec)
        writer.pencolor("red")
        writer.write(hhmmss, align="center", font=("Tahoma", 14, "bold"))               # printout time string
        writer.forward(115)
        tracer(True)

        sec_hand.setheading(6 * sec + 90)       # setheading second
        min_hand.setheading(6 * minute + 90)    # setheading min
        hour_hand.setheading(30 * hour + 90)    # setheading hour
        writer.goto(0, 0)
        time.sleep(0.5)
        tracer(True)
        ontimer(tick, 100)
    except Terminator:
        pass

def main():
    tracer(False)
    setup()                                         # call setup function
    tracer(True)
    tick()                                          # call tick function
    return "Analog clock demo"

if __name__ == "__main__":
    turtle.setup(500, 500)                          # setup canvas
    turtle.title("My Analog Clock with Python")     # set title
    msg = main()
    mainloop()
