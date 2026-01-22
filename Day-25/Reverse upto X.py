class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def push(self, data):
        if self.head is None:
            temp = Node(data)
            self.head = temp
            self.tail = temp
        else:
            temp = Node(data)
            self.tail.next = temp
            self.tail = temp

def reverseLinkedListUpToX(ll, x):
    prev = None
    current = ll.head
    next_node = None
    found = False
    
    # Reverse until we reach x or the end of the list
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        if current.data == x:
            found = True
            break
        current = next_node
    
    # If x was found, connect the reversed part to the remaining list
    if found:
        ll.head.next = next_node  # Original head becomes tail of reversed part
        ll.head = prev  # Update head to the new head after reversal
    else:
        # x not found, entire list reversed
        ll.head = prev

if __name__ == '__main__':
    ll = LinkedList()
    n = int(input())
    elements = list(map(int, input().split()))
    for t in elements:
        ll.push(t)
    x = int(input())
    reverseLinkedListUpToX(ll, x)
    ll.print()
