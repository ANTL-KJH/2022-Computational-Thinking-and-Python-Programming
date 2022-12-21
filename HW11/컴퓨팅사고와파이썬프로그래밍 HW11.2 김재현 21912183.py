"""
* 프로젝트명 : 컴퓨팅사고와파이썬프로그래밍 HW11.2 김재현 21912183
* 프로그램의 목적 및 기본 기능 :
* - Hashmap을 구성하여 학생정보를 다루는 프로그램
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2022.11.17
* ==========================================================================
* 프로그램 수정 / 보완 이력
* ==========================================================================
* 프로그램 수정자		일자			    버전		수정내용
* JH KIM			2022.11.17	    v1.0	최초 작성
* JH KIM            2022.11.21      v1.1    DiGraph관련 수정
"""

from MyGraph import *

def initGraph(G, ICD_fileName):             # init WeightedGraph
    input_str = " "
    node_names = []                         # list
    wedges = []
    while True:
        input_str = ICD_fileName.readline()
        if input_str == '':
            break
        start, end, weight = input_str.split(sep=" ")
        if start not in node_names:
            node_names.append(start)
        if end not in node_names:
            node_names.append(end)
        wedges.append(WeightedEdge(start, end, int(weight)))
        wedges.append(WeightedEdge(end, start, int(weight)))
    for i in range(len(node_names)):        # addNode
        G.addNode(Node(node_names[i]))
    for i in range(len(wedges)):            # addEdge
        # print("\ninitGraph() :: adding weighted_edge {} into Graph".format(we))
        G.addEdge(wedges[i])

    print("initGraph() - adding nodes into Graph : ", end="")
    for i in range(len(G.node_names)):
        print("{}, ".format(G.node_names[i]), end="")
    print()

    return G

EdgesPerLine = 5


def main():
    fin = open("InterCityDist_input.txt", 'r')          # file open
    G = WeightedGraph()                                 # WeightedGraph Class instance
    initGraph(G, fin)                                   # init
    node_names = G.getNode_NMs()
    print("Nodes : ", node_names)                       # print out node names
    edges = G.getWEdges()
    print("Edges :")
    eCount = 0
    for e in edges:                                     # printout edge
        print(" {}".format(e), end=', ')
        eCount += 1
        if eCount % EdgesPerLine == 0:
            print()
    print()
    G.printConnectivity()                               # printout table
    start_nm = "GJ"                                     # GJ -> SC
    end_nm = "SC"
    print("Trying ShortestPath_Dijkstra : ({} -> {})".format(start_nm, end_nm))
    path_Dijkstra, path_cost = Dijkstra(G, start_nm, end_nm)        # Dijkstra calc GJ -> SC
    print("Found shortestPath_Dijkstra ({} -> {}): {}, total_path_cost ={}".format(start_nm, end_nm, path_Dijkstra, path_cost))
    start_nm = "SC"     # G.nodes[7].getName()
    end_nm = "GJ"       # G.nodes[2].getName()
    print("Trying ShortestPath_Dijkstra : ({} -> {})".format(start_nm, end_nm))
    path_Dijkstra, path_cost = Dijkstra(G, start_nm, end_nm)        # Dijkstra calc SC -> GJ
    print("Found shortestPath_Dijkstra ({} -> {}): {}, total_path_cost ={}"\
    .format(start_nm, end_nm, path_Dijkstra, path_cost))

if __name__ == "__main__":
    main()