n=int(input('Enter no of numbers: '))
arr=input('red or yellow: ')
arr=arr.lower()
if arr=='red':
    arr=[(2*x)+1  for x in range(n)]
    print(arr)
if arr=='green':
    arr=[2*(x+1)  for x in range(n)]
    print(arr)

cost = 0
def dls_search(arr, target, search_level, root_index=0, current_level=0):
    global cost
    cost+=1
    if root_index < len(arr) and current_level <= search_level:
        print(arr[root_index])
        if arr[root_index] == target:
            print("Cost = ",cost)
            print("Element found at level", current_level, ":", target)
            return True

        
        current_level += 1

        
        left = dls_search(arr, target, search_level, 2 * root_index + 1, current_level)
        cost-=1

       
        right = dls_search(arr, target, search_level, 2 * root_index + 2, current_level)

        
        return left or right

    
    return False


target_element = 13
search_level = 2  

def main():
    n = int(input("Enter Max Search Level : "))
    for search_level in range(1,n+1):
        if not dls_search(arr, target_element, search_level):
            print("Element not found up to level", search_level)

main()





