def count_consistent_cars(components, n, models):
    allowed = set(components)
    count = 0
    
    line = ' '.join(models).split()
    for model in line:
        consistent = True
        for char in model:
            if char not in allowed:
                consistent = False
                break
        if consistent:
            count += 1
    
    return count


if __name__ == '__main__':
    components = input().strip()
    n = int(input().strip())
    line = input().strip()
    models = line.split()
    result = count_consistent_cars(components, n, models)
    print(result)
