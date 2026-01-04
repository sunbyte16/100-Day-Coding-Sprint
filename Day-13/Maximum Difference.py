def user_logic(n, arr):
    min_so_far = arr[0]
    max_diff = -1

    for i in range(1, n):
        diff = arr[i] - min_so_far
        if diff > max_diff:
            max_diff = diff

        if arr[i] < min_so_far:
            min_so_far = arr[i]

    return max_diff if max_diff > 0 else -1


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx + N]))
        idx += N
        
        results.append(user_logic(N, arr))
    
    for res in results:
        print(res)


if __name__ == "__main__":
    main()
