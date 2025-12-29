def majority_subsequence(votes):
    votes.sort(reverse=True)   # non-increasing order
    total_sum = sum(votes)

    picked = []
    picked_sum = 0

    for v in votes:
        picked.append(v)
        picked_sum += v
        if picked_sum > total_sum - picked_sum:
            break

    return picked


# Input handling
n = int(input().strip())
votes = list(map(int, input().split()))

result = majority_subsequence(votes)
print(*result)
