class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def make_tree(idx, n, arr):
    if idx >= n or arr[idx] == -1:
        return None
    root = TreeNode(arr[idx])
    root.left = make_tree(2 * idx + 1, n, arr)
    root.right = make_tree(2 * idx + 2, n, arr)
    return root


def count_palindromic_paths(root):
    count = 0

    def dfs(node, mask):
        nonlocal count
        if not node:
            return

        # toggle bit for current node value (1–9)
        mask ^= (1 << node.val)

        # check leaf
        if not node.left and not node.right:
            # at most one bit set
            if mask & (mask - 1) == 0:
                count += 1
            return

        dfs(node.left, mask)
        dfs(node.right, mask)

    dfs(root, 0)
    return count


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))

    root = make_tree(0, n, arr)
    print(count_palindromic_paths(root))


if __name__ == "__main__":
    main()
