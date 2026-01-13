class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(head, k):
    if not head:
        return None

    first = head
    # Move first pointer to the Kth node from start
    for _ in range(k - 1):
        first = first.next

    kth_from_start = first

    # Use two pointers to find the Kth node from end
    slow = head
    fast = first
    while fast.next:
        fast = fast.next
        slow = slow.next

    kth_from_end = slow

    # Swap values
    kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val

    return head

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Number of nodes
    values = list(map(int, data[1:n+1]))  # Node values
    k = int(data[n+1])  # Kth position

    # Build linked list
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    head = dummy.next

    # Swap nodes
    modified_head = swapNodes(head, k)

    # Print result
    result = []
    current = modified_head
    while current:
        result.append(current.val)
        current = current.next
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
