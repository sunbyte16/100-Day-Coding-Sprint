def compareBits(a, b):
    n = len(a)
    total = 0
    
    for i in range(len(b) - n + 1):
        diff = 0
        for j in range(n):
            if a[j] != b[i + j]:
                diff += 1
        total += diff
    
    return total


if __name__ == '__main__':
    line1 = input().strip()
    line2 = input().strip()
    a = line1.split()[0]
    b = line2.split()[0]
    print(compareBits(a, b))
