def modify_array(n, arr):
    max_so_far = 0
    result = []

    for x in arr:
        max_so_far = max(max_so_far, x)
        result.append(x + max_so_far)

    return result


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    
    modified = modify_array(n, arr)
    print(*modified)
