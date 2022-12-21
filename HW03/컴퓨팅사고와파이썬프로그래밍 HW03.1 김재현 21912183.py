"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW03.1 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* -2개의 16진수 데이터 문자열을 한줄로 입력받고, 두 개의 정수로 변환하여 bit-wise 연산하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.09.13
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.09.13	v1.0	최초 작성
"""

input_str = input("input two hexadecimal numbers (예: 0xA3 0x3A) : ")       # 두개의 16진수를 하나의 문자열로 입력
num_str = input_str.split(sep=" ")
num_str[0] = int(num_str[0], 16)        # 16진수 문자를 10진수 정수로 변환
num_str[1] = int(num_str[1], 16)
a, b = map(int, num_str)                # mapping
anb = a & b             # and 연산
aob = a | b             # or 연산
aeb = a ^ b             # exclusive or 연산
print("a =", hex(num_str[0]), "=", bin(num_str[0]))         # printout
print("b =", hex(num_str[1]), "=", bin(num_str[1]))
print("a & b = {0:#04x} = {0:#010b}".format(anb, anb))
print("a | b = {0:#04x} = {0:#010b}".format(aob, aob))
print("a ^ b = {0:#04x} = {0:#010b}".format(aeb, aeb))