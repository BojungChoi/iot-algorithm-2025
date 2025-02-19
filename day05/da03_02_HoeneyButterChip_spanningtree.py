# 허니버터칩이 가장 많이 남은 편의점 찾기!

# 클래스 선언
class Graph:
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def printGraph(g):
    print('',end='\t')
    for v in range(g.SIZE):
        print("%20s" % storeAry[v][0], end=' ')
    print()
#  print(f'{g.graph[row][col]:>4d}', end='\t')
    for row in range(g.SIZE):
        print("%11s" % storeAry[row][0], end=' ') 
        for col in range(g.SIZE):
            print(f'{g.graph[row][col]:>10d}', end='\t\t')
        print()
    print()

# 전역변수 선언 부분
# SIZE = (5)
G = None
storeAry = [['GS25', 30],['CU', 60],['Seven11', 10],['어둠의유통업자', 90],['Emart24', 40]]
GS25, CU, Seven11,어둠의유통업자, Emart24 = 0, 1, 2, 3, 4
# SIZE = len(storeAry)


## 메인 코드 부분

gSize = 5
G = Graph(gSize)
G.graph[GS25][CU] = 1;G.graph[GS25][Seven11] = 1
G.graph[CU][GS25] = 1;G.graph[CU][Seven11] = 1;G.graph[CU][어둠의유통업자] = 1
G.graph[Seven11][GS25] = 1;G.graph[Seven11][CU] = 1;G.graph[Seven11][어둠의유통업자] = 1
G.graph[어둠의유통업자][Seven11] = 1;G.graph[어둠의유통업자][CU] = 1;G.graph[어둠의유통업자][Emart24] = 1
G.graph[Emart24][어둠의유통업자] = 1

print('## 편의점 그래프 ##')
printGraph(G)

stack = []
visitedAry = [] # 방문한 편의점

current = 0
maxStore = current
maxCount = storeAry[current][1]
stack.append(current)
visitedAry.append(current)

while (len(stack) != 0) :
    next = None
    for vertex in range(gSize):
        if G.graph[current][vertex] == 1:
            if vertex in visitedAry: # 방문한 적이 있는 편의점이면 탈락!
                pass
            else : # 방문한 적이 없는 편의점이면 다음 편의점으로 지정!
                next = vertex
                break

    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)