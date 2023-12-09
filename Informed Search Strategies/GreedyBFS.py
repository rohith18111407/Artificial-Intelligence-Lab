from queue import PriorityQueue

g=[]
visited=set()

def create_graph():
    g.append(('A','B',9))
    g.append(('A','C',6))
    g.append(('B','D',5))
    g.append(('C','D',8))
    g.append(('C','F',5))
    g.append(('D','E',7))
    g.append(('D','G',6))
    g.append(('F','G',7))
    g.append(('E','H',4))
    g.append(('G','H',8))
    

def greedyBFS(src):
    global g,visited
    q=PriorityQueue()
    q.put((0,src))
    while q.qsize()>0:
        c1,source1=q.get()
        while q.empty()==False:         # q stores only the particular level node and cost, so clear it at each level
            dummy_cost,dummy_src=q.get()
        if source1 in visited:
            continue
        print(" => ",source1,end="")
        if source1=='H':
            print("\nCost = ",c1)
            break
        visited.add(source1)
        for src1,dest1,cost1 in g:
            if src1==source1:
                q.put((c1+cost1,dest1))

create_graph()
greedyBFS('A')
