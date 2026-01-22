def rearrange_blocks_to_form_name(S, P):
    from collections import Counter

    n, m = len(S), len(P)
    if m > n:
        return 0, []

    p_count = Counter(P)
    window = Counter(S[:m])

    result = []

    if window == p_count:
        result.append(1)

    for i in range(m, n):
        window[S[i]] += 1
        window[S[i - m]] -= 1

        if window[S[i - m]] == 0:
            del window[S[i - m]]

        if window == p_count:
            result.append(i - m + 2)

    return len(result), result


# Correct input handling for this judge
S = input().strip()
P = input().strip()

count, indices = rearrange_blocks_to_form_name(S, P)

print(count)
if count == 0:
    print("none")
else:
    print(" ".join(map(str, indices)))
