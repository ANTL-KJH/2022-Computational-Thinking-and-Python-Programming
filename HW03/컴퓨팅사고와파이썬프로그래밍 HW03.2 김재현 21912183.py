"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW03.2 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* -사용자로부터 년, 월, 일을 입력받고 서기 1년 1월 1일부터 몇번째 날짜인지,
* -무슨 요일인지 계산하여 출력하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.09.16
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.09.16	v1.0	최초 작성
"""

weekday_name = [None, "MON", "TUE", "WED", "THR", "FRI", "SAT", "SUN"]      # 요일 이름 init
month_day = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]          # 각 달의 날짜 설정
while True:
    elapsed_day = 0
    input_str = input("input year month day : ")            # input year, month, day
    yr_mn_dy = input_str.split(sep=" ")                     # split
    year, month, day = map(int, yr_mn_dy)                   # mapping
    print("Input yr_mn_dy_strings : ", yr_mn_dy)            # print string
    if year == 0 and month == 0 and day == 0:               # exit point
        exit()
    for i in range(1, year):                                # 1~year-1년 날짜 덧셈
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:   # leapyear check
            elapsed_day += 366
        else:
            elapsed_day += 365                              # 1~month-1월 날짜 덧셈
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:      # leapyear check
        month_day[2] = 29
    else:
        month_day[2] = 28
    for i in range(1, month):
        elapsed_day += month_day[i]
    elapsed_day += day
    weekday = elapsed_day % 7               # find weekday
    print("Day (year({}), month({}), day({})) : week_day({}), elapsed {} days from Jan01AD01".\
          format(year, month, day, weekday_name[weekday],elapsed_day))      # printout
