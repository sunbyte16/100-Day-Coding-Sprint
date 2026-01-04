def minimum_time_to_solve_problems(n, k, times):
    # Edge cases
    if k == 0:
        return 0
    if n == 0:
        return -1

    # If any member takes 0 time, infinite problems can be solved
    if 0 in times:
        return 0

    # Binary search bounds
    left, right = 1, min(times) * k
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        total = 0
        for t in times:
            total += mid // t
            if total >= k:
                break

        if total >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    k = int(data[1])
    times = list(map(int, data[2:2+n]))
    
    print(minimum_time_to_solve_problems(n, k, times))


if __name__ == "__main__":
    main()
