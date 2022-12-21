"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW07.1 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - Class Person과 상속관계에 있는 Class Student를 다루는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.10.13
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.10.13	    v1.0	최초 작성
"""

class Person:
    def __init__(self, name=None, age=None):                # init Person object
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):              # init 실행전 object memory allocation
        cls.__inst = super(Person, cls).__new__(cls)
        return cls.__inst

    def __str__(self):                                  # return printout str
        return "Person(name={}, age={})".format(self.name, self.age)

    def __del__(self):                                  # destructor
        return

    def __dict__(self):                                 # dict
        print("Person::__dict__() is executed.")
        return self.name, self.age


class Student(Person):                                  # class student, Person을 상속 받음
    def __init__(self, name, birth, age, st_id, major, gpa):        # init Student
        Person.__init__(self, name, age)                            # init Person
        self.birth = birth
        self.setMajor(major)
        self.setSTID(st_id)
        self.setGPA(gpa)


    def __str__(self):                      # return printout str
        return "Student(name={}, birth={}, age={}, st_id={}, major={}, GPA={})".format(self.name, self.birth, self.age, self.st_id, self.major, self.GPA)

    def __del__(self):                      # destructor
        return

    def getMajor(self):                     # Major accessor
        return self.major

    def getSTID(self):                      # STID accessor
        return self.st_id

    def getGPA(self):                       # GPA accessor
        return self.GPA

    def setMajor(self, major):              # Major mutator
        set_majors = {"EE", "ICE", "ME", "CE"}
        if major in set_majors:
            self.major = major
        else:
            print("*** Error in setting major (name:{}, age:{})".format(self.name, major))
            self.major = None  # default value

    def setSTID(self, st_id):               # STID mutator
        self.st_id = st_id

    def setGPA(self, gpa):                  # GPA mutator
        self.GPA = gpa


def compareStudent(st1, st2, key):
    if key == "st_id" and st1.st_id < st2.st_id:
        return True
    elif key == "name" and st1.name < st2.name:
        return True
    elif key == "GPA" and st1.GPA > st2.GPA:
        return True
    else:
        return False
# 나머지 부분은 직접 구현할 것


def sortStudent(L_st, key):
    for i in range(0, len(L_st)):
        min_idx = i
        for j in range(i+1, len(L_st)):
            if compareStudent(L_st[j], L_st[min_idx], key):
                min_idx = j
        if min_idx != i:
            L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]


def printStudents(L_st):
    for s in range(len(L_st)):
        print(L_st[s])


def main():
    students = [
        Student("Kim", 990101, 21, 12345, "EE", 4.0),
        Student("Lee", 980715, 22, 11234, "ME", 4.2),
        Student("Park", 101225, 20, 10234, "ICE", 4.3),
        Student("Hong", 110315, 19, 13123, "CE", 4.1),
        Student("Yoon", 971005, 23, 11321, "ICE", 4.2),
        Student("Wrong", 100000, 23, 15321, "??", 3.2)]
    print("students before sorting : ")
    printStudents(students)

    sortStudent(students, "name")
    print("\nstudents after sorting by name : ")
    printStudents(students)

    sortStudent(students, "st_id")
    print("\nstudents after sorting by student_id : ")
    printStudents(students)

    sortStudent(students, "GPA")
    print("\nstudents after sorting by GPA in decreasing order : ")
    printStudents(students)


if __name__ == "__main__":
    main()
