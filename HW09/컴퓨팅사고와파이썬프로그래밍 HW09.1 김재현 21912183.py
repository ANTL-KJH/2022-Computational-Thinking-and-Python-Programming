"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW09.1 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - 파일로부터 도형에 대한 정보를 입력받고 그리는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.11.04
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.11.04	    v1.0	최초 작성
"""

import turtle
import math
#from Turtle_Drawing import *


def fget_drawings(fin):                 # get shape data from dat file
    L_drawings = []
    while True:
        draw_data = []
        line = fin.readline()           # read line
        if not line:
            break
        draw_data = line.split()        # split line
        #draw_data.append(split_line)
        L_drawings.append(draw_data)    # append data
    for i in range(len(L_drawings)):
        for p in range(2, 5):
            L_drawings[i][p] = int(L_drawings[i][p])
    #print(L_drawings)
    return L_drawings

def drawCircle(t, center_pos, radius, color):   # draw circle
    t.up()
    cx, cy = center_pos                 # center_pos에서 cx, cy 분배
    t.goto(cx, cy-radius)               # start pos
    t.down()
    t.width(1)
    t.circle(radius)                    # draw Circle
    t.up()
    return

def drawStar(t, center_pos, radius, color):         # draw star
    t.pencolor(color)
    t.width(3)
    t.goto(center_pos)
    cx, cy = center_pos
    startx = cx -radius / 2
    theta = math.radians(360 / 5)
    starty = cy + radius / (2.0 * math.tan(theta))
    t.up()
    t.goto(-radius // 2, radius // 6)               # starting position
    t.pendown()  # pen down to draw
    for i in range(5):                              # draw
        t.forward(radius)
        t.right((360 * 2) / 5)
    t.penup()
    return

def drawPolygon(t, center_pos, num_vert, radius, color):    # draw polygon
    #center_pos = (center_x, center_y)  # center_pos tuple
    center_x, center_y = center_pos
    line_width = 3                                          # line width = 3
    t.up();
    t.goto(center_pos);                                     # move to center pos
    t.dot(10, "blue");
    t.write(center_pos)                                     # dot at the center pos and write pos
    t.width(line_width)                                     # set pen
    t.pencolor(color)

    line_length = radius * math.sin(math.radians((360 / num_vert) / 2)) * 2  # radius로부터 line_length 연산
    start_x = center_x - line_length / 2  # set start_x, start_y
    theta = math.radians((180 - 360 / num_vert) / 2)
    h = line_length * math.tan(theta) / 2
    start_y = center_y - h

    t.penup()
    t.goto(center_x - 50, start_y - 50);
    t.write("({} {})".format(color, getPolygonName(num_vert)))  # polygon name 출력

    t.penup();
    t.goto(start_x, start_y);
    t.pendown()
    t.dot(10, "red");
    t.write("({:.1f}, {:.1f})".format(start_x, start_y))

    for i in range(num_vert):  # draw
        t.forward(line_length)
        t.left(360 / num_vert)
    t.up();
    t.home();
    t.down()  # goto center
    return

def getNumVertex(shape):    # 도형의 이름을 통해 다각형의 각을 찾는 함수
    polygons = {"triangle": 3, "square": 4, "pentagon": 5, "hexagon": 6, "heptagon": 7, "octagon": 8, "nonagon": 9,
                "decagon": 10}
    num_vertices = polygons[shape]
    return num_vertices  # return vertex

def getPolygonName(num_vert):   # 각을 통해 다각형의 이름을 찾는 함수
    polygons = ["triangle","square", "pentagon", "hexagon", "heptagon", "octagon", "nonagon", "decagon"]
    poly_name = polygons[num_vert-3]
    return poly_name

def main():
    turtle.setup(900, 500)                  # 900, 500 size canvas 생성
    turtle.title("Drawing polygons with user-defined Turtle_Drawing.py")        # Title setting
    t = turtle.Turtle()                     # turtle object
    t.shape("classic")

    fin = open("drawings.txt")      # file open
    L_drawings = fget_drawings(fin)
    fin.close()
    for drawing in L_drawings:
        (color, shape, cx, cy, radius) = drawing        # x, y, shape, radius, color
        center_pos = (cx, cy)                           # center position
        print("drawing a {} {} of circumscribed circle's radius {} at center_pos({}, {}).".format(color, shape, radius, cx, cy))
        t.up(); t.goto(center_pos); t.down()            # move
        t.dot(10, "red"); t.write(center_pos)           # dot at the center_pos
        t.width(5)
        if (shape == "circle"):                         # circle
            drawCircle(t, center_pos, radius, color)
        elif (shape == "star"):                         # star
            drawStar(t, center_pos, radius, color)
        else:
            num_vert = getNumVertex(shape)              # polygon
            if num_vert != None:
                drawPolygon(t, center_pos, num_vert, radius, color)
                drawCircle(t, center_pos, radius, color)
            else:
                print("Drawing shape {} is not implemented yet !!".format(shape))
    turtle.exitonclick()        # 실행 결과 확인을 위한 exitonclick()

if __name__ == "__main__":
    main()
