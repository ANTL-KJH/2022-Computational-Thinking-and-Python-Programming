"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW05.2 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - 터틀 그래픽 가능을 사용하여 지정된 위치에 다각형을 그리는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.10.05
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.10.05	v1.0	최초 작성
"""

import turtle, math
import turtle as myTurtle
PI = 3.141592
ROUND = 360

def drawPolygon(t, center_x, center_y, line_length, num_vertices):
    t.up()                  # pen up
    t.write(t.pos())        # write pos
    j = (180 - (ROUND / num_vertices)) / 2
    # 내각의 절반을 구함
    radian = PI / 180 * j                               # radian
    height = (line_length / 2) * math.tan(radian)       # calc height
    distance = math.sqrt(pow((line_length / 2), 2) + pow(height, 2))    # 중심에서 꼭짓점까지의 거리
    if (num_vertices == 4):                             # 사각형은 상단 꼭짓점이 없으므로 예외
        a = line_length / 2
        t.goto(center_x - a, center_y + a)
        t.lt(90 + (ROUND / num_vertices) / 2)
    else:
        t.goto(center_x, center_y + distance)           # 상단 꼭짓점 이동
        t.lt(90)                                        # 북쪽 정렬
    t.lt(180 - j)                                       # 각도에 맞게 turn
    t.down()                                            # pendown

    for i in range(0, num_vertices):
        t.forward(line_length)          # draw
        t.write(t.position())           # write pos
        t.dot(5, "red")                 # draw dot
        t.lt(ROUND / num_vertices)      #turn
    t.up()
    t.goto(center_x, center_y)


def main():
    t = turtle.Turtle()             # Turtle
    t.shape("turtle")               # shape = turtle
    # input x, y, ver, len
    center_x, center_y, num_vertices, line_length = map(int, input("input center_x, center_y, num_vertices, and line_length : ").split(' '))
    center_pos = (center_x, center_y)
    line_width = 3
    t.up(); t.goto(center_pos); t.down()        # goto center_pos
    t.dot(10, "red");
    #t.write(center_pos)
    t.width(line_width)
    t.pencolor("blue")                          # pen color = blue
    t.color("blue")                             # color = blue
    drawPolygon(t, center_x, center_y, line_length, num_vertices)       # draw
    myTurtle.exitonclick()          # 클릭하면 종료

if __name__ == "__main__":
    main()

