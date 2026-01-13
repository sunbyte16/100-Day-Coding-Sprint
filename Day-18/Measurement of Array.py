def array_measurement(n, arr):
    MOD = 10**9 + 7

    # Step 1: Pair value with original index
    arr_with_index = [(value, idx) for idx, value in enumerate(arr)]
    
    # Step 2: Sort by value
    arr_with_index.sort(key=lambda x: x[0])
    
    # Step 3: Track last occurrence of each value in sorted array
    last_index = {}
    for i, (val, _) in enumerate(arr_with_index):
        last_index[val] = i  # always update to get last occurrence
    
    # Step 4: Compute measurement
    measurement = 0
    for val, orig_idx in arr_with_index:
        measurement = (measurement + orig_idx + last_index[val]) % MOD
    
    return measurement

# Main function to read input
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))
    
    print(array_measurement(n, arr))
