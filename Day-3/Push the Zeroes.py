n = int(input())
arr = list(map(int, input().split()))

# Two pointer approach
write_idx = 0

for i in range(n):
    if arr[i] != 0:
        arr[write_idx] = arr[i]
        write_idx += 1

# Fill remaining positions with zeros
while write_idx < n:
    arr[write_idx] = 0
    write_idx += 1

print(*arr)
