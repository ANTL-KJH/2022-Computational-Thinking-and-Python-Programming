"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW07.2 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - Class Date를 이용하여 날짜 데이터를 처리하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.10.13
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.10.13	v1.0	최초 작성
"""

class Date:
    def __init__(self, yr, mn, dy):         # Class Date init
        self.setYear(yr)
        self.setMonth(mn)
        self.setDay(dy)

    def __lt__(self, other):                # operation overloading <
        if self.Year < other.Year:
            return True
        elif self.Year == other.Year:
            if self.Month < other.Month:
                return True
            elif self.Month == other.Month:
                if self.Day < other.Day:
                    return True
        return False

    def __str__(self):                      # printout str
        s = "({:4}-{:2}-{:2})".format(self.Year, self.Month, self.Day)
        return s

    def getYear(self):                      # Year accessor
        return self.Year

    def getMonth(self):                     # Month accessor
        return self.Month

    def getDay(self):                       # Day accessor
        return self.Day

    def setYear(self, yr):                  # Year mutator
        if yr < 0:
            print("Illegal Data :: Year({})".format(yr))
            exit(1)
        self.Year = yr

    def setMonth(self, mn):                 # Month mutator
        if mn < 0 or mn > 12:
            print("Illegal Data :: Month({})".format(mn))
            exit(1)
        self.Month = mn

    def setDay(self, dy):                   # Day mutator
        month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.isLeapYear(self.Year)
        self.Day = dy

    def isLeapYear(self, yr):               # Check LeapYear
        if ((yr % 4 == 0) and (yr % 100 != 0) or (yr % 400 == 0)):
            return True
        return False

def main():
    # class objec gen
    dates = [
        Date(2000, 9, 15),
        Date(1997, 2, 20),
        Date(2001, 5, 2),
        Date(2001, 5, 1),
        Date(1999, 3, 1)
    ]

    print("dates before sorting : ")
    for d in dates:
        print(d)

    dates.sort()
    print("\nstudents after sorting : ")
    for d in dates:
        print(d)

if __name__ == "__main__":
    main()
