"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW04.1 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - 표준 입력장치로 부터 10개의 날짜를 입력 받아 정렬하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.09.27
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.09.27	v1.0	최초 작성
"""

Date_List = []      # 튜플을 저장할 리스트
for i in range(0, 10):
    (yr, mn, dy) = tuple(map(int, (input("input year, month, day : ")).split(sep=" ")))     # 년, 월, 일 분리하여 튜플 생성
    Date_List.append((yr, mn, dy))          # 리스트에 튜플 save
    print("Date_List = ", Date_List)


print("\nAfter input of 10 dates")
print("Date_List = ", Date_List, end="\n\n")

print("After sorting, Date_List")
Date_List.sort()                        # sorting
print("Date_List = ", Date_List)