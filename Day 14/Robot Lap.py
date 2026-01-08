def car_returns_to_origin(n, moves):
    x, y = 0, 0

    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'L':
            x -= 1
        elif move == 'R':
            x += 1

    return "YES" if x == 0 and y == 0 else "NO"


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    moves = ''.join(data[1:])[:n]   # ✅ FIXED & SAFE
    
    result = car_returns_to_origin(n, moves)
    print(result)


if __name__ == "__main__":
    main()
