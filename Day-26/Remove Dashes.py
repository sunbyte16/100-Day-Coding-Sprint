def process_dashes(n, s):
    stack = []
    
    for ch in s:
        if ch == '_':
            if not stack:
                return "-1"   # No letter to remove
            stack.pop()
        else:
            stack.append(ch)
    
    if not stack:
        return "-1"
    
    return "".join(stack)


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    s = data[1]
    
    result = process_dashes(n, s)
    print(result)

if __name__ == "__main__":
    main()
