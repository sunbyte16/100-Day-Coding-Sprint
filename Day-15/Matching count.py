def matching_count(items, ruleKey, ruleValue):
    # Map ruleKey to the corresponding index
    key_index = {
        "type": 0,
        "color": 1,
        "name": 2
    }[ruleKey]

    count = 0
    for item in items:
        if item[key_index] == ruleValue:
            count += 1

    return count


def main():
    import sys
    data = sys.stdin.read().strip().splitlines()

    n = int(data[0])
    items = []

    # Read items
    for i in range(1, n + 1):
        items.append(data[i].split())

    ruleKey = data[n + 1].strip()
    ruleValue = data[n + 2].strip()

    print(matching_count(items, ruleKey, ruleValue))


if __name__ == "__main__":
    main()
