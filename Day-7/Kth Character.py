import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    s = data[2]
    
    # kth character after reversing
    print(s[n - k])

if __name__ == "__main__":
    main()
