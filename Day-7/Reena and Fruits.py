def max_sum_of_min_pairs(nums):
    nums.sort()
    total = 0
    for i in range(0, len(nums), 2):
        total += nums[i]
    return total


# -------- Driver Code --------
if __name__ == "__main__":
    import sys
    data = list(map(int, sys.stdin.read().split()))
    
    n2 = data[0]          # 2N
    nums = data[1:]       # fruits array
    
    print(max_sum_of_min_pairs(nums))
