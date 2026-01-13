def min_parachutes(k, n):
    if n == 0 or k == 0:
        return 0
    # dp[m][k] = max floors we can check with m moves and k parachutes
    dp = [0] * (k + 1)
    moves = 0
    while dp[k] < n:
        moves += 1
        for j in range(k, 0, -1):
            dp[j] = dp[j] + dp[j-1] + 1
    return moves


def main():
    import sys
    n, k = map(int, sys.stdin.read().strip().split())
    print(min_parachutes(k, n))


if __name__ == "__main__":
    main()
