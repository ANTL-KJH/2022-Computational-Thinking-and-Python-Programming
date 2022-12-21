"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW02 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* -표준입력장치 (키보드)로부터 직사각형의 가로와 세로를 입력받아 넓이와 둘레를 계산하여 출력하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.09.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.09.08	v1.0	최초 작성
"""

input_str = input("width, length = ")       # 가로 세로를 문자열 형태로 입력 받음
num_str = input_str.split(sep=' ')          # 띄어쓰기를 기준으로 split
width, length = map(float, num_str)         # float 형태로 width, length에 입력
area = width * length                       # area 계산
perimeter = 2 * width + 2 * length          # perimeter 계산
print("Rectangle of width(", width, ") and length (", length, ") : area (", area, "), perimeter (", perimeter, ")")
