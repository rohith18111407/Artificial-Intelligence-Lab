import math

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def generate_state_space_tree(level):
    if level < 0:
        return None

    root = TreeNode(1)
    queue = [root]

    for i in range(level):
        next_level_nodes = []
        for node in queue:
            left_value = 2 * node.value + 1
            right_value = 2 * node.value + 2

            node.left = TreeNode(left_value)
            node.right = TreeNode(right_value)

            next_level_nodes.append(node.left)
            next_level_nodes.append(node.right)
        
        queue = next_level_nodes

    return root

def terminal_test(node):
    return node.left is None and node.right is None

def utility(node):
    return node.value

def minimax_decision(node, strategy):
    path = []

    if strategy == "max":
        best_value = max_value(node, path)
    elif strategy == "min":
        best_value = min_value(node, path)

    return best_value, path

def max_value(node, path):
    if terminal_test(node):
        return utility(node)

    v = -math.inf
    best_child = None

    if node.left:
        left_child_value = min_value(node.left, path)
        if left_child_value > v:
            v = left_child_value
            best_child = node.left

    if node.right:
        right_child_value = min_value(node.right, path)
        if right_child_value > v:
            v = right_child_value
            best_child = node.right

    if best_child:
        path.append(best_child)
    
    return v

def min_value(node, path):
    if terminal_test(node):
        return utility(node)

    v = math.inf
    best_child = None

    if node.left:
        left_child_value = max_value(node.left, path)
        if left_child_value < v:
            v = left_child_value
            best_child = node.left

    if node.right:
        right_child_value = max_value(node.right, path)
        if right_child_value < v:
            v = right_child_value
            best_child = node.right

    if best_child:
        path.append(best_child)

    return v

def print_tree(node, indent="", last=True):
    if node is not None:
        print(indent, end="")
        if last:
            print("└── ", end="")
            indent += "    "
        else:
            print("├── ", end="")
            indent += "│   "

        print(node.value)

        if node.left or node.right:
            print_tree(node.left, indent, False)
            print_tree(node.right, indent, True)

def print_path(path):
    print("The path followed in the decision-making process:")
    for node in path:
        print(node.value, end=" -> ")
    print("End")

if __name__ == "__main__":
    print("Welcome to the Minimax Algorithm Example")
    
    level = int(input("Enter the depth of the state space tree (0 or greater): "))

    state_space_tree_root = generate_state_space_tree(level)
    print("State Space Tree for depth", level, ":")
    print_tree(state_space_tree_root)

    print()
    
    strategy = input("Enter 'max' for Maximizing or 'min' for Minimizing: ")
    
    best_value, best_path = minimax_decision(state_space_tree_root, strategy)
    
    print("The best value for the", strategy, "player is:", best_value)
    print_path(best_path)
