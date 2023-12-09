def main():

	tree = {(0,0):((-1,-1),"Intial State")}

	state_list = [(0,0)]
	for state in state_list:	
		threeG,fourG = state	
		if threeG > 0:
			new_state = (0,fourG)
			if new_state not in state_list:
				tree[new_state] = (state,"Empty 3 Gallon Container")
				#print("Child = ", new_state)
				state_list.append(new_state)
			
		if threeG < 3:
			new_state = (3,fourG)
			if new_state not in state_list:
				tree[new_state] = (state,"Fill 3 Gallon Container")
				#print("Child = ", new_state)
				state_list.append(new_state)
			
		if fourG > 0:
			new_state = (threeG,0)
			if new_state not in state_list:
				tree[new_state] = (state,"Empty 4 Gallon Container")
				#print("Child = ", new_state)
				state_list.append(new_state)
			
		if fourG < 4:
			new_state = (threeG,4)
			if new_state not in state_list:
				tree[new_state] = (state,"Fill 4 Gallon Container")
				#print("Child = ", new_state)
				state_list.append(new_state)
		
		#4----> 3 Gallon		
		if threeG < 3 and fourG > 0:
			fillable = 3 - threeG
			if fillable > fourG :				
				new_state = (threeG+fourG, 0)
				
			else:
				new_state = (3 , fourG - fillable)
			if new_state not in state_list:
				tree[new_state] = (state,"Transfer Contents of 4 Gallon to 3 Gallon")
				#print("Child = ", new_state)
				state_list.append(new_state)
		
		#3 ---> 4 Gallon
		if threeG > 0 and fourG < 4:
			fillable = 4- fourG
			if fillable > threeG:
				new_state = (0,threeG+fourG)
			else:
				new_state = (threeG - fillable,4)
			if new_state not in state_list:
				tree[new_state] = (state,"Transfer Contents of 3 Gallon to 4 Gallon")
				#print("Child = ", new_state)
				state_list.append(new_state)

		if new_state[1] == 2:
			#print(tree)
			printPath(tree,(new_state,"Goal State"))
		#print(state)
			
		
		
					
	
def printPath(tree,init_state):
	pathcost=0
	while(init_state[0] != (-1,-1)):
		print(init_state[1],init_state[0],sep="\n")
		init_state = tree[init_state[0]]
		pathcost+=1
	
	print()
	print("Cost is:",pathcost)
			

main()
