class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def countNodes(head):
    if head is None or head.next is None or head.next.next is None:
        return 0

    count = 0
    prev = head
    curr = head.next

    while curr.next is not None:
        next_node = curr.next

        if curr.data > prev.data and curr.data > next_node.data:
            count += 1

        prev = curr
        curr = next_node

    return count

def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    elements = list(map(int, data[1:]))

    head = None
    tail = None

    for elem in elements:
        new_node = Node(elem)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    result = countNodes(head)
    print(result)   # ✅ ONLY this should print

if __name__ == "__main__":
    main()
