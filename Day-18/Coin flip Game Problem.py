def find(m):
    if m <= 0:
        return 0
    return int(m ** 0.5)


if __name__ == "__main__":
    m = int(input().strip())
    count = find(m)
    print(count)
