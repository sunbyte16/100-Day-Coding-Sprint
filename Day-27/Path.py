def user_logic(n, s):
    from collections import defaultdict
    
    pieces = defaultdict(int)
    buy = 0
    
    for ch in s:
        if ch.islower():
            pieces[ch] += 1
        else:
            need = ch.lower()
            if pieces[need] > 0:
                pieces[need] -= 1
            else:
                buy += 1
    
    return buy


def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    s = data[1]

    print(user_logic(n, s))


if __name__ == "__main__":
    main()
