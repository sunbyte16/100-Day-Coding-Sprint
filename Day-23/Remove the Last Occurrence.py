class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_last_occurrences(head):
    from collections import Counter

    freq = Counter()
    curr = head
    while curr:
        freq[curr.val] += 1
        curr = curr.next

    dummy = ListNode(0)
    tail = dummy
    curr = head

    while curr:
        if freq[curr.val] > 1:
            tail.next = ListNode(curr.val)
            tail = tail.next
        freq[curr.val] -= 1
        curr = curr.next

    return dummy.next

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next

# Correct input for this judge
n = int(input())
values = list(map(int, input().split()))

if n == 0:
    print("")
else:
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    new_head = remove_last_occurrences(head)
    print_linked_list(new_head)
