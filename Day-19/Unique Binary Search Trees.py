def numTrees(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    
    total = 0
    for i in range(1, n + 1):
        left = numTrees(i - 1, memo)
        right = numTrees(n - i, memo)
        total += left * right
    
    memo[n] = total
    return total

if __name__ == '__main__':
    number_of_nodes = int(input())
    print(numTrees(number_of_nodes))
