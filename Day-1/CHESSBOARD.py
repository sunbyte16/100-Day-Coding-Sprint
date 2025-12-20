def determine_color(s):
    """
    Parameters:
        s (str): Input string representing a position like 'a1', 'b2', etc.
    Returns:
        str: "Black" or "White" based on the problem statement.
    """
    col_char = s[0]
    row = int(s[1])

    col = ord(col_char) - ord('a') + 1  # a=1, b=2, ...

    if (col + row) % 2 == 0:
        return "Black"
    else:
        return "White"


def main():
    import sys
    input = sys.stdin.read
    s = input().strip()
    result = determine_color(s)
    print(result)


if __name__ == "__main__":
    main()