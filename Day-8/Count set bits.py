def count_total_set_bits(n):
    dp = [0] * (n + 1)
    total = 0

    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
        total += dp[i]

    return total


if __name__ == "__main__":
    n = int(input().strip())
    print(count_total_set_bits(n))
