n=int(input('no of numbers: '))
arr=input('Enter Color Red/Green')
arr=arr.lower()
if arr=='red':
    arr=[(2*x)+1  for x in range(n)]    #odd numbers
    print(arr)
if arr=='green':
    arr=[2*(x+1)  for x in range(n)]    #even numbers
    print(arr)


def bfs_search(arr,target):
    index = 0
    found = False
    print(arr[0])
    cost = 0
    while index < len(arr):     
        
        left_child = (index*2)+1
        right_child = (index*2)+2
        if left_child < len(arr):
            cost+=1            
            print(arr[left_child])
            if arr[left_child] == target:            	
                print("Found")
                print("Cost to reach= ",cost)
                found = True
                return
        if right_child < len(arr):
            cost+=1
            print(arr[right_child])
            if arr[right_child] == target:
                print("Found!")
                print("Cost = ",cost)
                found = True
                return
        
        index+=1
    if found == False:    	
        print("Not Found!!")

target = int(input("Enter target"))
bfs_search(arr,target)
