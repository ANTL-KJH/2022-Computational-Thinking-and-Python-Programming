"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW02 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* -표준입력장치 (키보드)로부터 원의 반지름을 입력받고 그 원의 넓이와 원둘레를 출력하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.09.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.09.08	v1.0	최초 작성
"""
import math

PI = 3.141592
radius = float(input("radius : "))      # 반지름 값 입력
area = pow(radius, 2) * PI              # calculate area
circumference = 2 * radius * PI         # calculate circumference

print("Circle of radius (", radius, ") : area", area, ", circumference :", circumference)   # printout
