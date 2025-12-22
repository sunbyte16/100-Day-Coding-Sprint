def nth_row_pascal(n):
    row = []
    val = 1
    for k in range(n + 1):
        row.append(val)
        val = val * (n - k) // (k + 1)
    return row

def main():
    import sys
    n = int(sys.stdin.read().strip())
    result = nth_row_pascal(n)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
