def count_pairs(arr):
    from collections import defaultdict

    msb_count = defaultdict(int)

    for x in arr:
        if x == 0:
            continue
        msb = x.bit_length() - 1
        msb_count[msb] += 1

    ans = 0
    for cnt in msb_count.values():
        ans += cnt * (cnt - 1) // 2

    return ans


# Input
N = int(input())
A = list(map(int, input().split()))

print(count_pairs(A))
