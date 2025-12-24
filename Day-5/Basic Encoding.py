def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    Q = int(data[0])
    
    freq_map = {}
    idx = 1

    # Read queries
    for _ in range(Q):
        A = int(data[idx])
        B = int(data[idx + 1])
        idx += 2
        freq_map[B] = freq_map.get(B, 0) + A

    # If only one unique number
    if len(freq_map) <= 1:
        print(0)
        return

    # Find min and max frequencies
    min_freq = min(freq_map.values())
    max_freq = max(freq_map.values())

    # Numbers with min and max frequencies
    min_numbers = [num for num, freq in freq_map.items() if freq == min_freq]
    max_numbers = [num for num, freq in freq_map.items() if freq == max_freq]

    # Apply tie-breaking rules
    lowest_num = min(min_numbers)     # smallest number with lowest freq
    highest_num = max(max_numbers)    # largest number with highest freq

    print(abs(highest_num - lowest_num))


if __name__ == "__main__":
    main()
