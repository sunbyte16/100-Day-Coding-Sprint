from collections import deque

def max_submission_queue_size(n, arr):
    q = deque()
    max_size = 0

    for t in arr:
        # Remove all submissions <= t - 5000
        while q and q[0] <= t - 5000:
            q.popleft()

        # Add current submission
        q.append(t)

        # Track maximum size
        max_size = max(max_size, len(q))

    return max_size


# -------- Driver Code --------
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    print(max_submission_queue_size(n, arr))
