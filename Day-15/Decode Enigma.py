def interpret(s):
    """
    Parameters:
        s (str): Input string
    Returns:
        str: Interpreted command string
    """
    result = []
    i = 0
    n = len(s)

    while i < n:
        if s[i] == 'S':
            result.append("send")
            i += 1
        elif i + 1 < n and s[i:i+2] == "[]":
            result.append("the")
            i += 2
        elif i + 4 < n and s[i:i+5] == "[sps]":
            result.append("ships")
            i += 5
        else:
            # Safety fallback (should not occur with valid input)
            i += 1

    return " ".join(result)


def main():
    import sys
    s = sys.stdin.read().strip()
    print(interpret(s))


if __name__ == "__main__":
    main()
