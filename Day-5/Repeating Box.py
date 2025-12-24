def find_repeated_box():
    import sys
    data = list(map(int, sys.stdin.read().split()))
    
    m = data[0]              # total boxes = 2*n
    labels = data[1:]
    target = m // 2          # repeated count
    
    freq = {}
    for x in labels:
        freq[x] = freq.get(x, 0) + 1
        if freq[x] == target:
            print(x)
            return

if __name__ == "__main__":
    find_repeated_box()
