#Importing Necessary Modules
import copy
import random

# Global Variables to Track Iterations, Backtracks, and States
iterations = 0
backtracks = 0

# Main Function 
def main():
    size = 4
    board = createBoard(size)
    print("Empty Board : \n")
    printBoard(board)
    print("Initial State:\n")
    generateStates(board)
    printBoard(board)
    #objective(board)
    hillclimb(board)


#Function to Create Inital Board
def createBoard(size):
    board = [["-" for _ in range(size)] for __ in range(size)]
    return board

#Function to Print Board
def printBoard(board):
    print()
    for row in board:
        print(row)
    print()

#Function To generate Inital Random State
def generateStates(board,row=0):
    if row == len(board):
        return    
    col = random.randint(0,len(board)-1)    #both limits inclusive
    if board[row][col] == 'Q':
        generateStates(board,row)
    board[row][col] = 'Q'
    generateStates(board,row+1)

#Function to Calculate the number of attacking pairs
def objective(board):
    attacking_pairs = 0
    queen_pos = []
    for row in range(len(board)):
        queen_pos.append((row,board[row].index('Q')))
    #print(queen_pos)
    for i in range(len(board)):
        for j in range(i+1,len(board)):
            #print(queen_pos[i],queen_pos[j])
            if(queen_pos[i][1] == queen_pos[j][1]):
                #print("Column: ",queen_pos[i],queen_pos[j])
                attacking_pairs +=1
            if( abs(queen_pos[i][0] - queen_pos[j][0]) == abs(queen_pos[i][1] - queen_pos[j][1])):
                attacking_pairs +=1
                #print("Diagonal : ",queen_pos[i],queen_pos[j])
    #print()
    #print(attacking_pairs)
    return attacking_pairs

#Function To Calculate Minimum State
def find_min(states):
    min_value = float('inf')
    min_state = None

    for child,value in states:
        if value < min_value:
            min_value = value
            min_state = child

    return min_state

#Hill Climb Function
def hillclimb(board,recursion_depth = 0):
    global iterations, backtracks

    #Terminate when maximum recursion depth is reached or solution is found
    if recursion_depth == 4 or (objective(board)==0):
        return
    
    iterations += 1

    #Find position of queens
    states = []
    queen_pos = []
    for row in range(len(board)):
        queen_pos.append(board[row].index('Q'))
    
    #Generate all possible states and calculate the Objective Function Value
    for row in range(len(board)):        
        for col in range(len(board)):
            if col != queen_pos[row]:                
                child = copy.deepcopy(board)                
                child[row] = ["-" for _ in range(len(board))] 
                child[row][col] = "Q"
                #printBoard(child)
                #print("No. of Attacking Pairs = ",objective(child))
                #print("\n")
                states.append((child,objective(child)))

    #Print Minimum State and continue
    print(f"Min State for Iteration {recursion_depth+1} :\n")
    min_state = find_min(states)
    print("No. of Attacking Pairs = ",objective(min_state))
    printBoard(min_state)   
    min_attacking_pairs = objective(min_state)
    
    if min_attacking_pairs >= objective(board):
        backtracks+= 1 

    print("Probability of Queen in Each State:")
    for state in states:
        count_queens = sum(row.count('Q') for row in state[0])
        probability = count_queens / (len(board) * len(board))
        printBoard(state[0])
        print(f"Probability: {probability:.2f}")

    print("Iterations = ",iterations)
    print("Bactracks = ",backtracks)
    hillclimb(min_state,recursion_depth+1)




main()