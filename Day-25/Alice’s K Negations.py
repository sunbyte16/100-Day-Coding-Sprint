import heapq

def max_sum_after_k_operations(arr, k):
    # Convert arr into a min-heap
    heapq.heapify(arr)
    
    for _ in range(k):
        # Pop the smallest element, flip it, push back
        smallest = heapq.heappop(arr)
        heapq.heappush(arr, -smallest)
    
    return sum(arr)

# Driver code
if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = max_sum_after_k_operations(arr, k)
    print(result)
