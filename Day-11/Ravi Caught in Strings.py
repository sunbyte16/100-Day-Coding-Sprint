import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]
    
    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    max_len = 1
    for i in range(n):
        # Odd length palindromes
        len1 = expand_around_center(i, i)
        # Even length palindromes
        len2 = expand_around_center(i, i + 1)
        max_len = max(max_len, len1, len2)
    
    print(max_len)

if __name__ == "__main__":
    main()
