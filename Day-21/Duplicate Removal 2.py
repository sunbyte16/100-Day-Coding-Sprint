class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicates(head):
    # Dummy node to handle edge cases easily
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy  # prev is the last node before the current sequence
    current = head

    while current:
        # If current node has duplicates
        if current.next and current.val == current.next.val:
            # Skip all nodes with the same value
            val_to_remove = current.val
            while current and current.val == val_to_remove:
                current = current.next
            prev.next = current  # Link prev to the first non-duplicate node
        else:
            prev = current
            current = current.next

    return dummy.next

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    if n == 0:
        print("null")
        return
    
    values = list(map(int, data[1:n+1]))

    # Create the linked list
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    head = dummy.next

    # Remove duplicates
    new_head = removeDuplicates(head)

    # Print the linked list or "null" if empty
    if not new_head:
        print("null")
    else:
        res = []
        current = new_head
        while current:
            res.append(str(current.val))
            current = current.next
        print(" ".join(res))

if __name__ == "__main__":
    main()
