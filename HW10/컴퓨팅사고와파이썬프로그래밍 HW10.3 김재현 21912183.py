"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW10.3 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - numpy 모듈과 matplotlib을 이용하여 Gauss 분포를 그래프로 출력하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.11.11
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.11.11	    v1.0	최초 작성
"""

import numpy as np
import matplotlib.pyplot as plt

def gauss(mu, sigma, X):
    y = 1.0/(sigma * np.sqrt(2*np.pi)) * np.exp(-((X - mu) ** 2)/(2 * sigma ** 2))
    return y

def main():
    x = np.linspace(-8, 8, num=101)                 # chart 범위는 -8 ~ 8, 0을 제외하고 100 개의 구간

    mu, sigma = 0, 2  # mean = 0, standard_deviation = 2
    y1 = gauss(mu, sigma, x)                        # 평균 = 0, 표준편차 2
    plt.plot(x, y1, color="red", label="sigma=2")
    mu, sigma = 0, 1                                # mean = 0, standard_deviation = 2
    y2 = gauss(mu, sigma, x)                        # 평균 = 0, 표준편차 1
    plt.plot(x, y2, color="blue", label="sigma=1")
    mu, sigma = 0, 0.5                              # mean = 0, standard_deviation = 2
    y3 = gauss(mu, sigma, x)                        # 평균 = 0, 표준편차 0.5
    plt.plot(x, y3, color="green", label="sigma=0.5")

    plt.title("Normal Distribution Graph1 - mu = 0.0, sigma = [0.5, 1, 2]")
    plt.legend(loc="best")
    plt.grid(True)
    plt.savefig("Gauss_Distribution_mu=0.png")
    plt.show()


    x = np.linspace(-8, 8, num=101)                     # chart 범위는 -8 ~ 8, 0을 제외하고 100 개의 구간

    mu, sigma = -2, 1  # mean = -2, standard_deviation = 1
    y1 = gauss(mu, sigma, x)                            # 평균 = 0, 표준편차 2
    plt.plot(x, y1, color="red", label="mu=-2.0")
    mu, sigma = 0, 1                                    # mean = 0, standard_deviation = 1
    y2 = gauss(mu, sigma, x)                            # 평균 = 0, 표준편차 1
    plt.plot(x, y2, color="blue", label="mu=0.0")
    mu, sigma = 2, 1                                    # mean = 0, standard_deviation = 2
    y3 = gauss(mu, sigma, x)                            # 평균 = 2, 표준편차 1
    plt.plot(x, y3, color="green", label="mu=2.0")

    plt.title("Normal Distribution Graph1 - mu = [-1.0, 0.0, 1.0], sigma = 1")
    plt.legend(loc="best")
    plt.grid(True)
    plt.savefig("Gauss_Distribution_sigma=1.png")
    plt.show()

if __name__ =="__main__":
    main()
