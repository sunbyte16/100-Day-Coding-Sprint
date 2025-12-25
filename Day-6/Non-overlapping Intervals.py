def erase_overlap_intervals(intervals):
    if not intervals:
        return 0

    # Sort intervals by end time
    intervals.sort(key=lambda x: x[1])

    count_non_overlap = 1
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] >= prev_end:
            count_non_overlap += 1
            prev_end = intervals[i][1]

    return len(intervals) - count_non_overlap


if __name__ == '__main__':
    import sys
    data = sys.stdin.read().split()
    
    N = int(data[0])
    M = int(data[1])  # Always 2, not needed further
    intervals = []
    
    idx = 2
    for _ in range(N):
        intervals.append([int(data[idx]), int(data[idx + 1])])
        idx += 2

    print(erase_overlap_intervals(intervals))
