def find_k_nearest_points(points, k):
    # Annotate each point with its squared distance and original index
    points_with_dist = []
    for idx, (x, y) in enumerate(points):
        dist_sq = x*x + y*y
        points_with_dist.append((dist_sq, idx, x, y))
    
    # Sort based on distance first, then index to maintain input order for ties
    points_with_dist.sort()
    
    # Pick the first k points after sorting
    result = []
    for i in range(k):
        _, _, x, y = points_with_dist[i]
        result.append([x, y])
    
    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Number of points
    k = int(data[1])  # Number of nearest points to find
    
    points = []
    index = 2
    for _ in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        points.append([x, y])
        index += 2
    
    # Call user logic function and get the result
    result = find_k_nearest_points(points, k)
    
    # Print the result
    for point in result:
        print(point[0], point[1])

if __name__ == "__main__":
    main()
