from queue import PriorityQueue

g=[]
h={'S':5,'A':3,'B':4,'C':2,'D':6,'G':0}
visited=set()

def create_graph():
    g.append(('S','A',1))
    g.append(('S','G',10))
    g.append(('A','C',1))
    g.append(('A','B',2))
    g.append(('B','D',5))
    g.append(('C','D',3))
    g.append(('C','G',4))
    g.append(('D','G',2))    

def AStar(src):
    global g,visited
    q=PriorityQueue()
    q.put((0,src))
    travel_cost=[]
    path_cost=0
    while q.qsize()>0:
        c1,source1=q.get()
        if source1!=src:
            for src1,cost1 in travel_cost:
                if src1==source1:
                    path_cost+=cost1
                    break
            travel_cost.clear()                 #next level adjacent nodes need to be stored
        while q.empty()==False:                 #next level f(n) values need to be stored
            dummy_cost,dummy_src=q.get()
        if source1 in visited:
            continue
        print(" => ",source1,end="")
        if source1=='G':
            print("\nCost = ",c1)
            break
        visited.add(source1)
        for src1,dest1,cost1 in g:
            if src1==source1:
                travel_cost.append((dest1,cost1))           #storing the dest node along with the cost of node without heuristic value
                q.put((path_cost+cost1+h[dest1],dest1))     #storing the f(n) value in queue()[includes heuristic value]

create_graph()
AStar('S')
