def is_valid(arr):
    s = 0
    for x in arr:
        s += x
        if s == 0:
            return False
    return True


n = int(input().strip())
arr = list(map(int, input().split()))

# Non-decreasing order
asc = sorted(arr)

# Non-increasing order
desc = sorted(arr, reverse=True)

asc_valid = is_valid(asc)
desc_valid = is_valid(desc)

if not asc_valid and not desc_valid:
    print("IMPOSSIBLE")

else:
    print("POSSIBLE")
    if asc_valid and desc_valid:
        # choose the one with larger first element
        if desc[0] >= asc[0]:
            print(*desc)
        else:
            print(*asc)
    elif desc_valid:
        print(*desc)
    else:
        print(*asc)
