"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW08.1 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - 파일로부터 사용자의 데이터를 입력받고 데이터를 분석하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.10.30
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.10.30	    v1.0	최초 작성
* JH KIM            2022.11.01      v1.1    리스트 수정
"""


def main():
    input_file = open("student_records.txt", 'r')
    output_file = open("output.txt", 'w')
    Student_Data = []

    for line in input_file.readlines():                 # Data input
        temp_list = []
        name, kor, eng, math, sci = line.split()
        temp_list.append(name)
        temp_list.append(int(kor))
        temp_list.append(int(eng))
        temp_list.append(int(math))
        temp_list.append((int(sci)))
        Student_Data.append(temp_list)
    input_file.close()

    for i in range(len(Student_Data)):                  # Printout
        print(Student_Data[i])
    print()

    for i in range(len(Student_Data)):                  # clac sum, avg and append
        sum = 0
        avg = 0
        sum = Student_Data[i][1] + Student_Data[i][2] + Student_Data[i][3] + Student_Data[i][4]     # calc sum
        avg = sum / 4                                   # clac avg
        Student_Data[i].append(sum)                     # append
        Student_Data[i].append(avg)

    print("After calculate_scores(students)")           # printout Template
    for i in range(40):
        print("=", end="")
    print()
    print("name : kor  eng  math  sci  sum  avg")
    output_file.write("name : kor  eng  math  sci  sum  avg\n")
    for i in range(40):
        print("-", end="")
        output_file.write("-")
    print()
    output_file.write("\n")

    for i in range(len(Student_Data)):                  # Printout Data
        print("{:4} : {:3}, {:3}, {:3}, {:3}, {:3}, {:.2f}".format(Student_Data[i][0], Student_Data[i][1], Student_Data[i][2], Student_Data[i][3], Student_Data[i][4], Student_Data[i][5], Student_Data[i][6]))
        output_file.write("{:4} : {:3}, {:3}, {:3}, {:3}, {:3}, {:.2f}\n".format(Student_Data[i][0], Student_Data[i][1], Student_Data[i][2], Student_Data[i][3], Student_Data[i][4], Student_Data[i][5], Student_Data[i][6]))

    for i in range(40):
        print("=", end="")
    print()

if __name__ == "__main__":
    main()