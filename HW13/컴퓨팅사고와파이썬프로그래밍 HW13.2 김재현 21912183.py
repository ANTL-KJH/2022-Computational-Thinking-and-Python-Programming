"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW13.2 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - handwritten digits recognition testing program
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.11.25
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.11.25	    v1.0	최초 작성
"""


import os
import PIL
import cv2
import glob
import numpy as np
from tkinter import *
from PIL import Image, ImageDraw, ImageGrab
# load model
from keras.models import load_model


def draw_lines(event):                  #  draw line
    global lastx, lasty
    x, y = event.x, event.y
    # create line
    cv.create_line((lastx, lasty, x, y), width=8, fill='black', capstyle=ROUND, smooth=TRUE, splinesteps=12)
    lastx, lasty = x, y

def clear_widget():                     # clear Widget
    global cv
    cv.delete("all")

def activate_event(event):              # draw line with mouse left click
    global lastx, lasty
    cv.bind('<B1-Motion>', draw_lines)  # B1-Motion => drag with left clicking
    lastx, lasty = event.x, event.y

def recognize_digit():
    global image_number
    predictions = []
    percentage = []
    filename = f'image_{image_number}.png'                  # set file name
    widget = cv

    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()

    ImageGrab.grab().crop((x, y, x1, y1)).save(filename)    # save written digits image
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)        # gen rectangle
        top = int(0.05 * th.shape[0])
        bottom = top
        left = int(0.05 * th.shape[1])
        right = left
        th_up = cv2.copyMakeBorder(th, top, bottom, left, right, cv2.BORDER_REPLICATE)

        roi = th[y - top:y + h + bottom, x - left:x + w + right]
        img = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)       # image resize
        img = img.reshape(1, 28, 28, 1)                                     # image reshape
        img = img / 255.0
        pred = model.predict([img])[0]
        final_pred = np.argmax(pred)
        data = str(final_pred) + ' ' + str(int(max(pred) * 100)) + '%'
        font = cv2.FONT_HERSHEY_SIMPLEX                                     # set font
        fontScale = 0.5
        color = (255, 0, 0)                                                 # set color
        thickness = 1
        cv2.putText(image, data, (x, y - 5), font, fontScale, color, thickness) # print text
    cv2.imshow("image", image)      # image show
    cv2.waitKey(0)

def main():
    cv.bind('<Button-1>', activate_event)           # start when click left button
    btn_save = Button(text="Recognize Digits", command=recognize_digit) # call recognize_digit function
    btn_save.grid(row=2, column=0, padx=1, pady=1)                      # grid recognize button
    btn_clear = Button(text="Clear widget", command=clear_widget)       # call clear widget
    btn_clear.grid(row=2, column=1, padx=1, pady=1)                     # grid clear widget
    # mainloop()
    root.mainloop()

if __name__ == "__main__":
    model = load_model("CNN_model_Digits")          # load model
    model.summary()
    print("Model is loaded successfully ...")
    root = Tk()                                     # Tkinter
    root.resizable(0, 0)
    root.title("Handwritten Digits Recognition GUI App")    # set title
    lastx, lasty = None, None
    image_number = 0
    cv = Canvas(root, width=640, height=480, bg='white')    # set canvas
    cv.grid(row=0, column=0, pady=2, sticky=W, columnspan=2)
    main()