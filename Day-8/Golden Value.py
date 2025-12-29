def golden_value(arr):
    n = len(arr)
    MAX_BIT = 31  # FIX 1: support large values
    answer = 0

    for b in range(MAX_BIT):
        # count[parity][bit]
        count = [[0, 0], [0, 0]]

        # empty prefix
        count[0][0] = 1

        pref = 0
        odd_sum = 0
        even_sum = 0

        for i in range(n):
            pref ^= arr[i]
            parity = (i + 1) & 1
            bit = (pref >> b) & 1

            # Odd-length → same parity
            odd_sum += count[parity][1 - bit]

            # Even-length → different parity
            even_sum += count[1 - parity][1 - bit]

            count[parity][bit] += 1

        # FIX 2: NO absolute value
        answer += (even_sum - odd_sum) * (1 << b)

    return answer


# -------- Input --------
n = int(input().strip())
arr = list(map(int, input().split()))
print(golden_value(arr))
