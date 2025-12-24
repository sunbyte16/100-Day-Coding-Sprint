def process(s):
    result = []
    for ch in s:
        if ch == '#':
            if result:
                result.pop()
        else:
            result.append(ch)
    return "".join(result)

def main():
    bob = input().strip()
    alice = input().strip()

    if process(bob) == process(alice):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
