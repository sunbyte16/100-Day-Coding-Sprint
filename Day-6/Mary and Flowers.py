def find_flower_indices(n, t, arr):
    left, right = 0, n - 1

    while left < right:
        s = arr[left] + arr[right]

        if s == t:
            return (left, right)
        elif s < t:
            left += 1
        else:
            right -= 1

    return (-1, -1)  # This won't happen as per problem statement


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    t = int(data[1])
    arr = list(map(int, data[2:]))

    i, j = find_flower_indices(n, t, arr)
    print(i, j)


if __name__ == "__main__":
    main()
