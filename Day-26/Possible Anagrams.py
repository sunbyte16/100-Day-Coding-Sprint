def find_anagram_indices(secret1, secret2):
    n = len(secret1)
    m = len(secret2)
    
    if m > n:
        return []
    
    freq = [0] * 26
    
    # Build frequency for secret2
    for ch in secret2:
        freq[ord(ch) - 97] += 1
    
    count = m
    result = []
    left = 0
    
    for right in range(n):
        idx = ord(secret1[right]) - 97
        
        if freq[idx] > 0:
            count -= 1
        freq[idx] -= 1
        
        # Window size exceeded
        if right - left + 1 > m:
            lidx = ord(secret1[left]) - 97
            if freq[lidx] >= 0:
                count += 1
            freq[lidx] += 1
            left += 1
        
        if count == 0:
            result.append(left)
    
    return result


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    secret1 = data[0]
    secret2 = data[1]
    
    result = find_anagram_indices(secret1, secret2)
    
    if not result:
        print("Empty Array")
    else:
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
