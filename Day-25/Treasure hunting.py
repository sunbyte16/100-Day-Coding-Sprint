from functools import lru_cache

def user_logic(n, a, b):
    @lru_cache(None)
    def dfs(i, mask):
        # i -> current index in array a
        # mask -> bitmask representing which elements in b are used
        if i == n:
            return 0  # all elements paired
        
        res = float('inf')
        for j in range(n):
            if not (mask & (1 << j)):  # if b[j] is not used
                res = min(res, (a[i] ^ b[j]) + dfs(i + 1, mask | (1 << j)))
        return res

    return dfs(0, 0)

# Driver code
def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().strip().split()))
    
    n = data[0]
    a = data[1:n+1]
    b = data[n+1:2*n+1]
    
    result = user_logic(n, a, b)
    print(result)

if __name__ == "__main__":
    main()
