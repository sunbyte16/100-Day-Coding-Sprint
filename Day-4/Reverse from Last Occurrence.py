def transform_string(s, ch):
    idx = s.rfind(ch)
    
    # If character not found, return original string
    if idx == -1:
        return s
    
    # Reverse substring from last occurrence to end
    return s[:idx] + s[idx:][::-1]


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    s = data[0]
    ch = data[1]
    
    print(transform_string(s, ch))


if __name__ == "__main__":
    main()
