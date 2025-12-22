import sys
sys.setrecursionlimit(10**7)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def user_logic(root):
    max_diameter = 0

    def dfs(node):
        nonlocal max_diameter
        if not node:
            return 0

        left_height = dfs(node.left)
        right_height = dfs(node.right)

        # Diameter measured in number of edges
        max_diameter = max(max_diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    dfs(root)
    return max_diameter


def construct_tree(i, nodes):
    if i < 0 or i >= len(nodes):
        return None

    node = TreeNode(i + 1)

    l, r = nodes[i]
    if l != -1:
        node.left = construct_tree(l - 1, nodes)
    if r != -1:
        node.right = construct_tree(r - 1, nodes)

    return node


def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])

    nodes = []
    idx = 1
    for _ in range(n):
        l = int(data[idx])
        r = int(data[idx + 1])
        idx += 2
        nodes.append((l, r))

    root = construct_tree(0, nodes)
    print(user_logic(root))


if __name__ == "__main__":
    main()
