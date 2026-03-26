import sys

def change_longest(arr, x):
    max_val = max(arr)
    for i in range(len(arr)):
        if arr[i] == max_val:
            arr[i] = max(0, arr[i] - x)


def pole_arrangement(arr):
    n = len(arr)

    # Check all triplets i < j < k
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:  # middle should be taller than first
                for k in range(j + 1, n):
                    if arr[i] < arr[k] < arr[j]:
                        return True
    return False


# ----------- MAIN -------------
data = list(map(int, sys.stdin.read().split()))

n = data[0]
x = data[1]
arr = data[2:2+n]

# Step 1: modify tallest poles
change_longest(arr, x)

# Step 2: check arrangement
result = pole_arrangement(arr)

# Output
print(1 if result else 0)
