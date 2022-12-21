"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW07.3 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - Class를 이용하여 Time를 처리하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.10.14
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2022.10.14  v1.0	최초 작성
"""
class Time:
    def __init__(self, hr, mn, sec):        # init
        self.setHour(hr)
        self.setMinute(mn)
        self.setSecond(sec)

    def __lt__(self, other):                # operation overloading <
        if self.Hour < other.Hour:
            return True
        elif self.Hour == other.Hour:
            if self.Minute < other.Minute:
                return True
            elif self.Minute == other.Minute:
                if self.Second < other.Second:
                    return True
        return False

    def __str__(self):                      # print 호출시 전달되는 string
        return str("({:2}:{:2}:{:2})".format(self.Hour, self.Minute, self.Second))

    def getHour(self):                      # return Hour
        return self.Hour

    def getMinute(self):                    # return Minute
        return self.Minute

    def getSecond(self):                    # return Second
        return self.Second

    def setHour(self, hr):                  # set Hour
        if hr < 0 or hr > 23:
            print("Illegal Data :: Hour({:2})".format(hr))
            exit(1)
        self.Hour = hr

    def setMinute(self, mn):                # set Minute
        if mn < 0 or mn > 59:
            print("Illegal Data :: Minute({:2})".format(mn))
            exit(1)
        self.Minute = mn

    def setSecond(self, sec):               # set Second
        if sec < 0 or sec>59:
            print("Illegal Data :: Second({:2})".format(sec))
            exit(1)
        self.Second = sec

def main():
    times = [
        Time(23, 59, 59),
        Time(9, 0, 5),
        Time(13, 30, 0),
        Time(3, 59, 59),
        Time(0, 0, 0),
    ]
    print("times before sorting : ")
    for t in times:
        print(t)
    #
    times.sort()
    print("\ntimes after sorting : ")
    for t in times:
        print(t)

if __name__ == "__main__":
    main()