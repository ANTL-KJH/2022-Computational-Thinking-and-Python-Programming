"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW01 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* -직사각형의 가로, 세로와 중심 좌표를 입력받고 사각형을 그리는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.08.31
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.08.31	v1.0	최초 작성
* JH KIM			2022.09.01	v1.1	함수 작성
"""
import turtle
import time

t=turtle.Turtle()
width = float(input("Input width : "))
height = float(input("Input height : "))
cx = float(input("Input cx : "))
cy = float(input("Input cy : "))
if(cx<0):
    start_x = cx + (width / 2)
else:
    start_x = cx - (width / 2)
if(cy<0):
    start_y = cy + (height / 2)
else:
    start_y = cy - (height / 2)
t.up()
t.goto(start_x, start_y)
t.down()
t.goto(start_x + width, start_y)
t.goto(start_x + width, start_y + height)
t.goto(start_x, start_y + height)
t.goto(start_x, start_y)
time.sleep(5)