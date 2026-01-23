def find_and_replace_pattern(words, pattern):
    def match(word, pattern):
        if len(word) != len(pattern):
            return False
        
        w2p = {}
        p2w = {}
        
        for w, p in zip(word, pattern):
            if w in w2p and w2p[w] != p:
                return False
            if p in p2w and p2w[p] != w:
                return False
            w2p[w] = p
            p2w[p] = w
        
        return True

    matched = []
    for word in words:
        if match(word, pattern):
            matched.append(word)

    return len(matched), matched


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    words = data[1:n+1]
    pattern = data[n+1]
    
    cnt, res = find_and_replace_pattern(words, pattern)
    
    print(cnt)
    if cnt > 0:
        print(" ".join(res))


if __name__ == "__main__":
    main()
