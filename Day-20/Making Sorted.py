def user_logic(bst1_nodes, bst2_nodes):
    # Combine both lists
    combined = bst1_nodes + bst2_nodes
    # Sort the combined list
    combined.sort()
    return combined

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # Number of nodes in the first BST
    bst1_nodes = list(map(int, data[1:N+1]))  # Node values of bst1
    
    M = int(data[N+1])  # Number of nodes in the second BST
    bst2_nodes = list(map(int, data[N+2:N+2+M]))  # Node values of bst2
    
    # Call user logic function and get the result
    result = user_logic(bst1_nodes, bst2_nodes)
    
    # Print the output as space-separated integers
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
