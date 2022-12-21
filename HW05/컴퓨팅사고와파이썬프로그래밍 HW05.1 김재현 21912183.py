"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW05.1 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - 큰 사이즈의 정수형 난수를 만들고 mergesort 하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.10.05
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.10.05	v1.0	최초 작성
"""

import random, time


def genBigRandList(n):
    l = []
    """while(len(l)<n):                         # 10만개이상 생성시 매우 오래걸림
        rand_num = random.randint(0, n)         # random number 생성
        if rand_num not in l:                   # 중복이 아닌 경우 append
            l.append(rand_num)"""

    for i in range(0,n):                        # list 생성
        l.append(i)
    for i in range(0,n):                        # shuffle을 이용한 random 생성
        r1 = random.randint(0, n-1)
        r2 = random.randint(0, n-1)
        if r1 == r2:                            # 두 랜덤 값이 같으면 continue
            continue
        temp = l[r1]                            # swap
        l[r1] = l[r2]
        l[r2] = temp
    return l

def printListSample(L, per_line=10, sample_lines=2):        # random list의 앞, 뒤 sample을 출력하는 함수
    for i in range(0, per_line * sample_lines):             # 앞 20개 sample printout
        print("{0:7}".format(L[i]), end="")
        if(i>0 and (i+1) % 10 == 0):
            print()

    print("     . . . . . .")

    for i in range((len(L) - (per_line*sample_lines)), (len(L))):       # 뒤 20개 sample printout
        print("{0:7}".format(L[i]), end="")
        if (i > 0 and (i+1) % 10 == 0):
            print()

def _merge(L_left, L_right):                    # mergesort
    L_res = []
    i, j = 0, 0
    len_left, len_right = len(L_left), len(L_right)
    while i < len_left and j < len_right:
        if L_left[i] < L_right[j]:
            L_res.append(L_left[i])
            i += 1
        else:
            L_res.append(L_right[j])
            j += 1
    while (i < len_left):
        L_res.append(L_left[i])
        i += 1
    while (j < len_right):
        L_res.append(L_right[j])
        j += 1
    return L_res

def mergeSort(L):                               # mergesort
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
    L_left = mergeSort(L[:middle])
    L_right = mergeSort(L[middle:])
    return _merge(L_left, L_right)




def main():
    while True:
        print("\nPerformance test of merge sorting algorithm")
        size = int(input("Input size of random list L (0 to quit) = "))     # size input
        if size == 0:
            break
        L = genBigRandList(size)                        # genBigRand
        # testing MergeSorting

        print("\nBefore mergeSort of L :")
        printListSample(L, 10, 2)                       # printout sample

        t1 = time.time()                                # time check
        sorted_L = mergeSort(L)                         # sort
        t2 = time.time()

        print("After mergeSort of L :")
        printListSample(sorted_L, 10, 2)
        time_elapsed = t2 - t1
        print("Merge sorting took {} sec".format(time_elapsed))

if __name__ == "__main__":
    main()