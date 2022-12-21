"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW06.3 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - 사용자에게 랜덤 리스트의 size를 입력받고 사용자 정의 패키지를 이용하여
* - 난수 생성, 샘플 출력, mergesorting을 수행하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.10.07
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.10.07	v1.0	최초 작성
"""

import random, time, sys
sys.path.append("C:/MyPyPackage/myModules")
import MyMatrix
def main():
    A = [[1,2,3,4], [5,6,7,8], [9,10,0,1]]              # matrix init
    B = [[1,0,0,0], [0,1,0,0], [0,0,1,1]]
    C = [[1,0,0], [0,1,0], [0,0,1], [0,0,0]]

    MyMatrix.printMtrx("A", A)                          # printout Mrtx A, B, C
    MyMatrix.printMtrx("B", B)
    MyMatrix.printMtrx("C", C)

    D = MyMatrix.addMtrx(A, B)                          # add Mtrx
    MyMatrix.printMtrx("A + B", D)

    E = MyMatrix.subMtrx(A, B)                          # sub Mtrx
    MyMatrix.printMtrx("A ‐ B", E)

    F = MyMatrix.mulMtrx(A, C)                          # mul Mtrx
    MyMatrix.printMtrx("A * C", F)

if __name__ == "__main__":
    main()