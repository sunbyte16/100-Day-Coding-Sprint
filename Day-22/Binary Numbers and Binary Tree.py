class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def make_tree(idx, arr, n):
    if idx >= n:
        return None
    root = TreeNode(arr[idx])
    root.left = make_tree(2 * idx + 1, arr, n)
    root.right = make_tree(2 * idx + 2, arr, n)
    return root


def dfs(node, current):
    if not node:
        return 0

    current = (current << 1) | node.val

    if not node.left and not node.right:
        return current

    return dfs(node.left, current) + dfs(node.right, current)


def user_logic(root):
    return dfs(root, 0)


def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    root = make_tree(0, arr, n)
    print(user_logic(root))


if __name__ == "__main__":
    main()
