def k_closest_points():
    import sys
    data = sys.stdin.read().split()
    
    idx = 0
    N = int(data[idx]); idx += 1
    
    points = []
    for _ in range(N):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        points.append((x, y))
    
    K = int(data[idx])
    
    # Sort points by distance from origin
    points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
    
    # Print first K points
    for i in range(K):
        print(points[i][0], points[i][1])


if __name__ == "__main__":
    k_closest_points()
