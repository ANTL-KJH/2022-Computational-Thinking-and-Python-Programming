"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW10.1 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - numpy 모듈을 이용하여 행렬의 연산 및 증명하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.11.11
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.11.11	    v1.0	최초 작성
"""

import numpy as np

def main():
    # Matrix A, B define
    LinearArray_A = np.array([[1, 5, 3, 3, 7], [3, 4, 5, 6, 7], [1, 3, 5, 7, 9], [3, 1, 4, 1, 5], [5, 5, 3, 3, 1]], dtype=np.int32)
    LinearArray_B = np.array([105, 135, 145, 74, 75], dtype=np.int32)

    print("A = \n{}".format(LinearArray_A))                 # print out Matrix A
    print("B = \n{}".format(LinearArray_B))                 # print out Matrix B

    det_A = np.linalg.det(LinearArray_A)                    # Matrix A determinant
    print("det_A = \n",det_A)

    inv_A = np.linalg.inv(LinearArray_A)                    # Inverse Matrix A
    print("inv_A =\n", inv_A)

    Result = np.linalg.solve(LinearArray_A, LinearArray_B)  # Solve Matrix
    print("X =\n", Result)

    B1 = np.matmul(LinearArray_A, Result)                   # Proof Calculate
    print("B1 = A * X = \n", B1)

    X1 = np.matmul(inv_A, LinearArray_B)                    # Proof Calculate
    print("X1 = inv_A * B = \n", X1)

if __name__ == "__main__":
    main()
