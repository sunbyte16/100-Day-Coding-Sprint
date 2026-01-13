class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    # Dummy node to handle head swaps easily
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        # Nodes to be swapped
        first = prev.next
        second = prev.next.next

        # Swapping nodes
        prev.next = second
        first.next = second.next
        second.next = first

        # Move prev to next pair
        prev = first

    return dummy.next


def stringToListNode(input):
    input = input[1:-1].strip()
    if not input:
        return None
    node_values = list(map(int, input.split(',')))
    dummy_root = ListNode(0)
    ptr = dummy_root
    for val in node_values:
        ptr.next = ListNode(val)
        ptr = ptr.next
    return dummy_root.next

def listNodeToString(node):
    if not node:
        return '[]'
    return '[' + ', '.join(map(str, iter_list(node))) + ']'

def iter_list(node):
    while node:
        yield node.val
        node = node.next

if __name__ == '__main__':
    import sys
    input = sys.stdin.read().strip()
    head = stringToListNode(input)
    swapped_head = swapPairs(head)
    print(listNodeToString(swapped_head))
