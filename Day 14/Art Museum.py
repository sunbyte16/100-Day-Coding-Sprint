def user_logic(n, positions):
    xs = [p[0] for p in positions]
    ys = [p[1] for p in positions]

    xs.sort()
    ys.sort()

    # Odd number of lakes → single median point
    if n % 2 == 1:
        return 1

    # Even number of lakes → range of medians
    x_left = xs[n // 2 - 1]
    x_right = xs[n // 2]
    y_left = ys[n // 2 - 1]
    y_right = ys[n // 2]

    return (x_right - x_left + 1) * (y_right - y_left + 1)


def main():
    import sys
    data = sys.stdin.read().strip().split()

    if not data:
        return

    n = int(data[0])
    positions = []

    idx = 1
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        positions.append((x, y))
        idx += 2

    print(user_logic(n, positions))


if __name__ == "__main__":
    main()
