"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW10.2 김재현 21912183
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
    LinearArray_A = np.loadtxt("Matrix_data.txt")                   # load Matrix data from txt file
    print("A = \n", LinearArray_A)

    det_A = np.linalg.det(LinearArray_A)                            # determinant A
    print("A_det = ", det_A)

    inv_A = np.linalg.inv(LinearArray_A)                            # inverse Matrix of A
    print("A_inv =", inv_A)

    LinearArray_E = np.matmul(LinearArray_A, inv_A)                 # A * inv_A = I
    print("E= np.matmul (A, A_inv)", LinearArray_E)

if __name__=="__main__":
    main()
