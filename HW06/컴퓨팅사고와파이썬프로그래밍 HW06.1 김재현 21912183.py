"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW06.1 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - 사용자 정의 패키지를 이용하여 난수 생성, 샘플 출력, selection sorting을 수행하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.10.07
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.10.07	v1.0	최초 작성
"""

import sys
myPyModules_dir = "C:/MyPyPackage/myModules"        # module 경로
sys.path.append(myPyModules_dir)                    # system 경로
import MyList
import MySortings

def main():
    L = []
    n = 100

    MyList.genRandList(L, n)                            # genRandList
    print("Before Sorting :")
    MyList.printListSample(L, 10, 3)                    # print samples
    MySortings.selectionSort(L)                         # sorting
    print("\nAfter Sorting :")
    MyList.printListSample(L, 10, 3)                    # print samples

if __name__ == "__main__":
    main()