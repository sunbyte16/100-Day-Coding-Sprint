def find_youngest_member(n, m, gifts):
    """
    Parameters:
        n (int): Number of family members
        m (int): Number of gifts exchanged
        gifts (list of tuples): (a_i, b_i) meaning a_i gave a gift to b_i
    Returns:
        int: Youngest member or -1
    """
    # in_degree[i]: gifts received by i
    # out_degree[i]: gifts given by i
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    for a, b in gifts:
        out_degree[a] += 1
        in_degree[b] += 1

    # Youngest member: receives from all others and gives none
    for i in range(1, n + 1):
        if out_degree[i] == 0 and in_degree[i] == n - 1:
            return i

    return -1


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    m = int(data[1])

    gifts = []
    idx = 2
    for _ in range(m):
        a_i = int(data[idx])
        b_i = int(data[idx + 1])
        gifts.append((a_i, b_i))
        idx += 2

    result = find_youngest_member(n, m, gifts)
    print(result)


if __name__ == "__main__":
    main()