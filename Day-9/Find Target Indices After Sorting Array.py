import bisect

def find_target_indices(arr, K):
    arr.sort()
    # Find the first occurrence using bisect_left
    left = bisect.bisect_left(arr, K)
    # Find the index just after the last occurrence using bisect_right
    right = bisect.bisect_right(arr, K)
    
    # The indices of K in sorted array are from left to right-1
    indices = list(range(left, right))
    
    return len(indices), indices

if __name__ == "__main__":
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    K = int(input().strip())
    
    count, indices = find_target_indices(arr, K)
    
    print(count)
    if count > 0:
        print(" ".join(map(str, indices)))
