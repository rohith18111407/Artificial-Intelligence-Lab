n=int(input('no of numbers: '))
arr=input('Enter Color Red or Green: ')
arr=arr.lower()
if arr=='red':
    arr=[(2*x)+1  for x in range(n)]
    print(arr)
if arr=='green':
    arr=[2*(x+1)  for x in range(n)]
    print(arr)
    
cost = 0
def dfs_search(arr, target,root_index=0):
    global cost
    cost+=1
    if root_index < len(arr):    	    	        
        print(arr[root_index])        
        if arr[root_index] == target:
            print("Cost = ",cost)
            print("found:", target)
            return True

        
        left = dfs_search(arr, target, 2 * root_index + 1)
        cost-=1      
        right = dfs_search(arr, target, 2 * root_index + 2)
        

       
        return left or right

   
    return False


target_element = 5

if not dfs_search(arr,target_element):
    print("Element not found:", target_element)
