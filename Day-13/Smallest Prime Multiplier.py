def compute_x(p, n):
    import math
    return (p * n) // math.gcd(p, n)


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    p = int(data[0])
    n = int(data[1])
    
    result = compute_x(p, n)
    print(result)

if __name__ == "__main__":
    main()
