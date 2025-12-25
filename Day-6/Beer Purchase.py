def max_beers(N, X, A):
    A.sort()
    
    prefix = 0
    total = 0

    for k in range(1, N + 1):
        prefix += A[k - 1]
        if prefix > X:
            break
        
        total += (X - prefix) // k + 1

    return total


if __name__ == "__main__":
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max_beers(N, X, A))
