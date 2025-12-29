def find_class_id(arr):
    n = len(arr)

    # Check first class
    if n >= 2 and arr[0] >= arr[1]:
        return 0

    # Check middle classes
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return i

    # Check last class
    if n >= 2 and arr[n - 1] >= arr[n - 2]:
        return n - 1


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().split()))
    print(find_class_id(arr))
