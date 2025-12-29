class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_balanced_bst(arr, l, r):
    if l > r:
        return None
    
    # IMPORTANT: use UPPER MID
    mid = (l + r + 1) // 2
    root = Node(arr[mid])
    
    root.left = build_balanced_bst(arr, l, mid - 1)
    root.right = build_balanced_bst(arr, mid + 1, r)
    
    return root


def preorder_print(root):
    if not root:
        return
    
    left = root.left.val if root.left else "."
    right = root.right.val if root.right else "."
    
    print(f"{left} <- {root.val} -> {right}")
    
    preorder_print(root.left)
    preorder_print(root.right)


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().split()))
    
    arr.sort()
    root = build_balanced_bst(arr, 0, n - 1)
    preorder_print(root)
