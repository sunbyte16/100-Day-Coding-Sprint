def follows_ab_pattern(s):
    """
    Parameters:
        s (str): Input string representing the row of boxes
    Returns:
        str: "YES" if the sequence follows the "ab" pattern, otherwise "NO"
    """
    seen_b = False

    for ch in s:
        if ch == 'b':
            seen_b = True
        elif ch == 'a' and seen_b:
            return "NO"

    return "YES"


def main():
    import sys
    s = sys.stdin.read().strip()
    
    result = follows_ab_pattern(s)
    print(result)

if __name__ == "__main__":
    main()
