def min_cost_to_reach_end(V):
    n = len(V)
    dp = [0] * n

    for i in range(1, n):
        cost = dp[i - 1] + abs(V[i] - V[i - 1])

        if i >= 2:
            cost = min(cost, dp[i - 2] + abs(V[i] - V[i - 2]))

        if i >= 3:
            cost = min(cost, dp[i - 3] + abs(V[i] - V[i - 3]))

        dp[i] = cost

    return dp[-1]


# Input handling
n = int(input().strip())
V = list(map(int, input().split()))
print(min_cost_to_reach_end(V))
