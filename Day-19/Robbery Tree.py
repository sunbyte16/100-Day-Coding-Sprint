class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insertLevelOrder(arr, i):
    if i >= len(arr) or arr[i] == "null":
        return None
    root = TreeNode(int(arr[i]))
    root.left = insertLevelOrder(arr, 2 * i + 1)
    root.right = insertLevelOrder(arr, 2 * i + 2)
    return root

def user_logic(root):
    def dfs(node):
        if not node:
            return (0, 0)  # (rob_this, not_rob_this)
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        rob_this = node.val + left[1] + right[1]
        not_rob_this = max(left) + max(right)
        
        return (rob_this, not_rob_this)
    
    return max(dfs(root))

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    root = insertLevelOrder(data, 0)
    
    result = user_logic(root)
    print(result)

if __name__ == "__main__":
    main()
