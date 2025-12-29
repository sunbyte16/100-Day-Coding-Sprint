def find_class_id(arr):
    n = len(arr)
    
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return i


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().split()))
    print(find_class_id(arr))
