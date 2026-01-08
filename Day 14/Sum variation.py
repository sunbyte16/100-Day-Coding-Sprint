def calculate_sum(nums):
    total_sum = sum(nums)

    positive_set = set()
    for num in nums:
        if num > 0:
            positive_set.add(num)

    missing = 1
    while missing in positive_set:
        missing += 1

    ascii_value = ord(str(missing)[0])
    return total_sum + ascii_value


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    nums = list(map(int, data[1:1+n]))  # ✅ FIX HERE
    
    result = calculate_sum(nums)
    print(result)


if __name__ == "__main__":
    main()
