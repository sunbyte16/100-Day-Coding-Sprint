class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def sum_of_values_in_range(root, start, end):
    if root is None:
        return 0

    # If value is less than start, ignore left subtree
    if root.val < start:
        return sum_of_values_in_range(root.right, start, end)

    # If value is greater than end, ignore right subtree
    if root.val > end:
        return sum_of_values_in_range(root.left, start, end)

    # Value lies in range
    return (
        root.val +
        sum_of_values_in_range(root.left, start, end) +
        sum_of_values_in_range(root.right, start, end)
    )

def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    values = list(map(int, data[1:n+1]))
    start = int(data[n+1])
    end = int(data[n+2])

    root = None
    for val in values:
        root = insert_into_bst(root, val)

    print(sum_of_values_in_range(root, start, end))

if __name__ == "__main__":
    main()
