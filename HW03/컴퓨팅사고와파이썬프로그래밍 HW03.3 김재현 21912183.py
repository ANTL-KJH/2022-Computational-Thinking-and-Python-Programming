"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW03.3 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* -사용자로부터 년, 월, 일을 입력받고 해당 월의 달력을 출력하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.09.16
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.09.16	v1.0	최초 작성
"""

month_Name = [None, "January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekday_Name = ["SUN", "MON", "TUE", "WED", "THR", "FRI", "SAT"]
month_day = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]          # 각 달의 날짜 설정
input_str = input("input year month day : ")
yr_mn_dy = input_str.split(sep=" ")                     # split
year, month, day = map(int, yr_mn_dy)
elapsed_day = 0
for i in range(1, year):  # 1~year-1년 날짜 덧셈
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:  # leapyear check
        elapsed_day += 366
    else:
        elapsed_day += 365  # 1~month-1월 날짜 덧셈
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:  # leapyear check
    month_day[2] = 29
else:
    month_day[2] = 28
for i in range(1, month):
    elapsed_day += month_day[i]
weekday = elapsed_day % 7               # 해당 월의 시작 요일 계산

print()
print("{} of Year {}".format(month_Name[month], year))  # 년, 월 출력
for i in range(0, 28):                                  # 구분선 출력
    print("=", end="")
print()
for i in range(0, 7):
    print("{0:>4}".format(weekday_Name[i]), end="")     # 4칸, 오른쪽 정렬
print()
for i in range(0, 28):                                  # 구분선 출력
    print("-", end="")
print()
count = 0
for i in range(0, weekday + 1):                         # 시작 일 앞의 빈칸 채우기
    if weekday == 6:
        break
    print("    ", end="")
    count += 1


for i in range(1, month_day[month] + 1):
    print("{0:>4}".format(i), end="")
    count += 1
    if count == 7:
        print()
        count = 0

print()
for i in range(0, 28):                                  # 구분선 출력
    print("=", end="")
print()