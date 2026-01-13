from math import gcd
from collections import defaultdict

def count_pairs_divisible_by_k(k, n, arr):
    freq = defaultdict(int)
    
    # Count frequency of gcd of each element with k
    for num in arr:
        g = gcd(num, k)
        freq[g] += 1

    gcd_list = list(freq.keys())
    ans = 0

    # Count valid pairs
    for i in range(len(gcd_list)):
        g1 = gcd_list[i]
        for j in range(i, len(gcd_list)):
            g2 = gcd_list[j]
            if (g1 * g2) % k == 0:
                if i == j:
                    # Choose 2 out of freq[g1] => freq[g1] * (freq[g1]-1) // 2
                    ans += freq[g1] * (freq[g1] - 1) // 2
                else:
                    ans += freq[g1] * freq[g2]
    
    return ans

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    k = int(data[0])
    n = int(data[1])
    arr = list(map(int, data[2:2+n]))
    
    result = count_pairs_divisible_by_k(k, n, arr)
    print(result)
