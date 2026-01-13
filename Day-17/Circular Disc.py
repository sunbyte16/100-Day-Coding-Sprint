def minTimeToType(word):
    # Sort the string first
    word = ''.join(sorted(word))

    current = 'a'
    time = 0

    for ch in word:
        # Calculate circular distance
        diff = abs(ord(ch) - ord(current))
        move = min(diff, 26 - diff)

        # Move time + typing time
        time += move + 1

        # Update current pointer
        current = ch

    return time


def main():
    import sys
    word = sys.stdin.read().strip()
    print(minTimeToType(word))


if __name__ == "__main__":
    main()
