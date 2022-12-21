"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW05.4 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - 행렬을 연산하고 출력하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.10.05
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.10.05	v1.0	최초 작성
"""

def printMtrx(name, M):
    row = len(M)            # row size
    col = len(M[1])         # col size
    print(name,"=")
    for i in range(0, row):
        for p in range(0, col):
            print("{:4}".format((M[i][p])), end="")     # print out
        print()

def addMtrx(M1, M2):
    Mtrx = []
    result = 0
    row = len(M1)           # row size
    col = len(M1[1])        # col size
    for i in range(0, row):
        temp_row = []
        for p in range(0, col):
            result = M1[i][p] + M2[i][p]
            temp_row.append(result)
        Mtrx.append(temp_row)
    return Mtrx

def subMtrx(M1, M2):
    Mtrx = []
    result = 0
    row = len(M1)           # row size
    col = len(M1[1])        # col size
    for i in range(0, row):
        temp_row = []
        for p in range(0, col):
            result = M1[i][p] - M2[i][p]
            temp_row.append(result)
        Mtrx.append(temp_row)
    return Mtrx

def mulMtrx(M1, M2):
    Mtrx = []
    col = len(M2[1])    # col size
    row = len(M1)       # row size
    Common_size = len(M1[1])

    for i in range(0, row):
        temp_row = []                # 행 임시저장
        for j in range(0, col):
            result = 0  # 요소들 결과를 여기서 초기화
            for k in range(0, Common_size):
                result += M1[i][k] * M2[k][j]  # 요소의 곱을 더해주면서 F의 요소를 완성
            temp_row.append(result)  # 행에 집어넣는다.
        Mtrx.append(temp_row)  # 그리고 그 행을 행렬F에 집어넣으면서 반복
    return Mtrx  # 반환

def main():
    A = [[1,2,3,4], [5,6,7,8], [9,10,0,1]]
    B = [[1,0,0,0], [0,1,0,0], [0,0,1,1]]
    C = [[1,0,0], [0,1,0], [0,0,1], [0,0,0]]

    printMtrx("A", A)       # print out
    printMtrx("B", B)
    printMtrx("C", C)
    D = addMtrx(A, B)       # add
    printMtrx("A + B", D)
    E = subMtrx(A, B)       # sub
    printMtrx("A - B", E)
    F = mulMtrx(A, C)       # mul
    printMtrx("A * C", F)

if __name__ == "__main__":
    main()