"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW11.1 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - Hashmap을 구성하여 학생정보를 처리하는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.11.17
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.11.17	    v1.0	최초 작성
* JH KIM			2022.11.18	    v1.1	Hash map 수정
"""
import myHashMap

def main():
    #print(ord('0'))  # 48
    HashMap_Capacity = 7                                            # Capacity
    print("Creating a HashMap of capacity ({})".format(HashMap_Capacity))
    hsMap = myHashMap.HashMap(capacity=HashMap_Capacity)        # Hashmap init
    Entries = [("Kim", 19345, "ICE", 4.0), ("Park", 18234, "CS", 4.2), ("Hong", 20456, "EE", 3.9), \
                ("Lee", 20987, "ME", 3.8), ("Yoon", 21654, "ICE", 3.7), ("Moon", 21001, "CHEM", 4.1), \
                ("Hwang", 21123, "CE", 3.7), ("Choi", 19003, "EE", 4.3), ("Yeo", 20234, "ME", 3.8), \
                ("Jeong", 18005, "PH", 4.3)]
    for i in range(len(Entries)):
        entry = Entries[i]
        key = entry[0]                                              # key => name
        hsMap._setitem(key, entry)                                  # set item
        print("Entry[{:2}] : {}".format(i, Entries[i]))

    print("Current HashMap Internal Structure:\n", hsMap)           # Printout HashMap
    print("Checking entry searching in HashMap")

    while True:
        key = input("Input student name to search (. to quit) : ")  # input student name
        if key == '.':
            break
        v = hsMap._getitem(key)                                     # get item
        if v == None:
            print("key ({}) is not found in hashmap !!".format(key))
        else:
            print("key ({}) : Value ({})".format(key, v))

if __name__ == "__main__":
    main()
