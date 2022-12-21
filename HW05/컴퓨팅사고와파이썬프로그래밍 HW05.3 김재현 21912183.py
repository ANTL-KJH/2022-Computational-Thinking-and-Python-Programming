"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW05.3 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - 동적프로그래밍을 통해 Fibonacci 수열을 신속하게 계산하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.10.05
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.10.05	v1.0	최초 작성
"""

import time             # time module
memo = dict()           # global dict

def dynFibonacci(n):
    if n in memo:               # n 번째 연산결과가 dict에 있는 경우
        return memo[n]
    elif n == 0 or n == 1 :     # 0, 1번째 연산은 하지 않음
        memo[n] = n
        return n
    else:                       # calc Fibo
        fibo = dynFibonacci(n-1) + dynFibonacci(n-2)        # calc
        memo[n] = fibo          # save result at the dict
        return fibo




def main():
    # 시작(start), 종료(end), 간격(stride) 입력
    start, end, stride = map(int, input("input start, stop, step of Fibonacci serise : ").split())
    for i in range(start, end + 1, stride):         # 종료지점은 end + 1
        t_before = time.time()                      # time check
        fibo_i = dynFibonacci(i)                    # Fibo calc
        t_after = time.time()                       # time check
        t_diff = (t_after - t_before) * 1000000             # micro-sec
        print("dynFibo({:3}) = {:25}, took {:10.2f}[micro_sec]".format(i, fibo_i, t_diff))  # printout


if __name__ == "__main__":
    main()
