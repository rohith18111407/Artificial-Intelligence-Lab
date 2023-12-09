n=int(input('Enter no of numbers: '))
arr=input('red or green: ')
arr=arr.lower()
if arr=='red':
    arr=[(2*x)+1  for x in range(n)]
    print(arr)
if arr=='green':
    arr=[2*(x+1)  for x in range(n)]
    print(arr)

cost = 0
def dls_search(arr, target, search_level, root=0, current_level=0):
    global cost
    cost+=1
    if root < len(arr) and current_level <= search_level:    	        
        print(arr[root])
        if arr[root] == target:
            print("Cost = ",cost)
            print("Element found at level", current_level, ":", target)
            return True

        
        current_level += 1

        
        left = dls_search(arr, target, search_level, 2 * root+ 1, current_level)
        cost-=1
	
       
        right = dls_search(arr, target, search_level, 2 * root + 2, current_level)

        
        return left or right
    
    return False


target_element = int(input("Enter target"))
search_level = int(input("Enter Search Level"))

if not dls_search(arr, target_element, search_level):
    print("Element not found up to level", search_level)



