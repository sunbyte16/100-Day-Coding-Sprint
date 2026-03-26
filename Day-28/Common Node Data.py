import sys

data = list(map(int, sys.stdin.read().split()))

n = data[0]
m = data[1]

arr1 = data[2:2+n]
arr2 = data[2+n:2+n+m]

i = n - 1
j = m - 1

ans = -1

while i >= 0 and j >= 0:
    if arr1[i] == arr2[j]:
        ans = arr1[i]
    else:
        break
    i -= 1
    j -= 1

print(ans)
