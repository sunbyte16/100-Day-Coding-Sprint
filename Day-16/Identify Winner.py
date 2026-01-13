def find_winner(arr):
    freq = {}

    # Count frequency
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Find first unique number
    for num in arr:
        if freq[num] == 1:
            return num

    return 0


def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))  # STRICT slicing

    print(find_winner(arr))


if __name__ == "__main__":
    main()
