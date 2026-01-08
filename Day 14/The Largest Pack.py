def find_largest_pack(N):
    """
    Parameters:
        N (int): Number of marbles produced in a day
    Returns:
        int: Number of marbles in the largest pack that can be produced
    """
    return 1 << (N.bit_length() - 1)


def main():
    import sys
    
    data = sys.stdin.read().strip()
    N = int(data)
    
    result = find_largest_pack(N)
    print(result)


if __name__ == "__main__":
    main()
