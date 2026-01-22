class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def build_linked_list(size, elements):
    if size == 0:
        return None
    head = Node(elements[0])
    tail = head
    for i in range(1, size):
        tail.next = Node(elements[i])
        tail = tail.next
    return head

def pair_sum(head):
    slow = head
    fast = head

    # find middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # compute max sum
    max_sum = -10**18
    first = head
    second = prev

    while second:
        max_sum = max(max_sum, first.val + second.val)
        first = first.next
        second = second.next

    return max_sum


# Correct input for this judge
n = int(input().strip())
elements = list(map(int, input().split()))
head = build_linked_list(n, elements)
print(pair_sum(head))
