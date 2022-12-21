"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW08.2 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - 클래스를 이용하여 파일로부터 Mtrx 데이터를 입력받고 연산하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.10.30
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.11.01	    v1.0	최초 작성
"""


class Mtrx:
    def __init__(self, name, n_row, n_col, lst_data):           # class init
        self.n_row = n_row                  # row init
        self.n_col = n_col                  # col init
        lst_row = []
        self.rows = []
        self.name = name                    # name
        index = 0
        for i in range(0, self.n_row):                          # list data를 row, col에 맞춰 입력
            for p in range(0, self.n_col):
                lst_row.append(lst_data[index])
                index = index + 1
            self.rows.append(lst_row)
            lst_row = []

    def set_name(self, name):               # setname
        self.name = name

    def __str__(self):
        s = "{} = \n".format(self.name)         # printout name
        for i in range(0, self.n_row):          # printout data
            for p in range(0, self.n_col):
                s += "{:6.2f}".format(self.rows[i][p])
            s += "\n"
        return s

    def __add__(self, other):                   # operator overloading +, 덧셈 연산
        add_result = []                            # 연산 결과를 담을 list
        for i in range(0, self.n_row):
            for p in range(0, self.n_col):
                add_data= self.rows[i][p] + other.rows[i][p]
                add_result.append(add_data)
        return Mtrx("R", self.n_row, self.n_col, add_result)

    def __sub__(self, other):                   # operator overloading +, 뺄셈 연산
        sub_list = []
        for i in range(0, self.n_row):
            for p in range(0, self.n_col):
                sub_data = self.rows[i][p] - other.rows[i][p]
                sub_list.append(sub_data)
        return Mtrx("R", self.n_row, self.n_col, sub_list)

    def __mul__(self, other):                   # operator overloading *, 곱셈 연산
        mul_list = []
        for i in range(0, self.n_row):
            for j in range(0, other.n_col):
                mul_data = 0
                for k in range(0, self.n_col):
                    mul_data = mul_data + self.rows[i][k] * other.rows[k][j]
                mul_list.append(mul_data)            # 곱셈 연산 종료 후 list에 append
        return Mtrx("R", self.n_row, other.n_col, mul_list)


def fget_MtrxData(fin):                                 # get Mtrx data from file
    Mtrx_row_col = fin.readline()                       # readline
    row, col = map(int, Mtrx_row_col.split())           # mapping row, col
    Mtrx_Lst = []
    for i in range(0, row):                             # readline and mapping data
        num = fin.readline()
        Mtrx_Lst += list(map(float, num.split()))
    return Mtrx_Lst, row, col

def main():
    print("Executing main()")
    input_file = open("matrix_data.dat", 'r')
    La, a_row, a_col = fget_MtrxData(input_file)        # get mtrx data from file
    print("fgetMtrx for mA")
    mA = Mtrx("mA", a_row, a_col, La)
    print(mA)

    Lb, a_row, a_col = fget_MtrxData(input_file)        # get mtrx data from file
    mB = Mtrx("mB", a_row, a_col, Lb)
    print("fgetMtrx for mB")
    print(mB)

    Lc, a_row, a_col = fget_MtrxData(input_file)        # get mtrx data from file
    mC = Mtrx("mC", a_row, a_col, Lc)
    print("fgetMtrx for mC")
    print(mC)

    mD = mA + mB                        # mD = mA + mB
    mD.set_name("mD = mA + mB")
    print(mD)

    mE = mA - mB                        # mE = mA - mB
    mE.set_name("mE = mA - mB")
    print(mE)

    mF = mA * mC                        # mF = mA * mB
    mF.set_name("mF = mA * mC")
    print(mF)


if __name__ == "__main__":
    main()

