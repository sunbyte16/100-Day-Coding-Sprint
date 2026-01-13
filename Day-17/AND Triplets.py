def countTriplets(n, arr):
    from collections import defaultdict

    pair_and_count = defaultdict(int)

    # Step 1: Count all pairwise AND results
    for i in range(n):
        for j in range(n):
            pair_and_count[arr[i] & arr[j]] += 1

    # Step 2: Count valid triplets
    result = 0
    for k in range(n):
        for val in pair_and_count:
            if (val & arr[k]) == 0:
                result += pair_and_count[val]

    return result


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:1 + n]))

    print(countTriplets(n, arr))


if __name__ == "__main__":
    main()
