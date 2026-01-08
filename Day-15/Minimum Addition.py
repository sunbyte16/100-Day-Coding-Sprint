def minimum_addition(str):
    # Step 1: Replace last character with 'c'
    s = str[:-1] + 'c'
    n = len(s)
    
    # Step 2: Create combined string for KMP LPS
    temp = s + '#' + s[::-1]
    
    # Step 3: Compute LPS array
    lps = [0] * len(temp)
    for i in range(1, len(temp)):
        length = lps[i-1]
        while length > 0 and temp[i] != temp[length]:
            length = lps[length-1]
        if temp[i] == temp[length]:
            length += 1
        lps[i] = length
    
    # Step 4: Minimum addition
    return n - lps[-1]


def main():
    import sys
    str = sys.stdin.read().strip()
    print(minimum_addition(str))


if __name__ == "__main__":
    main()
