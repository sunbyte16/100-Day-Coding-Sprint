n = int(input())
arr = list(map(int, input().split()))

if n % 2 == 0:
    print(0)
else:
    prefix_xor = 0
    result = 0
    for x in arr:
        prefix_xor ^= x
        result ^= prefix_xor
    print(result)
