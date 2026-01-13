class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def check(l1, l2):
    """
    Check if two linked lists share any common node.
    """
    nodes_set = set()
    
    # Traverse first list and store node references
    current = l1
    while current:
        nodes_set.add(current)
        current = current.next
    
    # Traverse second list and check for intersection
    current = l2
    while current:
        if current in nodes_set:
            return 1
        current = current.next
    
    return 0

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    m = int(data[1])
    
    node_map = {}
    
    # Build first linked list
    l1 = Node(0)
    temp = l1
    index = 2
    for i in range(n):
        val = int(data[index])
        index += 1
        if val in node_map:
            node = node_map[val]
        else:
            node = Node(val)
            node_map[val] = node
        temp.next = node
        temp = temp.next
    l1 = l1.next
    
    # Build second linked list
    l2 = Node(0)
    temp = l2
    for i in range(m):
        val = int(data[index])
        index += 1
        if val in node_map:
            node = node_map[val]
        else:
            node = Node(val)
            node_map[val] = node
        temp.next = node
        temp = temp.next
    l2 = l2.next
    
    # Check intersection
    result = check(l1, l2)
    print(result)

if __name__ == "__main__":
    main()
