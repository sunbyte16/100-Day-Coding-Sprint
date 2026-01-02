def user_logic(n, s):
    depth = 0
    max_depth = 0

    for ch in s:
        if ch == '(':
            depth += 1
            if depth > max_depth:
                max_depth = depth
        elif ch == ')':
            depth -= 1

    return max_depth


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    s = data[1]

    print(user_logic(n, s))


if __name__ == "__main__":
    main()
