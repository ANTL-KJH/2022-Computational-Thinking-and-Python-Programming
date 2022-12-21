"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW06.2 김재현 21912183
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
import MyList, MySortings

while True:
    size = int(input("\nsize of list (0 to terminate) = "))                     # input size
    L = []
    MyList.genRandList(L, size)                                                 # genRandList
    print("List (size : {}) before merge sorting : ".format(size))
    MyList.printListSample(L, 10, 2)                                            # printout samples
    t1 = time.time()                                                            # time check
    MySortings.mergeSort(L)                                                     # merge sorting
    t2 = time.time()                                                            # time check
    print("\nList (size : {}) after merge sorting : ".format(size))
    MyList.printListSample(L, 10, 2)                                            # printout samples
    print("Merge sorting for list of {} integers took {} sec".format(size, t2 - t1))
    MyList.shuffleList(L)                                                       # shuffle
    print("\nList (size : {}) before selection sorting : ".format(size))
    MyList.printListSample(L, 10, 2)                                            # printout samples
    t1 = time.time()                                                            # time check
    MySortings.selectionSort(L)                                                 # selection sorting
    t2 = time.time()                                                            # time check
    print("\nList (size : {}) after selection sorting : ".format(size))
    MyList.printListSample(L, 10, 2)                                            # printout samples
    print("Selection sorting for list of {} integers took {} sec".format(size, t2 - t1))

